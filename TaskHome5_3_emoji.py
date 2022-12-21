import emoji

def print_game(ls1, ls2, ls3):
    print()
    print(f' {ls1[0]}  |  {ls1[1]}  |  {ls1[2]} ')
    print(' --------------')
    print(f' {ls2[0]}  |  {ls2[1]}  |  {ls2[2]}')
    print(' --------------')
    print(f' {ls3[0]}  |  {ls3[1]}  |  {ls3[2]}')
    print()

emoji_x = emoji.emojize(':negative_squared_cross_mark:', language='alias')
emoji_o = emoji.emojize(':zero:', language='alias')

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

print_game(lst1, lst2, lst3)

for i in range(1, 6):
    x1 = int(input(f'Введите позицию для {emoji_x} :'))
    if 1 <= x1 <= 3: 
        lst1[lst1.index(x1)] = emoji_x
    elif 4 <= x1 <= 6: 
        lst2[lst2.index(x1)] = emoji_x
    elif 7 <= x1 <= 9: 
        lst3[lst3.index(x1)] = emoji_x
    else: 
        print('Вы ввели некорректное значение')
        break
    if all([j == emoji_x for j in lst1]) or all([k == emoji_x for k in lst2]) or all([m == emoji_x for m in lst3]):
        print()
        print_game(lst1, lst2, lst3)
        print('Крестики победили')
        print()
        break
    elif (lst1[0] == emoji_x and lst2[0] == emoji_x and lst3[0] == emoji_x or lst1[1] == emoji_x and lst2[1] == emoji_x and lst3[1] == emoji_x or 
    lst1[2] == emoji_x and lst2[2] == emoji_x and lst3[2] == emoji_x or lst1[0] == emoji_x and lst2[1] == emoji_x and lst3[2] == emoji_x or 
    lst1[2] == emoji_x and lst2[1] == emoji_x and lst3[0] == emoji_x):
        print()
        print_game(lst1, lst2, lst3)
        print(f'{emoji_x} победили')
        print()
        break
    print_game(lst1, lst2, lst3)
    if i == 5: 
        print('Вы сыграли в ничью')
        print()
        break
    o1 = int(input(f'Введите позицию для {emoji_o}  :'))
    if 1 <= o1 <= 3: 
        lst1[lst1.index(o1)] = emoji_o
    elif 4 <= o1 <= 6: 
        lst2[lst2.index(o1)] = emoji_o
    elif 7 <= o1 <= 9: 
        lst3[lst3.index(o1)] = emoji_o
    else: 
        print('Вы ввели некорректное значение')
        break
    if all([j == emoji_o  for j in lst1]) or all([k == emoji_o  for k in lst2]) or all([m == emoji_o  for m in lst3]):
        print()
        print_game(lst1, lst2, lst3)
        print('Крестики победили')
        print()
        break
    elif (lst1[0] == emoji_o  and lst2[0] == emoji_o  and lst3[0] == emoji_o  or lst1[1] == emoji_o  and lst2[1] == emoji_o  and lst3[1] == emoji_o  or 
    lst1[2] == emoji_o  and lst2[2] == emoji_o  and lst3[2] == emoji_o  or lst1[0] == emoji_o  and lst2[1] == emoji_o  and lst3[2] == emoji_o or 
    lst1[2] == emoji_o  and lst2[1] == emoji_o  and lst3[0] == emoji_o):
        print()
        print_game(lst1, lst2, lst3)
        print(f'{emoji_o}  победили')
        print()
        break
    print_game(lst1, lst2, lst3)