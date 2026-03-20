num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

start = min(num_1, num_2)
end = max(num_1, num_2)

for i in range(start + 1, end):
    print(i)