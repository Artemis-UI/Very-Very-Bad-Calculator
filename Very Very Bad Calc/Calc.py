from tkinter import *

Plus = False
Minus = False
Divide = False
Addition = False


def Type():
    global Plus, Minus, Divide, Addition
    Plus = True
    Minus = Divide = Addition = False
def Type2():
    global Plus, Minus, Divide, Addition
    Minus = True
    Plus = Divide = Addition = False

def Type3():
    global Plus, Minus, Divide, Addition
    Addition = True
    Minus = Divide = Plus = False

def Type4():
    global Plus, Minus, Divide, Addition
    Divide = True
    Minus = Addition = Plus = False



def Calculate():
    Num1 = 0
    Num2 = 0
    Num1 = Int1.get()
    Num2 = Int2.get()
    Num1 = int(Num1)
    Num2 = int(Num2)
    Int1.delete(0,END)
    Int2.delete(0,END)

    if Plus == True:
        outvaria = Num1 + Num2
    elif Minus == True:
        outvaria = Num1 - Num2
    elif Addition == True:
        outvaria = Num1 * Num2
    elif Divide == True:
        outvaria = Num1 / Num2
    else:
        outvaria = "Operator Missing"
    Varoa.set(outvaria)

    


    
    

    


window = Tk()
window2 = Tk()
window3 = Tk()


Varoa = StringVar()
Varoa.set("main")


Int1 = Entry(window2,
             font=('Arial',50),
             bg='BLACK',
             fg='white')

Int2 = Entry(window2,
             font=('Arial',50),
             bg='BLACK',
             fg='white')


submit_button = Button(window,
                       text="Submit",
                       command=Calculate,
                       bg='BLACK',
                       fg='white')

Plus_Button = Button(window3,
                     text="+",
                     command=Type,
                     bg='BLACK',
                     fg='WHITE',
                     padx=20)

Addition_Button = Button(window3,
                     text="*",
                     command=Type3,
                     bg='BLACK',
                     fg='WHITE',
                     padx=20)

Divide_Button = Button(window3,
                     text="/",
                     command=Type4,
                     bg='BLACK',
                     fg='WHITE',
                     padx=20)

Minus_Button = Button(window3,
                      text="-",
                      command=Type2,
                      bg='BLACK',
                      fg='WHITE',
                      padx=20)

window.geometry("200x100")
window.title("Calculator")

window2.geometry("200x150")
window2.title("Calculator")

window3.geometry("300x300")
window3.title("Calculator")


icon = PhotoImage(file='Calc.png')
window.iconphoto(True,icon)
window.config(background="Gray")
Int1.pack()
Int2.pack()
submit_button.pack()

Output = Label(window, textvariable=Varoa, font=('Arial',14))
Output.pack(pady=20)


Plus_Button.grid(row=0,column=0)
Minus_Button.grid(row=0,column=1)
Addition_Button.grid(row=0,column=2)
Divide_Button.grid(row=0,column=3)

window.mainloop()
window2.mainloop()
window3.mainloop()
