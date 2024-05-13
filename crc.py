def binary_string(input_str):
    """
    Convert a string to binary
    """
    return " ".join(format(ord(x), "08b") for x in input_str)


def convert_d_to_b(input_d, input_str):
    """
    Convert decimal value to binary
    """
    length = len(input_str) + 2
    return format(input_d, f"0{length*8}b")


def show(input_str):
    print("Char\tDenary Val\tBinary Val")
    for i in input_str:
        print("-" * 50)
        print(f"{i}\t{ord(i)}\t\t{format(ord(i), '08b')}")


def total_denary(input_b_str):
    return int("".join(input_b_str.split(" ")), 2)


if __name__ == "__main__":
    print("\n")
    input_str = input("ENTER THE STRING TO BE CHECKED: ")
    b_str = binary_string(input_str)
    print("\n")
    show(input_str)
    print("\n")
    print("NOW THE BINARY IS")
    print(b_str)
    print("THE TOTAL DENARY VALUE IS")
    print(total_denary(b_str))
    print("\n")
    print("ADD 16BITS TO THE END")
    b_str_after_16 = b_str + " " + "0" * 8 + " " + "0" * 8
    denary = total_denary(b_str_after_16)
    print(b_str_after_16)
    print("\n")
    print("AFTER ADDING 16 BITS")
    print("THE DENARY VALUE IS ")
    print(denary)
    print("\n")
    remainder = denary % 65521
    print(f"THE REMAINDER AFTER BEING DIVIDED BY 65521 -> {remainder}")
    print("\n")
    val_after_sub = denary - remainder
    print(f"{denary} - {remainder} = {val_after_sub}")
    print("\n")
    b_str = convert_d_to_b(val_after_sub, input_str)
    print(" ".join(b_str[i : i + 8] for i in range(0, len(b_str), 8)))
