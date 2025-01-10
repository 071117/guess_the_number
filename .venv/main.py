from random import *
x = randint(1, 100)
a = ['Слишком много, попробуйте еще раз', 'Слишком мало, попробуйте еще раз', 'Вы угадали, поздравляем!']
print('Добро пожаловать в числовую угадайку')
print('Введи число!')
digit = int(input())

flag = True

def is_valid(z):
    return 1 <= z <= 100

while not is_valid(digit):
    print('А может быть все-таки введем целое число от 1 до 100?')
    digit = int(input())


def guess(digit):
    while digit != x:
        if digit > x:
            print(a[0])
        elif digit < x:
            print(a[1])

        digit = int(input())

        while not is_valid(digit):
            print('А может быть все-таки введем целое число от 1 до 100?')
            digit = int(input())

    print(a[2])


guess(digit)
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')






