numbers_list = []
for i in range(10):
    number = int(input("Enter number: "))
    numbers_list.append(number)
print("Numbers without duplicate:")
for number in numbers_list:
    if numbers_list.count(number) == 1:
        print(number)
