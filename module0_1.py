#1st program
print(f'9 ** 0.5 * 5 = {9 ** 0.5 * 5}')

#2nd program
print(f'9.99 > 9.98 and 1000 != 1000.1 = {9.99 > 9.98 and 1000 != 1000.1}')

#3rd program
print(f'2 * 2 + 2 = {2 * 2 + 2}')
print(f'2 * (2 + 2) = {2 * (2 + 2)}')
print(f'2 * 2 + 2 == 2 * (2 + 2): {2 * 2 + 2 == 2 * (2 + 2)}')

#4th program
some_string = '123.456'
some_int = float(some_string)
some_int *= 10
result = int(some_int % 10)
print(f'первое число после точки у цифры 123.456: {result}')