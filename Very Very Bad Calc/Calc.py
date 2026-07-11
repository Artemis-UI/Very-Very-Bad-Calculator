from tkinter import*

outvaria = "main"
Plus = False
Minus = False
Divide = False
Addition = False

def Type():
    Plus = True
    return Plus
def Type2():
    Minus = True
    return Minus
def Type3():
    Addition = True
    return Addition
def Type4():
    Divide = True
    return Divide


def Calculate():
    Num1 = Int1.get()
    Num2 = Int2.get()
    Int1.delete(0,END)
    Int2.delete(0,END)





    
    

    


window = Tk()
window2 = Tk()
window3 = Tk()


Output = Label(window,
               text=outvaria,
               font=('Arial',20,'bold'),
               fg='Blue',
               bg='Gray',
               relief=SUNKEN,
               bd=4,
               padx=8)


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
Output.pack()
Int1.pack()
Int2.pack()
submit_button.pack()


Plus_Button.grid(row=0,column=0)
Minus_Button.grid(row=0,column=1)
Addition_Button.grid(row=0,column=2)
Divide_Button.grid(row=0,column=3)

window.mainloop()
window2.mainloop()
window3.mainloop()
