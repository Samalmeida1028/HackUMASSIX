import MorseCodeConverter as m


def checkInput(input):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890(),/?;:"'.upper()
    for char in str:
        if char in input:
            return True
    return False



def textToOutput(input):
    input = input.upper()
    short = 1
    instruction = (short, short*2)
    instruct = []
    space = .5
    if checkInput(input):
        morse = m.textToMorse(input)
    else:
        morse = input
    for char in morse:
        if char !=' ':
            num = ord(char)//ord('.')
            instruct.append(instruction[num-1])
            instruct.append(space)
    print(instruct)


def test():
    textToOutput('The quick brown fox jumps over the lazy dog.')


if __name__ == '__main__':
    test()