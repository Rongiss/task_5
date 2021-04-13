import intro_task_5_2
import input_task_5_2
import calkulate_and_out_task_5_2

FEDERATION_TAX = 5
REGIONAL_TAX = 2.5

def main():
    intro_task_5_2.info(FEDERATION_TAX, REGIONAL_TAX)
    money_from_user = input_task_5_2.enter_cash()
    calkulate_and_out_task_5_2.calcalculete_and_out(FEDERATION_TAX, REGIONAL_TAX, money_from_user)
    intro_task_5_2.out_list()

main()