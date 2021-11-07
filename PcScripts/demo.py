import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw

while(True):
    recieve_= input("Rather recieve morse code than send? Y/N: ")
    while recieve_ != Y  or recieve_ !=N:
        recieve_= input("INVAILD INPUT. TRY AGAIN Y/N: ")

    if(recieve_=='Y'):
        print('hi')

    else:
        keyboardOrSensor=input("Want to type sentence rather than use morse code? Y/N: "):
        while keyboardOrSensor!= Y  or keyboardOrSensor !=N:
            keyboardOrSensor= input("INVAILD INPUT. TRY AGAIN Y/N: ")
        if(keyboardOrSensor=='N'):
            userInput= input("ENTER A SENTENCE TO CONVERT/SEND");
            transformedUserInput= m.TextToOutput(userInput);

        else:    
            print("Morse Code!")


    continue_= input("Continue? Y/N: ")
    while continue_ != Y  or continue_ !=N:
        continue_= input("Continue? Y/N: ")
    if continue_ == 'N':
        break


