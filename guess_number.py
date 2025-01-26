from random import randint

number_leader = randint(1, 100)
number_player = int(input('Введите число: '))
while number_leader != number_player:
    if number_leader > number_player:
        print('Ваше число меньше того, что загадано')
        number_player = int(input('Попробуй еще раз!'))
    elif number_leader < number_player:
        print('Ваше число больше того, что загадано')
        number_player = int(input('Попробуй еще раз!'))
if number_player == number_leader:
    print('Отличная интуиция! Вы угадали число :)')
