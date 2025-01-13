from random import randint
import math

from unicodedata import digit

# Глобальные переменные
n = 100  # Максимально возможное загадываемое число
sm = 0  # Счетчик попыток
best_result = 0  # Лучший результат


# Используемые функции
def is_valid(z):  # Защита от дурака
    return 1 <= z <= n


def guess(digit, x):
    global sm, n
    while digit != x:
        if digit > x:
            print('Слишком много, попробуйте еще раз')
        elif digit < x:
            print('Слишком мало, попробуйте еще раз')

        sm += 1  # Увеличиваем счетчик попыток
        digit = int(input())

        while not is_valid(digit):
            print('А может быть все-таки введем целое число от 1 до ', n, '?', sep='')
            digit = int(input())

    print('Вы угадали, поздравляем!')

print('Добро пожаловать в числовую угадайку')

def fun():
    global n, best_result
    print('Хотите изменить максимально возможное загадываемое число? По умолчанию стоит число 100.')
    question = input()
    if question[:2].capitalize() == 'Да' or question.capitalize() == 'Yes':
        print('Прошу!')
        n = int(input())
        print('Погнали! Введи число!')
        digit = int(input())
    elif question.isdigit():
        n = int(question)
        print('Погнали! Введи число!')
        digit = int(input())

    while not is_valid(digit):
        print('А может быть все-таки введем целое число от 1 до ', n, '?', sep='')
        digit = int(input())

    x = randint(1, n)  # Загадываемое число
    guess(digit, x)

    best_result = math.ceil(math.log2(n))


fun()

print('Хотите узнать сколько Вы использовали попыток, чтобы угадать число?:)')
question = input()
if question[:2].capitalize() == 'Да' or question.capitalize() == 'Yes':
    print(f'Вы потратили {sm + 1} попыток ;)'
          f'Лучший, возможный, результат {best_result}!')
flag = True
while flag == True:
    print('Хотите сыграть еще? Это бесплатно!')
    question = input()
    if question.capitalize() == 'Да' or question.capitalize() == 'Yes':
        sm = 0  # Сброс счетчика попыток
        n = 100
        fun()
        print('Хотите узнать сколько Вы использовали попыток, чтобы угадать число?:)')
        question = input()
        if question[:2].capitalize() == 'Да' or question.capitalize() == 'Yes':
            print(f'Вы потратили {sm + 1} попыток ;)'
                  f'Лучший, возможный, результат {best_result}!')
    else:
        flag = False

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')