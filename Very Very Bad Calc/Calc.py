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

    

window3 = Tk()


Varoa = StringVar()
Varoa.set("Output")


Int1 = Entry(window3,
             font=('Arial',40),
             bg='BLACK',
             fg='white',
             width= 5)

Int2 = Entry(window3,
             font=('Arial',40),
             bg='BLACK',
             fg='white',
             width= 5)


submit_button = Button(window3,
                       text="Submit",
                       command=Calculate,
                       bg='BLACK',
                       fg='white')

Plus_Button = Button(window3,
                     text="+",
                     command=Type,
                     bg='BLACK',
                     fg='WHITE',
                     padx=38.499999,
                     pady=20)

Addition_Button = Button(window3,
                     text="*",
                     command=Type3,
                     bg='BLACK',
                     fg='WHITE',
                     padx=40,
                     pady=20)

Divide_Button = Button(window3,
                     text="/",
                     command=Type4,
                     bg='BLACK',
                     fg='WHITE',
                     padx=40,
                     pady=20)

Minus_Button = Button(window3,
                      text="-",
                      command=Type2,
                      bg='BLACK',
                      fg='WHITE',
                      padx=40,
                      pady=20)



window3.title("Calculator")
window3.configure(bg='GRAY')
icon = PhotoImage(file='Calc.png')


Output = Label(window3, textvariable=Varoa, font=('Arial',40),bg='BLACK', fg='WHITE')

Int1.grid(row= 0, column= 0)
Int2.grid(row = 1, column= 0)
Plus_Button.grid(row=0,column=1)
Minus_Button.grid(row=1,column=1)
Addition_Button.grid(row=2,column=1)
Divide_Button.grid(row=3,column=1)
Output.grid(row=5, column=0, columnspan=2,sticky='nsew')
submit_button.grid(row=3, column= 0,sticky='nsew')

window3.mainloop()
