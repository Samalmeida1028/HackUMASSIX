import MorseCodeConverter as m
import serial

def checkInput(input):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890(),/?;:"'.upper()
    for char in str:
        if char in input:
            return True
    return False



def textToOutput(input):
    #takes in string of characters or morse code
    input = input.upper()
    #short represents dit
    short = 2
    #long represents dah
    long = short*3
    #represents the possible options
    instruction = (long, short)
    #represents the final output instructions for light
    instruct = []
    #Reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    if checkInput(input):
        morse = m.textToMorse(input)
    else:
        morse = input
    print(morse)
    for char in morse:
        space = 1
        if char != ' ':
            num = ord(char)//((ord('-'))+1)
            instruct.append((instruction[num],1))
        else:
            space = long
        instruct.append((space,0))
    i = 0
    while i < len(instruct):
        if instruct[i][1] == 0 and instruct[i][0] == long:
            k = 0
            j = 0
            while k < 4:
                if (i + k < len(instruct)):
                    if instruct[i + k][1] == 0 and instruct[i + k][0] == long:
                        k += 1
                    else:
                        break
                else:
                    break
            if (k == 4):
                instruct.pop(i)
                i -= 1
        i += 1
    return instruct


def test():
    print(textToOutput('The quick brown fox jumps over the lazy dog.'))


if __name__ == '__main__':
    test()