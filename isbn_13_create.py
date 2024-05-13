user_input = input("Gimme twelve digits number : ")

odd_place_nums = []
even_place_nums = []

for index, value in enumerate(user_input, start=1):
    if index % 2 == 0:
        even_place_nums.append(int(value))
        continue
    odd_place_nums.append(int(value))


sum_of_odd_nums = sum(odd_place_nums)
sum_of_even_nums = sum(even_place_nums)

total_sum = sum_of_odd_nums + (3 * sum_of_even_nums)
the_remainder = total_sum % 10
the_final_val = 10 - the_remainder
print("\n")
print(f"Your ISBN-13 number should be {user_input + str(the_final_val)}")
