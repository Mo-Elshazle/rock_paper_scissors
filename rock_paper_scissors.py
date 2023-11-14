import random

def play_game():

    print("welcome to rock paper scissors game ")

    user = input ("choose 'r' for rock 'p' for paper 's' for scissors \n")
    pc = random.choice(['r' , 'p', 's' ])

    print( "your choice is : " + user )
    print("pc choice is : " + pc)

    if (user == pc) :
        print ("it`s a tie ")
    elif (user == "r" and pc == "s") or (user == "s" and pc == "p") or (user == "p" and pc == "r") :
        print("You win ! ")
    else :
        print ("You lose! ")    

while True:
    play_game()

    play_again = input("Do you want to play again? (yes/no)\n").lower()
    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break






























