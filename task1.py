#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

number = float(input('Введите трехзначное число: '))
summ = 0
while number > 0:
    a = number % 10
    summ = summ + a
    number = number//10
print(summ)