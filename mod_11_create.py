user_input = input("enter the number : ")

while len(user_input) > 9:
    print("maximum number should not exceed 9 characters")
    user_input = input("enter the number : ")

wt_start = len(user_input) + 1
total = 0

for val in user_input:
    weighted_val = wt_start * int(val)

    # wt_start = wt_start - 1
    # at the beginnning, wt_start is 7, then 7 - 1 = 6 and that 6 is assigned again to the variable named "wt_start"
    wt_start -= 1

    # total = total + result
    total += weighted_val


remainder = total % 11

result = 11 - remainder

check_digit = result

if result == 10:
    check_digit = "X"
if result == 11:
    check_digit = 0


x = user_input + str(check_digit)
print(f"the result is {x}")
