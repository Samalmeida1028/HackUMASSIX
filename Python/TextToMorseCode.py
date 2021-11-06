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
                                '1': '.----', '2': '..---', '3': '...--',
                                '4': '....-', '5': '.....', '6': '-....',
                                '7': '--...', '8': '---..', '9': '----.',
                                '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                '?': '..--..', '/': '-..-.', '-': '-....-',
                                '(': '-.--.', ')': '-.--.-', '   ': ' '}



def Text_to_Morsecode(sentence):
    m = Morse()
    cipher=''
    if sentence[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM ':
        for letter in sentence:
            cipher += m.text[letter]+' '
        return cipher
    else:
        l = []
        i,count,t = 0,0,0
        while i < len(sentence):
            for j in range(i+1,len(sentence)):
                if sentence[j:j+1] == ' ':
                    if sentence[j:j+3] == '   ':
                        l.append(sentence[i:j])
                        t +=1
                        if l[t-1] == '':
                            t -= 1
                            l.pop(t)
                            if l[t - 1] != '   ':
                                t+=1
                                l.insert(t,'   ')
                        i=j+3
                    else:
                        l.append(sentence[i:j])
                        if l[t - 1] == '':
                            t -= 1
                            l.pop(t)
                            t+=1
                        i = j+1
                elif j == len(sentence)-1:
                    l.append(sentence[i:j])
                    i=j
            i+=1
        return l







def test():
#put test cases in here
    text = Text_to_Morsecode("HI MY NAME IS CHUNGUS")
    print(text)
    print(Text_to_Morsecode(text))


    pass # for empty methods to pass the function

if __name__ == '__main__':
    test()