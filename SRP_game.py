#start the game
# ask the player to make a move (r, p, s) rock paper or scissor
#PC will select a random move 
#pc == player -> tie 
#pc == rock and player == paper -> player wins
#user won = you won
#any other case
#user lost = you lost or PC won = you lose

import random

user = input("what is your choice ?") # get the user input r=rock, p=paper, s=scissors
pc = random.choice(['r', 'p', 's'])

print(f"pc chose {pc}") # print the pc choice
print('user played:' + user) 

if user==pc:
    print("tie")
elif (user=='p' and pc=='r') or (user=='s' and pc=='p') or (user=='r' and pc=='s'):
    print("you won")
else:
    print("you lose")

