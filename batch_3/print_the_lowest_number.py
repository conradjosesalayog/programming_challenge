numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break
print("The lowest number is: ", min(numbers))
