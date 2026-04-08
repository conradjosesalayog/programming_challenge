numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break
numbers.sort(reverse=True)
print("Highest to lowest:" , numbers)