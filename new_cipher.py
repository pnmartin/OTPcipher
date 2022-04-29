import random
import re

def generatePad(inp):
    char_list = []
    while inp > 0:
        char_list.append(chr(random.randrange(65,91,1)))
        inp -= 1
    return char_list

def genPadfile(list):
    f = open("otpad.txt", "w")
    f.write("".join(list))
    f.close()



def shift_pos(message, shift):
    for let in message:
        if let.isalnum():
            let = ord(let)
            if (let > 64) and (let < 91):
                move = (let - 65 + (shift)) % 26 + 65

            else:
                move = (let - 97 + (shift)) % 26 + 97
            
            let = chr(move)
    return let


def otp_cipher(pad):
    en_pad = []
    for let in pad:
        let = ord(let)
        en_pad.append(let)
    return en_pad

def add_pad(message, en_pad):
    enci = []
    j = 0  
    for i in range(0, len(message)):
        enci.append(shift_pos(message[i], en_pad[j] - 65))
        if message[i].isalnum():
            j+=1
    return enci


def encipher(message_file, otp):
    
    with open(otp) as file:
        pad = file.read()
        en_pad = otp_cipher(pad)

    with open(message_file) as file:
        message = file.read()

    enci = add_pad(message, en_pad)
    
    f = open("encrypted-message.txt", "w")
    f.write("".join(enci))
    f.close()

    return enci
    

def sub_pad(message, de_pad):
    deci = []
    j = 0  
    for i in range(0, len(message)):
        deci.append(shift_pos(message[i], -(de_pad[j] - 65)))
        if message[i].isalnum():
            j+=1
    return deci

def decipher(message_file, otp):

    with open(otp) as file:
        pad = file.read()
        de_pad = otp_cipher(pad)

    with open(message_file) as file:
        message = file.read()

    deci = add_pad(message, de_pad)


    f = open("decrypted-message.txt", "w")
    f.write("".join(deci))
    f.close()

    return deci

