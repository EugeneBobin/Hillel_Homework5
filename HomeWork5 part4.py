numbers = input("Введите числа через пробел в количестве от 3 до 10 :")
numbers = numbers.split(" ")
result = [numbers[0], numbers[2], numbers[-2]]
print(result)
