#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает 
# Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна 
# их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их 
# произведение P. Помогите Кате отгадать задуманные Петей числа.

summa = int(input(f"Введите сумму чисел S = "))
mult = int(input(f"Введите произведение чисел P = "))
flag_break = False

for x in range(summa):
    if(flag_break == False):
        for y in range(summa):
            if (x + y == summa) and (x * y == mult):
                print("загаданные числа:")
                print(x, y)
                flag_break = True
                break
            elif (x == summa -1) and (y == summa -1):
                print("нет соответствующих чисел")