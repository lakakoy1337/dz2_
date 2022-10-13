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
    c = int(input("Введите c: "))

    def discriminant(a,b,c):
        d = int((b ** 2) - 4 * a * c)  # дискриминат
        return d
    if discriminant(a,b,c) < 0:
        print("корней нет")
    else:
        if discriminant(a,b,c) == 0:
            x1 = -b / 2 * a
            print("x = " + str(x1))
        else:
            x1 = ((-b) + (discriminant(a,b,c) ** 0.5)) / 2 * a
            x2 = ((-b) - (discriminant(a,b,c) ** 0.5)) / 2 * a
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
