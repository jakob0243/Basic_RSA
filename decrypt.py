'''test: e = 7 n = 77 d = 43'''

LETTERS = {'26': 'A', '27': 'B', '02': 'C', '03': 'D', '04': 'E',
           '05': 'F', '06': 'G', '07': 'H', '08': 'I', '09': 'J', '10': 'K', 
           '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', 
           '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', 
           '23': 'X', '24':'Y', '25': 'Z'} # A and B are set to 26 and 27 as if they were 00 and 01, A and B would encrypt to 00 and 01.


def split_message(message):
    '''
    Splits message into a list of 2 digit nums
    '''
    cipher_lets = []
    letter = ''
    count = 1
    for char in message:
        letter += char
        if count % 2 == 0:
            cipher_lets.append(letter)
            letter = ''
            count = 1
        else:
            count += 1
            
    return cipher_lets


def dif_splitter(message):
    '''
    Splits message into list, where each item in the
    list is a word
    '''
    message = message.split(' ')
    if message[0] == '':
        message.pop(0)
    
    return message


def decrypt(cipher_text, n, d):
    '''
    Takes cipher text, the public key and the private key
    and decrypts message. Returning it as a string with no spaces
    '''
    cipher_lets = dif_splitter(cipher_text)
    plain_text = ''
    text = ''
    
    for char in cipher_lets:
        normal_char = pow(int(char), int(d), int(n)) # Calculates char^d mod n
        if len(str(normal_char)) < 2:
            normal_char = '0' + str(normal_char)
        plain_text += str(normal_char)
        normal_char = LETTERS[str(normal_char)] # Changes the decrypted int to a char according to dict LETTERS
        text += normal_char
    
    return text