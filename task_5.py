# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
from random import randint

n_coins = int(input("Введите число монеток: "))
eagle = 0
tails = 0
for _ in range(1, n_coins + 1):
    variants = randint(0, 1)
    while eagle <= variants:
        eagle = +1
    else:
        tails =+ 1
if eagle < tails:
    print(eagle)
else:
    print(tails)
