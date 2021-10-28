# rock,paper,scissor
while True:
    choice = input("Do wanna play a game of Rock-paper-scissor? y/n \n")
    if choice == 'y':
        player_one = input("Player1 enter rock, paper,scissors: ")
        player_two = input("Player2 enter rock, paper,scissors: ")
        if (player_one == player_two):
            print("It's a tie!")

        elif player_one == "rock":
            if player_two == "scissors":
                print("Player_one wins! congratulations")
            else:
                print("Player_two wins! congratulations")

        elif player_one == "paper":
            if player_two == "rock":
                print("Player_two wins!congratulations")
            else:
                print("Player_one wins! congratulations")

        elif player_one == "scissors":
            if player_two == "paper":
                print("Player_one wins! congratulations")
            else:
                print("player_two wins! congratulations")
    else:
                print("thank you for playing!!")
                break







