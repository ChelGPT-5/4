import math

print("Используя модуль math, вычислите значения по следующим формулам:")
print("a) y = (pow(a, 2)/3) + (pow(2, a)+4/b) + ((math.sqrt(a ** 2 + 4)) / 4) + (math.sqrt(pow(pow(a, 2 + 4), 3)) / 4)")
a_str = input("Введите значение a: ")
a = float(a_str)

b_str = input("Введите значение b: ")
b = float(b_str)

y = (pow(a, 2) / 3) + (pow(2, a) + 4 / b) + ((math.sqrt(a ** 2 + 4)) / 4) + (math.sqrt(pow(pow(a, 2 + 4), 3)) / 4)
print(f"|при a = {a} и b = {b} y = {y:.3f}|")
print("----------------------------------------------------------------------")

print("b) y = cos(x) + sin(x)")
x_str = input("Введите значение x: ")
x = float(x_str)

y = math.cos(x) + math.sin(x)
print(f"|при x = {x} y = {y:.3f}|")
print("----------------------------------------------------------------------")

print("c) y = 3 ** (math.sqrt((pow(math.cos(x ** 2), 2) + pow(math.sin(2 * x - 1), 2))))")
x_str = input("Введите значение x: ")
x = float(x_str)

y = 3 ** (math.sqrt((pow(math.cos(x ** 2), 2) + pow(math.sin(2 * x - 1), 2))))
print(f"|при x = {x} y = {y:.3f}|")
print("----------------------------------------------------------------------")

print("d) y = (5 * x) + 3 * pow(x, 2) * (math.sqrt(1 + pow(math.sin, 2)(x)))")
x_str = input("Введите значение x: ")
x = float(x_str)

y = (5 * x) + 3 * pow(x, 2) * (math.sqrt(1 + pow(math.sin(x), 2)))
print(f"|при x = {x} y = {y:.3f}|")
print("----------------------------------------------------------------------")
