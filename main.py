import math
# calc na fuctions
# you ready?
print("1 - Сложение")
print("2 - Умножение")
print("3 - Деление")
print("4 - Вычетание")
print("5 - Квадратное уравнение")
number = int(input())
a = int(input("1 число: "))
b = int(input("2 число: "))
# Сложение
if number == 1:
    def sum(a, b):
       result = a + b
       return result
    print(sum(a, b))

# Вычитание
if number == 4:
    def subtract(a, b):
        result = a - b
        return result
    print(subtract(a, b))

# Умножение
if number == 2:
    def multiply(a, b):
        result = a * b
        return result
    print(multiply(a, b))

# Деление
if number == 3:
    def divide(a, b):
        result = a / b
        return result
    print(divide(a, b))

# Кв уравнение
if number == 5:
    c = int(input("3 число: "))
    print("Дискрименант равен: ")
    def discrimenant(a, b, c):
        result = b ** 2 - 4 * a * c
        return result
    print(discrimenant(a, b, c))
    if discrimenant(a, b, c) > 0:
        def x12(x1, x2):
            x1 = -b + math.sqrt(discrimenant(a, b, c)) / 2 * a
            x2 = -b - math.sqrt(discrimenant(a, b, c)) / 2 * a
        print("x1, x2 равно: ", x12())
    elif discrimenant(a, b, c) == 0:
        def dis0(result):
            result = -b / 2 * a
            print("дисрименант равен 0 , поэтому ответ: ", dis0(result))
    else:
        print("корней нет")
