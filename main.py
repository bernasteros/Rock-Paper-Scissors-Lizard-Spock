from elements import rock, paper, scissors, spock, lizard, logo
import random
from os import system, name
from time import sleep


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


element_word = {
    rock: "rock",
    paper: "paper",
    scissors: "scissors",
    spock: "spock",
    lizard: "lizard",
}

rock_win = [scissors, lizard]
paper_win = [spock, rock]
scissors_win = [lizard, paper]
spock_win = [rock, scissors]
lizard_win = [paper, spock]
player_score = 0
computer_score = 0

element_win = [[rock, ["breaks", "crushes"]], [paper, ["disproves", "covers"]],
               [scissors, ["slices",
                           "cuts"]], [spock, ["vaporises", "crushes"]],
               [lizard, ["eats", "poisons"]]]

gesture = [
    [rock, rock_win],
    [paper, paper_win],
    [scissors, scissors_win],
    [spock, spock_win],
    [lizard, lizard_win],
]

game = "y"

print(logo)
print("Welcome to Rock Paper Scissors Lizard Spock")

while (game == "y"):

    computer = random.randint(0, 4)
    player = int(
        input('''Please make your Choice:
  0 = rock 🪨
  1 = paper 📜
  2 = scissors ✂️
  3 = spock 🖖
  4 = lizard 🐉

  Your choice: '''))
    clear()

    # Simplifying addressing position of choices and winning conditions
    player_hand = gesture[player][0]
    computer_hand = gesture[computer][0]
    c_loser_list = gesture[player][1]
    p_loser_list = gesture[computer][1]


    if player >= 0 and player <= 4:
        print(f''' You play 
    {gesture[player][0]}''')
        sleep(1)
        print(f''' 
    Computer plays 
    {gesture[computer][0]}''')
        sleep(1)
        if player_hand == computer_hand:
            print("It is a draw!\n")
        elif computer_hand in c_loser_list:
            defeats = element_win[player][1][c_loser_list.index(computer_hand)]

            print(
                f"'{element_word[player_hand]} {defeats} {element_word[computer_hand]}'"
            )

            print("\nPlayer wins!\n")

            player_score += 1

        else:
            defeats = element_win[computer][1][p_loser_list.index(player_hand)]

            print(
                f"'{element_word[computer_hand]} {defeats} {element_word[player_hand]}'"
            )

            print("\nComputer wins!\n")
            computer_score += 1
    else:
        print("Non existing Choice, Computer wins by default!\n")
        computer_score += 1
    sleep(1)
    game = input(
        "Another round?\n 'y' for continue, any other key for quitting\n Answer: "
    )
    clear()
print(
    f"Thank you for playing :)\n Endscore:\n Player Score = {player_score} \n Computer Score = {computer_score}"
)
