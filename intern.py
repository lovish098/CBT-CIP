import random



game=['rock','paper','scissor']

predict = random.choice(game)

def winner(player,predict):
    if player == predict:
        print("game is tie")
    elif player == "rock" and predict == "scissor" or player =="paper" and predict == "rock" or player == "scissor" and predict == "paper" :
        print("you win the game")
    else:
        print("you loose the game")



print("Welcome to the game of Rock, Paper, Scissor")

player = input("press R for rock , press P for paper, press S for scissor \n").upper()

if player == "R":
    player = "rock"
    print("You Chooses Rock")
    print(f"computer chooses {predict}")

elif player == "P":
    player = "paper"
    print("You Chooses Paper")
    print(f"computer chooses {predict}")

elif player == "S":
     player = "scissor"
     print("You Chooses Scissor")
     print(f"computer chooses {predict}")

else :
    print("Choose the alphabet that are given")
    exit()


winner(player,predict)