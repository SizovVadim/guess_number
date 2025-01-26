from random import randint

number_leader = randint(1, 100)
number_player = int(input('Введите число: '))
while True:
    if number_leader > number_player:
        print('Ваше число меньше того, что загадано')
        number_player = int(input('Попробуй еще раз!'))
    elif number_leader < number_player:
        print('Ваше число больше того, что загадано')
        number_player = int(input('Попробуй еще раз!'))
    elif number_player == number_leader:
        break
print('Отличная интуиция! Вы угадали число :)')
