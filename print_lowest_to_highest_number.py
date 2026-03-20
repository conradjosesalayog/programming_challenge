numbers = []

while True:
    user_input = input("Enter number: ")

    if user_input.replace('.', '', 1).isdigit():
        number_value = float(user_input)
        numbers.append(number_value)
