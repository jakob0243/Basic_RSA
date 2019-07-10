'''raise errors test: e = 7 n = 77 d = 43'''

LETTERS = {'A': '26', 'B': '27', 'C': '02', 'D': '03', 'E': '04',
           'F': '05', 'G': '06', 'H': '07', 'I': '08', 'J': '09', 'K': '10', 
           'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 
           'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 
           'X': '23', 'Y':'24', 'Z': '25'} # A and B are set to 26 and 27 as if they were 00 and 01, A and B would encrypt to 00 and 01.

def encrypt_message(message, e, n):
    '''
    Takes message and encrypts the message, assuming
    message has only letters a-z and not case sensitive
    '''
    message = message.replace(' ', '')
    plain_text = ""
    cipher_text = ""
    # Iterates through each character in message encrypting it
    for char in message:
        char = char.upper()
        plain_text += LETTERS[char]
        encrypted = pow(int(LETTERS[char]), int(e), int(n)) # calculates char^e mod n
        if encrypted < 10:
            encrypted = ' 0' + str(encrypted) # adds 0 to start of string if char is less than 10
        else:
            encrypted = ' ' + str(encrypted)
            
        cipher_text += encrypted
    
    return cipher_text

            
            
    