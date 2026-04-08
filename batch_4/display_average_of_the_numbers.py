numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

average = sum(numbers)/len(numbers)
print("The average is: ", average)
