import random

def main():
    var = 'yes'
    while var == 'yes':
        numb = generate_number()
        var = int(input('введите ваше чило - '))
        while var != numb:
            if var > numb:
                print('Число меньше')
            else:
                print('Число больше')
            print('Попробуйте еще раз ')
            var = int(input('введите ваше чило - '))
        print("Вы агадали!")
        var = input('Введите "yes" для продолжения игры - ')
def generate_number():
    number = random.randint(1, 101)
    return number

main()