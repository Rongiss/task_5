CONST_FED_TAX = 0.05
CONST_REG_TAX = 0.025

print('Введите доход за месяц - ', end='')
dohod = float(input())

tax_reg = dohod * CONST_REG_TAX
tax_fed = dohod * CONST_FED_TAX
total = tax_fed + tax_reg

print('\nРегиональный налог равен -', format(tax_reg, '.2f'), sep=' ')
print('Федеральный налог равен -', format(tax_fed, '.2f'), sep=' ')
print('Суимарный налог составляет - ', format(total, '.2f'), sep=' ')