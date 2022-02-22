from tkinter import Tk, Label, Button

def click_action():
    print('oh')

root = Tk()

root.title('moja pierwsza aplikacja')
root.geometry('640x480')

label = Label(root, text='Hej!', font=20, fg='blue')
label.pack()

button = Button(root, text='Klikaj to kidosie', width = 10, command=click_action)
button.pack()

root.mainloop()
