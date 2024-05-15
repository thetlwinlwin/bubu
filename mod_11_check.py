user_input = input("Enter number to check mod 11 : ")

if len(user_input) > 10:
    print("Invalid Modulo 11")
    exit()

wt_start = len(user_input)
total = []

for val in user_input:
    weighted_val = int(val) * wt_start

    wt_start -= 1

    total.append(weighted_val)


total_sum = sum(total)

remainder = total_sum % 11
if remainder == 0:
    print("Valid Modulo 11 number")
else:
    print("Invalid Modulo 11 number")
