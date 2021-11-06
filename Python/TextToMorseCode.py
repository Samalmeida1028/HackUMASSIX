# path is CSV/file
import csv
import numpy as np

# file = open('CSV/input.csv', 'w+', newline='') -> create new file
# 'r' for reading 'w' for writing
# arr = file.readlines() creates an array of lines
# arr.split('|') -> splits by specified delimiter. make sure when you write data you separate values by delimiter


class Morse():

    def __init__(self):
        self.MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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

        self.MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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
                                '(': '-.--.', ')': '-.--.-', ' ': '   '}



def Text_to_Morsecode(sentence):
    m = Morse()
    cipher=''
    for letter in sentence:
        if letter != ' ':

            cipher += m.MORSE_CODE_DICT[letter]+ ' '
        else:

            cipher += ' '

    return cipher





def test():
#put test cases in here
    print(Text_to_Morsecode("HI MY NAME IS CHUNGUS"))


    pass # for empty methods to pass the function

if __name__ == '__main__':
    test()