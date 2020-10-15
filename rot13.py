# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# Implement ROT13 simple letter substitution cipher
# Author of this cata made passing tests with bugs. Verified by online rot13 decoder

def rot13(message):

    cipher_alphabet = {
        "a": "n",
        "A": "N",

        "b": "o",
        "B": "O",

        "c": "p",
        "C": "P",

        "d": "q",
        "D": "Q",

        "e": "r",
        "E": "R",

        "f": "s",
        "F": "S",

        "g": "t",
        "G": "T",

        "h": "u",
        "H": "U",

        "i": "v",
        "I": "V",

        "j": "w",
        "J": "W",

        "k": "x",
        "K": "X",

        "l": "y",
        "L": "Y",

        "m": "z",
        "M": "N",

        "n": "a",
        "N": "A",

        "o": "b",
        "O": "B",

        "p": "c",
        "P": "C",

        "q": "d",
        "Q": "D",

        "r": "e",
        "R": "E",

        "s": "f",
        "S": "F",

        "t": "g",
        "T": "G",

        "u": "h",
        "U": "H",
        
        "v": "i",
        "V": "I",

        "w": "j",
        "W": "J",

        "x": "k",
        "X": "K",

        "y": "l",
        "Y": "L",

        "z": "m",
        "Z": "M"
    }

    cipher_text = ""

    for character in message:
        if character not in cipher_alphabet.keys():
            cipher_text += character
        else:
            cipher_text += cipher_alphabet[character]
    
    return cipher_text

print(rot13("ANRKNFE5LOGS3BTU"))