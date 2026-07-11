from tkinter import*
from Intern import outvaria


def submit():
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

Int2 = Entry(window3,
             font=('Arial',50),
             bg='BLACK',
             fg='white')


submit_button = Button(window,
                       text="Submit",
                       command=submit,
                       bg='BLACK',
                       fg='white')

window.geometry("200x100")
window.title("Calculator")

window2.geometry("200x100")
window2.title("Calculator")

window3.geometry("200x100")
window3.title("Calculator")


icon = PhotoImage(file='Calc.png')
window.iconphoto(True,icon)
window.config(background="Gray")
Output.pack()
Int1.pack()
Int2.pack()
submit_button.pack()
window.mainloop()
window2.mainloop()
window3.mainloop()