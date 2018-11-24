def introduction():
    print("Welcome to Hangman");
    print("One player will enter a word or phrase");
    print("The other player will try to guess the word or phrase");
    print("You have 6 strikes until the game is over");
    print("NO CAPITAL LETTERS PLEASE");

def StringToArrayConverter(userInput):
    userInputArray = [""] * len(userInput);
    j = 0;
    for i in userInput:
        userInputArray[j] = i;
        j = j + 1;
    return userInputArray;

def StringToDashConverter(userInputArray):
    dashUserInputArray = [""] * len(userInputArray);
    dashUserInput = "";
    i = 0;
    j = 0;
    while(i < len(userInputArray)):
        if(userInputArray[i] == " "):
            dashUserInputArray[i] = " ";
        else:
            dashUserInputArray[i] = "_";
        i = i + 1;
    while(j < len(dashUserInputArray)):
        dashUserInput = dashUserInput + dashUserInputArray[j] + " ";
        j = j + 1;
    return dashUserInput;

def gameOver(userInputAsDashes, strikes):
    if(strikes >= 6):
        print("You lost");
        return True;
    elif(userInputAsDashes.find('_') == -1):
        print("You won");
        return True;
    else:
        return False;

def Checker(guess, userInputArray):
    i = 0;
    while(i < len(userInputArray)):
        if(userInputArray[i] == guess):
            return True;
        i = i + 1;
    return False;
def revealCharacter(guess, userInputArray, userInputAsDashes):
    i = 0;
    userInputAsDashesTempArray = list(userInputAsDashes);
    while(i < len(userInputArray)):
        if(userInputArray[i] == guess):
            if(i == 0):
                userInputAsDashesTempArray[i] = guess;
            else:
                userInputAsDashesTempArray[i + i] = guess;
        i = i + 1;
    userInputAsDashes = "".join(userInputAsDashesTempArray);
    return userInputAsDashes;


def main():
    introduction();
    userInput = input(print("What is the word or phrase?"));
    userInputAsDashes = "";
    userInputArray = [""] * len(userInput);
    userInputArray = StringToArrayConverter(userInput);
    userInputAsDashes = StringToDashConverter(userInputArray);
    strikes = 0;
    while(gameOver(userInputAsDashes, strikes) != True):
        print(userInputAsDashes);
        guess = input(print("What letter do you want to guess?"));
        if(Checker(guess, userInputArray) != True):
            strikes = strikes + 1;
            print("Letter not found! " + str(strikes) + " strike");
            continue;
        else:
            userInputAsDashes = revealCharacter(guess, userInputArray, userInputAsDashes);
            continue;
    print(userInputAsDashes);
main();