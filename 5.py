import random

def generatepas(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

def invert_case(password):
    invertedpas = ''.join(map(lambda x: x.lower() if x.isupper() else x.upper(), password))
    return invertedpas

length = 10
password = generatepas(length)
invertedpas = invert_case(password)

print("Generated password:", password)
print("Inverted password:", invertedpas)
