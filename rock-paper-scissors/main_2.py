import random
characters_=['R','P','S']
wins=[['R','S'],['P','R'],['S','P']]

def game():
    """
    This function is a game between the computer and a user.
    The valid options to make a choice from are:
    
    characters_=['R','P','S']

    where:

    "R" for "rock", 
    "P" for "paper", 
    "S" for "scissors"

    If user input is invalid (not amongst our options), we print an error, and ask for their input again.
    If there is a winner, we print the winner, and the program ends. 
    If it's a tie (the computer and player pick the same move), restart the game.

    computer=CPU
    human=user
    """
    while True:
        computer=(random.choice(characters_)).upper() 
        print(f"The computer has played: {computer}")
        human=(input("Please, choose R, P or S: \n ", )).upper()
        print(f'Player: {human}, CPU: {computer}')

        if human not in characters_:
            print("Please, input a valid option: ")

        elif human==computer:
            print("\n This is a tie \n")

        else:
            for configuarations in wins:
                if configuarations[0][0]==human and configuarations[1][0]==computer: #we check if the human has won
                    print('\n You win \n ')
                    return 
            
                elif configuarations[1][0]==human and configuarations[0][0]==computer: #we check if the computer has won
                    print('\n The computer has won \n')
                    return 

       
if __name__==game():
    game()