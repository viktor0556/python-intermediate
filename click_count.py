from tkinter import *

click = 0

def click_counter():
    global click 
    click += 1
    label.config(text=click)

window = Tk()
window.title("Click Count")
window.geometry("200x200")

Click = Button(text=" Click!", command=click_counter)
Click.pack(side="top")

label = Label(text=click, font=('consolas', 40))
label.pack(side="bottom")

window.mainloop()