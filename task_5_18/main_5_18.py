
def main():
    for num in range(1, 101):

        if fett_result(num):
            print(' Число {} - простое '.format(num) )



def fett_result(number):
    # ПРисвоение первичного значения True для ветвления
    result = True
    # Ветвление для определения результата
    if number % 2 == 0 or number % 3 == 0:
        result = False
    # Возвращаемое значение True or False
    return result
main()