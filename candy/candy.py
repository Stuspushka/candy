import random

f_turn = input('Выберите орел или решка? ')
f_turn.lower()
turn_checklist = ['орел', 'решка']
if f_turn == random.choice(turn_checklist):
    f_turn = 1
    print('Вы ходите первым')
else:
    f_turn = 0
    print('Компьютер ходит первым')
c = 150
while c>=0:
    if c>=57:
        if f_turn ==1:
            t=int(input('Введите количество конфет, которые вы ходите взять, но не более 28: '))
            if 0< t <= 28:
                c=c-t
                print(f'Всего осталось {c} конфет')
                print('Ход компьютера')
                t_k=random.randint(1,28)
                print(f'Компьютер взял {t_k} конфет')
                c=c-t_k
                print(f'Всего осталось {c} конфет')
            else:
                print('Вы не можете столько взять')
                continue
        else:
            t_k = random.randint(1, 28)
            print(f'Компьютер взял {t_k} конфет')
            c = c - t_k
            print(f'Всего осталось {c} конфет')
            print('Ваш ход')
            t = int(input('Введите количество конфет, которые вы ходите взять, но не более 28: '))
            if 0< t <= 28:
                c = c - t
                print(f'Всего осталось {c} конфет')
            else:
                print('Вы не можете столько взять')
                continue
    elif c>29:
        if f_turn == 1:
            t = int(input('Введите количество конфет, которые вы ходите взять, но не более 28: '))
            if 0< t <= 28:
                c = c - t
                if c>28:
                    print(f'Всего осталось {c} конфет')
                    print('Ход компьютера')
                    t_k = c-29
                    print(f'Компьютер взял {t_k} конфет')
                    c = c - t_k
                    print(f'Всего осталось {c} конфет')
                else:
                    print('Компьютер победил!')
                    break
            else:
                print('Вы не можете столько взять')
                continue
    elif c==29:
        t_k = 1
        print(f'Компьютер взял {t_k} конфет')
        print('Вы победили!')
        break
    else:
        if f_turn== 1:
            print('Вы победили!')
            break
        else:
            print('Компьютер победил!')
            break
