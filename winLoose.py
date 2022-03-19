from random import randint
from ff import money

slot = randint(1, 30)
bl = money
def result():
    while 1:
        global bl
        com = input(
            '1) Напиши 1 чтобы начать игру \n2) После окончания игры пропиши 2 чтобы увидеть результат \nВыберите вариянт: ')
        if com == '1':
            insrt = int(input('Выберите слот от 1 до 30: '))
            stav = int(input('Сколько хотите поставить в размере вашего баланса: '))
            if insrt == slot:
                bl = stav * 2
                print('Вы угодали!')
            elif slot != insrt:
                if bl > 0 and stav <= bl:
                    bl = bl - stav
                    print('Вы не угодали!')
                else:
                    print('У вас не хватет денег!')
        elif com == '2':
            if bl < 1000:
                print('Вы проиграли')
                print('Игра окончена')
                print(f'Ваш баланс состовляет {bl}')
                break
            elif bl > 1000:
                print('Вы Выиграше')
                print('Игра окончена')
                print(f'Ваш баланс состовляет {bl}')
                break
        else:
            print('Нет такого меню!')

result()