file = open("quick.txt", "r")
for line in file:
    # line = "A\n"
    print(line.strip())
    # after strip => line = "A"
    # but print function gives "\n"
    # the result is "A\n"
file.close()
