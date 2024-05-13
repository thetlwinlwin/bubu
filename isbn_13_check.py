# input should be 5372406186219

isbn = input("Gimme your ISBN-13 : ")

odd_place_nums = []
even_place_nums = []

for index, val in enumerate(isbn, start=1):
    if index % 2 == 0:
        even_place_nums.append(int(val))
        continue
    odd_place_nums.append(int(val))

sum_odd_nums = sum(odd_place_nums)
sum_even_nums = sum(even_place_nums)
total_sum = sum_odd_nums + (3 * sum_even_nums)
remainder = total_sum % 10

if remainder == 0:
    print("Valid ISBN")
else:
    print("ERROR. BLAME YOUR Student")
