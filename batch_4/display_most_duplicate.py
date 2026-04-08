numbers = []

while True:
    try:
        num = int(input("Enter number: "))
        numbers.append(num)
    except:
        break

most_duplicate = None
highest_count = 0

for num in numbers:
    count = numbers.count(num)
    if count > highest_count:
        highest_count = count
        most_duplicate = num

print("Number with most duplicates:", most_duplicate)
