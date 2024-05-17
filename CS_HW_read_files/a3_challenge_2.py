script_1 = open("transcript1.txt", "r")
script_2 = open("transcript2.txt", "r")


for line in script_1:
    print(line.strip())
    print(script_2.readline())


script_1.close()
script_2.close()
