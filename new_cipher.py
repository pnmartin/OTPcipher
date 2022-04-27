import random
import re

def generatePad(inp):
    char_list = []
    while inp > 0:
        char_list.append(chr(random.randrange(65,91,1)))
        inp -= 1
    f = open("otpad.txt", "w")
    f.write("".join(char_list))
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


def encipher(message_file, otp):
    enci = []
    en_pad = []
    
    with open(otp) as file:
        pad = file.read()
        for let in pad:
            let = ord(let)
            en_pad.append(let)

    with open(message_file) as file:
        message = file.read()

    j = 0  
    for i in range(0, len(message)):
        enci.append(shift_pos(message[i], en_pad[j] - 65))
        if message[i].isalnum():
            j+=1
    
    f = open("encrypted-message.txt", "w")
    f.write("".join(enci))
    f.close()

    #print(enci)
    return enci
    

'''message_file = input("Please input the file to be encrypted: ")
otpad = input("Please input the file containing the one time pad: ")

encipher(message_file, otpad)'''

#print(encipher('rall.txt', "qwert.txt"))


def decipher(message_file, otp):
    de_pad = []
    deci = []
    
    with open(otp) as file:
        pad = file.read()
        for let in pad:
            let = ord(let)
            de_pad.append(let)

    with open(message_file) as file:
        message = file.read()

    j = 0  
    for i in range(0, len(message)):
        deci.append(shift_pos(message[i], -(de_pad[j] - 65)))
        if message[i].isalnum():
            j+=1

    f = open("decrypted-message.txt", "w")
    f.write("".join(deci))
    f.close()

    return deci


#print(decipher('encrypted-messs.txt', "qwert.txt"))


'''dec_file = input("Please input the file to be decrypted: ")
otp = input("Please input the file containing the one time pad: ")

decipher(dec_file, otp)'''

'''with open('decrypted-message.txt') as file:
	text = file.read()
	print(text)'''
