import random

def main_5_11():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    print(num1)
    print('+', num2, sep=' ')
    result(num1 + num2)

def result(summ):
    res_user = float(input('Введите ваш ответ -'))
    if summ == res_user:
        print('\nВы правильно ответили')
        print("Поздравляю")
    else:
        print("\nВы ошиблись")
        print("Праильный ответ -", summ, sep=" ")

main_5_11()