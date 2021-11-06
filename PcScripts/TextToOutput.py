import MorseCodeConverter as m


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
    instruction = (short, long)
    #represents the final output instructions for light
    instruct = []
    #Re
    space = 1
    if checkInput(input):
        morse = m.textToMorse(input)
    else:
        morse = input
    print(morse)
    for char in morse:
        if char !=' ':
            num = ord(char)//(ord('.'))
            instruct.append((instruction[num-1],1))
            instruct.append((space,0))
        else:
            instruct.append((long,0))
    return instruct


def test():
    print(textToOutput('The quick brown fox jumps over the lazy dog.'))


if __name__ == '__main__':
    test()