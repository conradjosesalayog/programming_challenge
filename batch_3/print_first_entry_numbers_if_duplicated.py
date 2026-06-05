number_list = []
for i in range(10):
    num = int(input("Enter a number:"))
    if num not in number_list:
        number_list.append(num)
print(number_list)
