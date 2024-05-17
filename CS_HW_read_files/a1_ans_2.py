user_cruncher = int(
    input(
        "Would you like to 1. add, 2. divide, 3. multiply or 4. subtract? Enter 1 to 4 : "
    )
)
first_num = float(input("Enter your first number : "))
second_num = float(input("Enter your second number : "))


if user_cruncher == 1:
    result = first_num + second_num
elif user_cruncher == 2:
    result = first_num / second_num
elif user_cruncher == 3:
    result = first_num * second_num
elif user_cruncher == 4:
    result = first_num - second_num
else:
    print("Invalid Command ")
    exit()

file = open("calculation.txt", "w")
file.write(str(result))
file.close()
