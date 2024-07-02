def check_number(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

# Test the function
check_number(5)   # 5 is positive
check_number(-3)  # -3 is negative
check_number(0)   # 0 is zero
