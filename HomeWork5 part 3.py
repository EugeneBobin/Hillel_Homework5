numbers = input("Введите числа через пробел :")
numbers = numbers.split(" ")
x = 0
i = 1
for i in range(len(numbers)):
    i += 1
    if "0" in numbers:
        numbers.remove("0")
        x += 1
    else:continue
for el in range(x):
    numbers.append("0")
print(numbers)
