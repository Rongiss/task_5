import random

def main():
    stat_game = 'да'
    while stat_game == 'да':
        comp = comp_generate()
        user = user_change()
        the_geme(user, comp)
        print('Введите "да" что бы еще раз сыграть')
        stat_game = input()

def comp_generate():
    num = random.randint(1, 3)

    if num == 1:
        result = 'Камень'
    elif num == 2:
        result = 'Ножницы'
    elif num == 3:
        result = 'Бумага'
    return result

def user_change():
    print('\nВведите один из трех вариантов')
    print("Камень, Ножницы, Бумага")
    print('Ваш выбор - ', end='')
    user = input()

    return user

def the_geme(user, comp):

    print('\nКомпьютер случайно выбрал -', comp)
    # Сочетание Бумага Камень
    if user == 'Бумага' and comp == 'Камень':
        print('Вы выиграли!')
    elif user == 'Камень' and comp == 'Бумага':
        print('Выиграл компьютер')
    # Сочетание Бумага Ножницы
    elif user == 'Ножницы' and comp == 'Бумага':
        print('Вы выиграли!')
    elif user == 'Бумага' and comp == 'Ножницы':
        print('Выиграл компьютер')
    # Сочетание Камень Ножницы
    elif user == 'Камень' and comp == 'Ножницы':
        print('Вы выиграли!')
    elif user == 'Ножницы' and comp == 'Камень':
        print('Выиграл компьютер')
    elif user == comp:
        print('Ничья')
main()