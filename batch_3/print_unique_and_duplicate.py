numbers = []
while True:
    number_input = input("enter number: ")

    if not number_input.isdigit():
        break

    num = int(number_input)

    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)
