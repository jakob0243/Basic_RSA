from setup import setup
from encrypt import encrypt_message as encrypt
from decrypt import decrypt
from tkinter import *
from tkinter.ttk import *

class SystemGui:
    '''Class for doing stuff'''
    def __init__(self, box):
        self.box = box
        self.public_key, self.d, self.phi_n = setup()
        self.n = str(self.public_key[0])
        self.e = str(self.public_key[1])
        self.title = Label(self.box, text='RSA Cryptosystem', font=("Courier", 44))
        self.title.grid(row=0, column=1, columnspan = 5, rowspan=2)
        self.public_key = Label(self.box, text='Public Keys: ', font=("Courier", 22))
        self.public_key.grid(row=2, column=1, columnspan=3)
        self.public_keys = Label(self.box, text='n = {0}\ne = {1}'.format(self.n, self.e))
        self.public_keys.grid(row=4, column=2)
        self.private_label = Label(self.box, text='Private Key: ', font=("Courier", 22))
        self.private_label.grid(row=2, column=4, columnspan=3)
        self.private_key = Label(self.box, text='d: {0}\nphi_n: {1}'.format(self.d, self.phi_n))
        self.private_key.grid(row=4, column=4, columnspan=2)
        
        self.entry = Entry(self.box)
        self.entry.grid(row=6, column=2, columnspan=3)
        self.confirm_button = Button(self.box, text='encrypt', command=self.encrypt)
        self.confirm_button.grid(row=8, column=3)
        self.encrypted_label = Label(self.box, text='--------', font=("Courier", 22))
        self.encrypted_label.grid(row=10, column=2, columnspan=3)
        self.decrypt_button = Button(self.box, text='decrypt', command=self.decrypt)
        self.decrypt_button.grid(row=12, column=3)
        self.decrypted_label = Label(self.box, text='--------', font=("Courier", 22))
        self.decrypted_label.grid(row=14, column=2, columnspan=3)        
        
    def encrypt(self):
        '''
        Encrypts text by getting text from the entry box and encrypting it
        using the encrypt func. from encrypt.py
        '''
        text = self.entry.get()
        encrypted = encrypt(text, self.e, self.n)
        self.encrypted_label['text'] = str(encrypted)
        
        
    def decrypt(self):
        '''
        Takes the cipher text from the label and decrypts it using the
        decrypt func. from decrypt.py
        '''
        text = self.encrypted_label['text']
        plain_text = decrypt(text, self.n, self.d)
        self.decrypted_label['text'] = plain_text     
        
        
        
if __name__ == '__main__':
    window = Tk()
    gui = SystemGui(window)
    window.mainloop()