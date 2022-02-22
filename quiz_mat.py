import tkinter as tk # obsluga okna
import tkinter.font as tkFont # czcionki
import random #losowanie
import time #czas odgadywania

def open_window():
    global nick

    new_window = tk.Toplevel()
    new_window.geometry('200x80')

    lbl = tk.Label(new_window, text='Nick: ')
    lbl.pack()
    nick_input = tk.Entry(new_window, textvariable=nick)
    nick_input.pack()
    bb = tk.Button(
        new_window, text='Graj!'
        command=lambda: close_new_window(nick_input, new_window
    )
    bb.pack()

def close_new_window(nick_input, new_window():
    global question_no, time_start, points

    time_start = time.time()
    points = 0
    next_question()

# GUI - Graphical User Interface
gui = tk.Tk()
gui.title('Quiz matematyczny')
gui.geometry('480x360')

points = 0
question_no = 0 # ktore pytanie
time_start = 0 #kiedy gracz zaczął gre
nick = tk.StringVar() # nick gracza

btn1 = tk.Button(gui, text='btn1')
btn2 = tk.Button(gui, text='btn2')

btn1.grid(row=0, column=0, sticky='NSEW')
btn2.grid(row=0, column=1, sticky='NSEW')
btn3.grid(row=1, column=1, sticky='NSEW')



def next_question():
    global points, question_no, time_start, nick

    question_no += 1
    if question_no <= 10:
        generate_question()
    else:
            timeDiff = round(time.time() - time_start, 3)
            display_question(
                f'Brawo {nick.get()}!\n{points}/10 pkt.w {timeDiff}s',
                ['Jeszcze', 'raz', '?', '?']
            )
            question_no = 0

def generate_question():
    global question_ok
 
    # losujemy 2 liczby
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    equation = f'{a} * {b}'
    result = eval(equation)
    options = [result, result + 1, result + 2, result - 1]
    random.shuffle(options)

    question_ok = str(result)
    display_question(equation, options)
    


def answer(btn):
    global question_ok, points
    if question_no == 0:
        display_question('wpisz nick', ['']*4)
        open_window()
    if btn['text'] == question_ok:
        points += 1
    next_question()


def display_question(content, options):
    lblContent['text'] = content
    btnA['text'] = str(options[0])
