import string
user_input = input("Введите две буквы через дефис (например, a-c): ")
start, end = user_input.split('-')
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)

if start_index <= end_index:
    print(letters[start_index:end_index + 1])
else:
    print(letters[start_index:] + letters[:end_index + 1])

