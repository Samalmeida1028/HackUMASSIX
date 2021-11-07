import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw



while(True):
    recieve_= input("Want to Send or Convert Sentence? Y/N: ")
    while recieve_ != Y  or recieve_ !=N:
        recieve_= input("INVAILD INPUT. TRY AGAIN Y/N: ")


    userInput= input("ENTER A SENTENCE TO CONVERT/SEND");
    transformedUserInput= m.TextToOutput(userInput);






    continue_= input("Continue? Y/N: ")
    while continue_ != Y  or continue_ !=N:
        continue_= input("Continue? Y/N: ")
    if continue_ == 'N':
        break