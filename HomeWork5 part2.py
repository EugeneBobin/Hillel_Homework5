number = int(input("enter the number :"))
if number != 0:
    while number > 9:
        digit = [int(x) for x in str(number)]
        result = 1
        for number in digit:
            result *= number
        number = result
    print(result)
else:print("number can`t be zero")
