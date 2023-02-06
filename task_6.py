# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *3

summa_xy = int(input("Сумма чисел X + Y = "))
multiplication_xy = int(input("Произведение чисел X*Y = "))
first_number_x = 0
second_number_y = 0
while first_number_x < 1000:
    first_number_x +=1
    second_number_y = first_number_x
    while second_number_y < 1000:
        second_number_y +=1
        if first_number_x + second_number_y ==summa_xy and first_number_x*second_number_y == multiplication_xy:
            print(first_number_x, second_number_y)
