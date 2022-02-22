from random import choice
from tkinter import Tk, Label, Button

PAPER = 'papier'
ROCK = 'kamien'
SCISSORS = 'nozyce'
ACTIONS = [PAPER, ROCK, SCISSORS]

def check_player_win(player, pc):
    win_with = {
        PAPER: ROCK,
        ROCK: SCISSORS,
        SCISSORS: PAPER
    }
    if player == pc:
        return None # nikt
    return win_with[player] == pc
        

def play(what):
    pc = choice(ACTIONS)
    player_win = check_player_win(what, pc)
    if player_win is None:
        label.config(text='Remis sproboj ponownie', fg = 'blue')
    elif player_win:
        label.config(text='Wygrales:)', fg='green')
    else:
        label.config(text='przegrales:(', fg='red')
root = Tk()

root.title('Papier kamien nozyce')
root.geometry('320x240')

label = Label(root, text='Gramy teraz w papier kamien nozyce!', font=20, fg='blue')
label.pack()

button = Button(root, text='Papier', font = 30, command=lambda: play('papier')).pack()
button = Button(root, text='Kamien', font = 30, command=lambda: play('kamien')).pack()
button = Button(root, text='Nozyce', font = 30, command=lambda: play('nozyce')).pack()


root.mainloop()
