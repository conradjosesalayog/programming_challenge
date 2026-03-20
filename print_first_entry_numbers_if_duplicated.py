numbers = []
not_duplicated_numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))

for num in numbers:
    if numbers.count(num) == 1:
       not_duplicated_numbers.append(num)
print("Not duplicated:", not_duplicated_numbers)