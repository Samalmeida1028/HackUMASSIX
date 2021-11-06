# path is CSV/file
import csv

# file = open('CSV/input.csv', 'w+', newline='') -> create new file
# 'r' for reading 'w' for writing
# arr = file.readlines() creates an array of lines
# arr.split('|') -> splits by specified delimiter. make sure when you write data you separate values by delimiter


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
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
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
                                 '-----':'0',  '--..--':', ', '.-.-.-':'.',
                                 '..--..':'?', '-..-.':'/',  '-....-':'-',
                                 '-.--.':'(',  '-.--.-':')', '   ': ' ', '':''}





def textToMorse(sentence):
    m = Morse()
    cipher = ''
    for letter in sentence:
        cipher += m.text[letter] + ' '
    return cipher
#chinguun = .-. ._.

def morseToText(morse):
    m = Morse()
    l = morse.split(' ')

    print (l)
    cipher=''
    #for letter in sentence:
        #cipher += m.morse[letter] + ' '
    i=0
    while i<len(l):
        if l[i]=='' and i+3< len(l) and l[i+3]=='':
          cipher+=m.morse['   ']
          i=i+3
        else:
            cipher += m.morse[l[i]]
        i+=1
    return cipher
#.-. -_. = chinguun






def test():
#put test cases in here
    moresad = textToMorse("qwertyuiopsdfghjklzcvbnm1234567890".upper())
   # print(moresad)
    print(morseToText(moresad))


    pass # for empty methods to pass the function

if __name__ == '__main__':
    test()