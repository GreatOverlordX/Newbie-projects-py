# Classic Snake game with Python3
# Project based on Bro Code YouTube video  https://youtu.be/bfRwxS5d0SI

from tkinter import *
import random


# charasteristics of game
GAME_WIDTH = 1600
GAME_HEIGHT = 920
SPEED = 80 # the lower the faster the speed
SPACE_SIZE = 40
BODY_PARTS = 2
SNAKE_COLOR = '#DC143C' # crimson
FOOD_COLOR =  '#FFD700' # gold
BACKGROUND_COLOR = '#000000' # black




# Snake information 
class Snake: 
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
            

# Food information            
class Food: 
    
   def __init__(self):
       
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

# movement dynamic information
def next_turn(snake, food) :
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    x = x % GAME_WIDTH
    y = y % GAME_HEIGHT

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text='🐍 Your score: {}'.format(score))

        canvas.delete('food')

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction) :
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
            
# Here I made the snake to not collision with the edges therefore it return from left to right and viceversa as well as up and down.
def check_collisions(snake) :
    x, y = snake.coordinates[0]
    x = x % GAME_WIDTH
    y = y % GAME_HEIGHT
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
         return True
    return False

# Game over dynamic with the Time New Roman because it reminded me of Souls-like games
def game_over() :
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Times New Roman',150), text='YOU LOST ... ☹️', fill='red', tag='gameover')
    canvas.create_text(canvas.winfo_width()/5, canvas.winfo_height()/5,
                       font=('Times New Roman',100), text='OH NO! 😵', fill='red', tag='sadtext')


# I initially thought of a maximizable version
window = Tk() 
window.state('zoomed') # Start the program maximized
canvas = Canvas(window, bg=BACKGROUND_COLOR)
canvas.configure(width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack
window.configure(bg=BACKGROUND_COLOR)
canvas = Canvas()
canvas.pack
window.title('Classic Snake game')
window.resizable(True, True) # Making possible to resize window


score = 0
direction = 'up'

label = Label(window, text='🐍 Your score: {}'.format(score), bg=BACKGROUND_COLOR, fg='red', font=('Times New Roman', 40,))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()