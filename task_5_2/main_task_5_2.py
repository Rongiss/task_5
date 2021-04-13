import intro_task_5_2
import input_task_5_2
import calkulate_and_out_task_5_2

# Константы налоговых ставок
FEDERATION_TAX = 5
REGIONAL_TAX = 2.5

# Основная функция
def main():
    # Вызов информационной функции с параметрами
    # Налоговых ставок
    intro_task_5_2.info(FEDERATION_TAX, REGIONAL_TAX)

    # Функция ввода данных
    money_from_user = input_task_5_2.enter_cash()

    # Функция расчета суму
    calkulate_and_out_task_5_2.calcalculete_and_out(FEDERATION_TAX, REGIONAL_TAX, money_from_user)

    # Функция для вывода завершающего сообщения
    intro_task_5_2.out_list()

# Вызов основной функции
main()