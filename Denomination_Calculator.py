from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

root = Tk()
root.geometry("600x500")
root.configure(bg="blue")
root.title("Denomination Calculator")

#upload = Image.open("download.jpeg")
#upload = upload.resize((300,300))
#image = ImageTk.PhotoImage(upload)
#lb = Label(root, image=image, bg="blue")
#lb.place(x=180, y=20)

lb2 = Label(root, text="Hey User, Welcome to the Denomination Calculator!", bg="blue")
lb2.place(x=0.5, y=340, anchor=CENTER)
def Msg():
    Msg = messagebox.showinfo("Alert", "Do you want to continue?")
    if Msg=='ok':
        topwin()

button1 = Button(root, text="Let's get started", command=Msg, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='light grey')
    top.geometry('600x350+50+50')

    label = Label(top, text="Enter the amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are the notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            n2000 = amount//2000
            amount %= 2000
            n500 = amount//500
            amount %= 500
            n100 = amount//100

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)

            e1.insert(END, str(n2000))
            e2.insert(END, str(n500))
            e3.insert(END, str(n100))

        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50 )

    entry.place(x=200, y=80 )

    btn.place(x=240, y=120 )

    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )

    l2.place(x=180, y=230 )

    l3.place(x=180, y=260 )

    e1.place(x=270, y=200 )

    e2.place(x=270, y=230 )

    e3.place(x=270, y=260)

    top.mainloop()

root.mainloop()