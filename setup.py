from primes import get_p_and_q
from random import randint
from math import gcd as bltin_gcd


def egcd(a, b):
    '''
    Uses euclidean algorithm to recursively 
    calculate gcd of a and b
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    '''
    Calculates the multipicative inverse of a
    modulo m
    '''
    g, x, y = egcd(a, m)
    if g != 1: # a and m aren't co-prime then a has no inverse
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
    
def get_n():
    '''
    Generates primes and uses them to calculate
    n and phi of n
    '''
    p_q = get_p_and_q()#generate_prime(2)
    n = p_q[0] * p_q[1]
    
    phi_n = (p_q[0] - 1) * (p_q[1] - 1)
    
    return n, phi_n
    
    
def get_public_key(n, phi_n):
    '''
    Returns n and e as a tuple,
    e is calculated by generating random numbers
    between 10 and phi_n and if it is co-prime with
    phi_n then it is selected
    '''
    invertible = False
    while not invertible:
        e = randint(10, phi_n)
        if bltin_gcd(e, phi_n) == 1:
            invertible = True
            
    return n, e


def get_private_key(e, phi_n):
    '''
    Returns the multipicative inverse of e in z phi_n
    '''
    d = modinv(e, phi_n)
    
    return d

def setup():
    '''
    Sets up the private public keys needed
    and returns all 3 aswell as eulers thing, phi_n lol
    '''
    n, phi_n = get_n() # Generates n and phi_n
    public_key = get_public_key(n, phi_n) # Generates the public key from the n and phi_n
    d = get_private_key(public_key[1], phi_n) # Generates the private key used to decrypt
    
    return public_key, d, phi_n # Returns ((n, e), d, phi_n)



if __name__ == '__main__':
    print(setup())