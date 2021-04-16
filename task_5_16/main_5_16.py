import random

def main():
    ran()

def ran():
    a = 0
    b = 0
    for i in range(100):
        num = random.randint(1, 1000000)
        print(num)
        if num % 2 == 0:
            a += 1
        else:
            b += 1
    print('Количество четных ', a)
    print('Количество не четных ', b)
main()