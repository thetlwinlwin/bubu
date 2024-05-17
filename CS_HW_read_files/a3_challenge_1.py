file = open("numbers.txt", "r")

num_list = []

for line in file:
    # this will magically remove '\n' and transform str to int
    num = int(line)
    num_list.append(num)

print(f"The total sum of the number is : {sum(num_list)}")

file.close()
