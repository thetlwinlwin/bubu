file = open("players.txt", "w")

num_of_players = 4

for i in range(num_of_players):
    user_input = input(f"Enter Player {i+1} : ")
    file.write(user_input + "\n")


file.close()
