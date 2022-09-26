import math

print("1 - Сложение")
print("2 - Умножение")
print("3 - Деление")
print("4 - Вычетание")
print("5 - Квадратное уравнение")

number = int(input())

if number == 1:

    print("Введите первое число")
    number1 = int(input())
    print("Введите второе число")
    number2 = int(input())
    result = number1 + number2
    print(result)

if number == 2:

    print("Введите первое число")
    number1 = int(input())
    print("Введите второе число")
    number2 = int(input())
    result = number1 * number2
    print(result)

if number == 3:

    print("Введите первое число")
    number1 = int(input())
    print("Введите второе число")
    number2 = int(input())
    result = number1 / number2
    print(result)

if number == 4:

    print("Введите первое число")
    number1 = int(input())
    print("Введите второе число")
    number2 = int(input())
    result = number1 - number2
    print(result)

if number == 5:

    print("a*x**2+bx+c=0")

print("Введите a")
a = int(input())
print("Введите b")
b = int(input())
print("Введите c")
c = int(input())
print("Дискрименант равен")
D = b ** 2 - 4 * a * c
print(D)

print("Ответ")
if D > 0:
    x1 = -b + math.sqrt(D) / 2 * a
    x2 = -b - math.sqrt(D) / 2 * a
    print(x1, x2)
elif D == 0:
    x1 = -b / 2 * a
    print(x1)
else:
    print("корней нет")