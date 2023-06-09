# Пользователь вводит с клавиатуры i, s и n, программа должна рассчитать размер ежемесячной
# выплаты по формуле, а также найти, сколько пользователь всего заплатит банку и сколько
# составит переплата. Сделать ввод/вывод данных.
# m – ежемесячная выплата
# i – годовая процентная ставка
# p – месячная процентная ставка
# s – сумма займа
# n – количество месяцев, на которые взят кредит
# m = (s * p * (pow(1 +p), n))/ ((pow(1 + p), n) -1)

import math
i_str = input("Введите годовую процентную ставку: ")
i = float(i_str)
s_str = input("Введите сумму займа: ")
s = float(s_str)
n_str = input("Введите количество месяцев: ")
n = int(n_str)

p = i / (12 * 100)  # мес. процентная ставка
m = (s * p * (pow(1 + p, n))) / ((pow(1 + p, n)) - 1)  # ежемесячная выплата
total_payment = m * n  # общая сумма
overpayment = total_payment - s  # переплата

print("----------------------------------------------------------------------")
print(f"Ежемесячный платеж: {m:.2f}")
print(f"Общая сумма выплат: {total_payment:.2f}")
print(f"Переплата: {overpayment:.2f}")
print("----------------------------------------------------------------------")