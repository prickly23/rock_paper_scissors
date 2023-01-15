import random

win_user = 'Вы победили!'
win_comp = 'Победил компьютер'

counter_user = 0
counter_comp = 0
while True:
    user_choice = input('Камень, ножницы или бумага? ').lower()
    if user_choice == 'камень' or user_choice == 'ножницы' or user_choice == 'бумага':
        choice = ['камень', 'ножницы', 'бумага']
        comp_choice = random.choice(choice)
        print(f'Вы выбрали {user_choice}, компьютер выбрал {comp_choice}')
        if user_choice == comp_choice:
            print('Получается ничья!')
        elif user_choice == 'камень':
            if comp_choice == 'бумага':
                counter_comp += 1
                print(win_comp)
            else:
                counter_user += 1
                print(win_user)
        elif user_choice == 'бумага':
            if comp_choice == 'ножницы':
                counter_comp += 1
                print(win_comp)
            else:
                counter_user += 1
                print(win_user)
        elif user_choice == 'ножницы':
            if comp_choice == 'камень':
                counter_comp += 1
                print(win_comp)
            else:
                counter_user += 1
                print(win_user)
        play_again = input('Сыграем еще? да/нет: ')
        if play_again == 'нет':
            print(f'Итоговый счет: компьютер - {counter_comp}: пользователь - {counter_user}')
            break
    else:
        print('Некорректный ввод! Попробуйте еще раз!')
