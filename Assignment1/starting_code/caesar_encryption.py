#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:56:01 2021

@author: bing
"""

import random
import string


def caesarEncrypt(message, codebook, shift):
    '''
    - you can compute the index of a character, or,
    - you can convert the codebook into a dictionary
    '''

    encrypted = ""
    # put your code here
    for i in message:
        if str(i).isalpha():
            temp = ''
            for j in range(0, len(codebook)-1):
                if i == codebook[j]:
                    temp = codebook[(j+shift) % len(codebook)]
                    break
            encrypted += temp
        else:
            encrypted += i
    return encrypted


def caesarDecrypt(message, codebook, shift):
    decrypted = ""
    # put your code here
    for i in message:
        if str(i).isalpha():
            temp = ''
            for j in range(0, len(codebook)-1):
                if i == codebook[j]:
                    temp = codebook[(j-shift) % len(codebook)]
                    break
            decrypted += temp
        else:
            decrypted += i
    return decrypted


if __name__ == "__main__":
    # The following several lines generate the codebook
    # Please don't change it
    random.seed("Caesar")

    codebook = []
    for e in string.ascii_letters:
        codebook.append(e)

    random.shuffle(codebook)
    print("Your codebook:")
    print(codebook)
    # end of the codebook generation

    m = "Hello Kitty!"
    shift = 10000

    encoded = caesarEncrypt(m, codebook, shift)
    print("Origin:", m)
    print("Encoded:", encoded)
    decoded = caesarDecrypt(encoded, codebook, shift)
    print("Decoded", decoded)
