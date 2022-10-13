import math

print("1 - Сложение")
print("2 - Умножение")
print("3 - Деление")
print("4 - Вычетание")
print("5 - Квадратное уравнение")
spisok = []
number = int(input())
spisok = number
if spisok == 1:
    def sum(a, b):
        result = a + b
        return result


    print("Результат сложения:", sum(a, b))

if spisok == 2:
    def minus(a, b):
        result = a - b
        return result


    print("Результат вычитания:", sum(a, b))

if spisok == 3:
    def prois(a, b):
        result = a * b
        return result


    print("Результат умножения:", sum(a, b))

if spisok == 4:
    def dell(a, b):
        result = a / b
        return result


    print("Результат деления:", sum(a, b))

if spisok == 5:
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
