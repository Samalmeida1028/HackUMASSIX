import MorseCodeConverter as m


def checkInput(input):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890(),/?;:"'.upper()
    for char in str:
        if char in input:
            return True
    return False



def textToOutput(input):
    #takes in string of words or morse code
    input = input.upper()
    #Represent duration
    short = 1
    #Represent duration of a short and long
    instruction = (short, short*2)
    #Used to store the outpu aka structions to convert it to light
    instruct = []
    #Current duration between spaces of words
    space = .5
    #Checks if the input is a string and converts it morse code
    if checkInput(input):
        morse = m.textToMorse(input)
    #If it is morse code
    else:
        morse = input
    #morse to text
    for char in morse:
        if char !=' ':
            num = ord(char)//ord('.')+1
            instruct.append(instruction[num])
            instruct.append(space)
    print(instruct)


def test():
    textToOutput('The quick brown fox jumps over the lazy dog.')


if __name__ == '__main__':
    test()