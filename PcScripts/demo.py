import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw



userInput= input("ENTER A SENTENCE TO CONVERT/SEND");
transformedUserInput= m.TextToOutput(userInput);






continue_= input("Continue? Y/N: ")
while continue_ != Y  or continue_ !=N:
    continue_= input("Continue? Y/N: ")
    if continue_ == 'N':
        break
