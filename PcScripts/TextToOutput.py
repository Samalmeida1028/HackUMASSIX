import MorseCodeConverter as m
import serial

def checkInput(input):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890(),/?;:"'.upper()
    for char in str:
        if char in input:
            return True
    return False


def textToOutput(input):
    input = input.upper()
    dit = 2
    dah = dit*3
    interval = (dah, dit)
    instructions = []
    temp = ''
    
    if checkInput(input):
        morse = m.textToMorse(input)
    else:
        morse = input

    for i in range(len(morse)-1):
        if morse[i] != ' ':
            num = ord(morse[i])//((ord('-'))+1)
            instructions.append((interval[num],1))
            instructions.append((1, 0))
        elif morse[i+1] == ' ':
            space = dit
            instructions.append((space,0))
        else:
            space = dah
            instructions.append((space, 0))

    for i in instructions:
        temp += str(i[0] + i[1])
    instructions = temp
    return instructions


def test():
    print(textToOutput('The quick brown fox jumps over the lazy dog.'))





if __name__ == '__main__':
    test()