import MorseCodeConverter as m


def checkInput(input):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890(),/?;:"'.uppercase
    for char in str:
        if char in input:
            return True
    return false



def textToOutput(input):
    short = 1
    instruction = (short, short*2)
    instruct = []
    space = .5
    if checkInput(input):
        morse = m.textToMorse(input)
    else:
        morse = input
    for char in morse:
        num = int(char)//int('.')
        instruct.append(instruction[num])
    print(instruct)


def test():
    


if __name__ == '__main__':
    test()