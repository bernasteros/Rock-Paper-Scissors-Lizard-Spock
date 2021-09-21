import random
from os import system
from time import sleep

rock = '''"Rock"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''"Paper"
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''"Scissors"
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
spock = ''' "Spock"
                      _    
                     | |   
 ___ _ __   ___   ___| | __
/ __| '_ \ / _ \ / __| |/ /
\__ \ |_) | (_) | (__|   < 
|___/ .__/ \___/ \___|_|\_\
    | |                    
    |_|      
'''

lizard = ''' "Lizard"
              )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( / 
  `\.-''__.-' \ (     \_      

'''

gesture = [rock, paper, scissors, spock, lizard]
rock_win = [scissors, lizard]
paper_win = [spock, paper]
scissors_win = [lizard, paper]
spock_win = [rock, scissors]
lizard_win = [paper, spock]
player_score = 0
computer_score = 0
game = "y"

gesture = [[rock, rock_win], [paper, paper_win], [scissors, scissors_win],
           [spock, spock_win], [lizard, lizard_win]]

print("Welcome to Rock Paper Scissors Lizard Spock")

while (game == "y"):

    computer = random.randint(0, 4)
    player = int(
        input('''Please make your Choice:
  0 = rock
  1 = paper
  2 = scissors
  3 = spock
  4 = lizard

  >>>'''))
    if player >= 0 and player <= 4:
        print(f''' You play 
    {gesture[player][0]}''')

        print(f''' 
    Computer plays 
    {gesture[computer][0]}''')
        sleep(1)
        if gesture[player][0] == gesture[computer][0]:
            print("It is a draw!\n")
        elif gesture[computer][0] in gesture[player][1]:
            print("Player wins!\n")
            player_score = player_score + 1
        else:
            print("Computer wins!\n")
            computer_score = computer_score + 1
    else:
        print("Non existing Choice, Computer wins by default!\n")
        computer_score = computer_score + 1
    sleep(1)
    game = input(
        "Another round?\n 'y' for continue, any other key for quitting\n Answer: ")
    system('clear')
print(
    f"Thank you for playing :)\n Endscore:\n Player Score = {player_score} Points\n Computer Score = {computer_score}"
)
