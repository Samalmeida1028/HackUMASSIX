# path is CSV/file
import csv
import random
# file = open('CSV/input.csv', 'w+', newline='') -> create new file
# 'r' for reading 'w' for writing
# arr = file.readlines() creates an array of lines
# arr.split('|') -> splits by specified delimiter. make sure when you write data you separate values by delimiter

class testMorse():
    def __init__(self):
        self.charactersAvaliable={
            1: 'A', 2: 'B',
             3: 'C', 4: 'D', 5: 'E',
             6: 'F', 7: 'G', 8: 'H',
             9: 'I', 10: 'J', 11: 'K',
             12: 'L', 13: 'M', 14: 'N',
             15: 'O', 16: 'P', 17: 'Q',
             18: 'R', 19: 'S', 20: 'T',
             21: 'U', 22: 'V', 23: 'W',
            24: 'X', 25: 'Y', 26: 'Z',
             27: '1', 28: '2', 29: '3',
             30: '4', 31: '5', 32: '6',
             33: '7', 34: '8', 35: '9',
             36: '0', 37: ', ', 38: '. ',
             39: '?', 40: '/', 41: '-',
             42: '(', 43: ')', 44: ' '
        }

class Morse():
    def __init__(self):
        self.text = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ',': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-', ' ':'   '}

        self.morse = {'.-': 'A', '-...': 'B',
                                '-.-.': 'C', '-..': 'D', '.': 'E',
                                '..-.': 'F', '--.': 'G', '....': 'H',
                                '..': 'I', '.---': 'J', '-.-': 'K',
                                '.-..': 'L', '--': 'M', '-.': 'N',
                                '---': 'O', '.--.': 'P', '--.-': 'Q',
                                '.-.': 'R', '...': 'S', '-': 'T',
                                '..-': 'U', '...-': 'V', '.--': 'W',
                                '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                                '.----':'1', '..---': '2', '...--':'3',
                                '....-':'4', '.....':'5', '-....':'6',
                                 '--...':'7', '---..':'8', '----.':'9',
                                 '-----':'0',  '--..--':',', '.-.-.-':'.',
                                 '..--..':'?', '-..-.':'/',  '-....-':'-',
                                 '-.--.':'(',  '-.--.-':')', '   ': ' ', '':''}





def textToMorse(sentence):
    m = Morse()
    print(sentence)
    cipher = ''
    for letter in sentence:
        cipher += m.text[letter] + ' '
    
    return cipher
#chinguun = .-. ._.

def morseToText(morse):
    m = Morse()
    l = morse.split(' ')
    p=0
    while p<len(l):
        k=0
        if l[p]=='':  
            while k < 3:
                if (p + k < len(l)):
                    if l[p + k] =='':
                        k=k+1
                    else: 
                        break
                else:
                    break      
        if (k == 2):
            l.insert(p,"")
            p=p+2 
        else:
            p+=1

    #print (l)
    cipher=''
    i=0
    while i<len(l):
        k=0
        if l[i]=='':  
            while k < 4:
                if (i + k < len(l)):
                    if l[i + k] =='':
                        k=k+1
                    else: 
                        break
                else:
                    break
        else:
            cipher += m.morse[l[i]]
        if (k == 3):
            cipher+=m.morse['   ']
            i=i+3  
        else:
            i+=1

        # if l[i]=='' and i+3< len(l) and l[i+3]=='':
        #   cipher+=m.morse['   ']
        #   i=i+3
        # else:
        #     cipher += m.morse[l[i]]
        # i+=1
    return cipher
#.-. -_. = chinguun






def test():
    p="...   ---   ..."
    #print(textToMorse(ps))
    print(morseToText(p))
#put test cases in here
    # p=testMorse()
    # for i in range(0,100):
    #     c = ''
    #     for t in range(0,100):
    #        c += p.charactersAvaliable[random.randint(1, 44)]
    #     print(c)
    #     x = morseToText(textToMorse())
    #     assert(c==x)
    # inp = 'help me'.upper()
    # x = textToMorse(inp)
    # print(x)


    pass # for empty methods to pass the function

if __name__ == '__main__':
    test()