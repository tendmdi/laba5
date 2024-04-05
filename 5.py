import random

def generatepas(length):
    for _ in range(length):
        alphabet = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        yield alphabet

def invert_case(password):
    invertedpas = ''.join(map(lambda x: x.lower() if x.isupper() else x.upper(), password))
    return invertedpas

length = 10
passwordg = generatepas(length)
password = ''.join(passwordg)
invertedpas = invert_case(password)

print("Generated password:", password)
print("Inverted password:", invertedpas)
passwordg = generatepas(length)
password = ''.join(passwordg)
invertedpas = invert_case(password)

print("Generated password:", password)
print("Inverted password:", invertedpas)