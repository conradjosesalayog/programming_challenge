first_number = int(input("Enter number 1: "))
result = first_number
for i in range(2, 11):
    num = int(input(f"Enter number {i}: "))
    result -= num
print("Result:", result)
