from tkinter import *
import random as random

game = True
field = []
x_count = 0

length = 10
widht = 10

def print_window():                                                             # отрисовка игрового окна
    root = Tk()
    root.title('Игра')    
    for row in range(length):
        line = []
        for col in range(widht):
            button = Button(root, text = ' ', width = 4, height = 2, 
                            font = ('Verdana', 20, 'bold'),
                            background = 'lavender',
                            command = lambda row = row, col = col: click(row, col))
            button.grid(row = row, column = col, sticky = 'nsew')
            line.append(button)
        field.append(line)       
    new_button = Button(root, text = 'НАЧАТЬ ЗАНОВО', width = 4, height = 2, 
                        font = ('Verdana', 10, 'bold'),
                        command = new_game)
    new_button.grid(row = 11, column = 3, columnspan = 4, sticky = 'nsew')
    root.mainloop()    

def click(row, col):                                                            # обработка нажатия на поле 
    if game and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global x_count
        x_count += 1
        check_lose('X')
        if game and x_count < 51:
            computer_move()
            check_lose('O')
        if x_count == 51:
            messagebox.showinfo("Игра", "Игра закончилась ничьей")

def new_game():                                                                 # кнопка "Новая игра", которая очищает поле и начинает игру заного
    for row in range(length):
        for col in range(widht):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game
    game = True
    global x_count
    x_count = 0

def game_over(player):                                                          # функция окончания игры и показа окна победителя
    global game
    game = False
    if player == 'X': messagebox.showinfo('Победитель', 'Победил комьютер')
    else: messagebox.showinfo('Победитель', 'Вы выиграли')

def sum_empty_blocks():                                                         # функция подсчета пустых клеток 
    empty_blocks = 0
    for row in range(length):
        for col in range(widht):
            if field[row][col]['text'] == ' ':
                empty_blocks += 1
    return empty_blocks

def computer_move():                                                            # функция хода компьютера, которая в зависимости от других функций
    key = 0                                                                     # определяет ход
    blocks = sum_empty_blocks()
    while True:
        row = random.randint(0, length - 1)
        col = random.randint(0, widht - 1)
        if field[row][col]['text'] == ' ': 
            answer = move_area(row,col)
            key += 1
            if  key == blocks and answer == False:
                last_move = losing_move(row, col)
                if last_move:
                    answer = False
                    if key == blocks:
                        field[row][col]['text'] = 'O'
                        break 
                else:
                    key = 0
                    answer = True                 
            if answer:
                field[row][col]['text'] = 'O'
                break

def move_area(row, col):                                                        # функция, которая определяет некую пустую зону, границы которой 
    answer = False                                                              # является 1 клетка во всех направлениях 
    try:
        if (field[row - 1][col - 1]['text'] != 'O' and
            field[row - 1][col]['text'] != 'O' and
            field[row - 1][col + 1]['text'] != 'O' and
            field[row][col + 1]['text'] != 'O' and
            field[row + 1][col + 1]['text'] != 'O' and
            field[row + 1][col]['text'] != 'O' and
            field[row + 1][col - 1]['text'] != 'O' and
            field[row][col - 1]['text'] != 'O'):
                answer = True
    except IndexError:
        print('move_area_exception')         
    return answer   

def losing_move(row, col):                                                      # функия, определяющая ялвяется ли ход - проигрышным 
    chance = False
    kit = 0
    try:
        for i in range(1,5):                                                    # проверка проигрышного хода по горизонтали в левую сторону
            if field[row][col - i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по горизонтали в правую сторону
            if field[row][col + i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по вертикали вверх
            if field[row - i][col]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по вертикали вниз
            if field[row + i][col]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по диагонали влево вниз
            if field[row + i][col - i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по диагонали вправо вниз
            if field[row + i][col + i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по диагонали вправо вверх
            if field[row - i][col + i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0
        for i in range(1,5):                                                    # проверка проигрышного хода по диагонали влево вверх
            if field[row - i][col - i]['text'] == 'O':
                kit += 1
                if kit == 4:
                    kit = 0
                    chance = True
                    return chance
        kit = 0                    
    except IndexError:
        print('losing_move_exception')  
        
    
    
def check_lose(player):                                                         # функция проверки проигрыша по горизонтали, вертикали, диагонали 
    horizontal_lose(player)
    vertical_lose(player)
    diagonal_lose(player)
   
        
def horizontal_lose(player):
    series = 0
    for row in range(length):
        for col in range(widht):
            if field[row][col]['text'] == player:
                series += 1
                if series == 5:
                    field[row][col]['background'] = 'pink'
                    game_over(player)
            else: series = 0
        series = 0
        
def vertical_lose(player):
    series = 0
    for col in range(length):
        for row in range(widht):
            if field[row][col]['text'] == player:
                series += 1
                if series == 5:
                    field[row][col]['background'] = 'pink'
                    game_over(player)                
            else: series = 0                
        series = 0
        
def diagonal_lose(player):
    for row in range(length):
        for col in range(widht):
            try:
                if ((field[row][col]['text'] == player and
                    field[row + 1][col + 1]['text'] == player and
                    field[row + 2][col + 2]['text'] == player and
                    field[row + 3][col + 3]['text'] == player and
                    field[row + 4][col + 4]['text'] == player) or
                    (field[row][col]['text'] == player and
                    field[row + 1][col - 1]['text'] == player and
                    field[row + 2][col - 2]['text'] == player and
                    field[row + 3][col - 3]['text'] == player and
                    field[row + 4][col - 4]['text'] == player)):
                        field[row][col]['background'] = 'pink'
                        game_over(player)
            except IndexError:
                continue                  
print_window()