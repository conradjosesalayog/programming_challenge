lowest_number = None

while True:
    user_input = input("Enter number: ")

    try:
        number_value = int(user_input)
        if lowest_number is None or number_value < lowest_number:
            lowest_number = number_value
    except:
        break

print("Lowest:", lowest_number)
