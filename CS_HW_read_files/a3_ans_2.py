file = open("quick.txt", "r")

for line in file:
    #  line = "A\n"
    print(line)
    # print function ends the line with \n again.
    # That's why it becomes "A\n\n"

file.close()
