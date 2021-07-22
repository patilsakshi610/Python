from random import sample
from tkinter import *

root=Tk()
root.geometry("650x500")
root.minsize(200,200)
root.configure(bg="light gray")
root.title("random_password_generator")

main=Frame(root)
main.pack()

s=Label(text="Random Password Generator",bg="gray",fg="white",font=("Castellar",25))
s.pack(fill=X)


n=IntVar()
p=Label(text="enter the length of passwaord :",bg="light gray",fg='black',font=("Castellar",15))
p.place(x=10,y=80)
l=Entry(textvariable=n,font=(25))
l.place(x=10,y=120)
n.set("")


def Print():
    try:

        count =n.get()
        count_num = int(count)
        if (count_num < 6):
            disp = Label(text="Paasword Length must be greater than six", fg="white",bg="gray", font=("Castellar", 10))
            disp.place(x=10, y=220)

            def clear():
                disp.place_forget()

            b = Button(text='clear', command=clear, bg="gray", fg="white")
            b.place(x=150, y=350)


        elif (count_num > 20):
            disp1 = Label(text="Paasword Length must be smaller than twenty", fg="white", bg="gray", font=("Castellar", 10))
            disp1.place(x=10, y=220)

            def clear():
                disp1.place_forget()

            b = Button(text='clear', command=clear, bg="gray", fg="white")
            b.place(x=150, y=350)

        else:

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            p = "".join(sample(s,count_num))
            passwd=StringVar(root,name="pass")
            root.setvar(name="pass",value=p)
            disp3 = Label(text="Your password is :",fg="purple",font=("Castellar",10))
            disp3.place(x=10, y=200)
            disp4 = Label(text="%s," % root.getvar(name="pass"),bg="white",fg="blue",font=(18))
            disp4.place(x=10, y=240)

            def clear():
                disp3.place_forget()
                disp4.place_forget()

            b = Button(text='clear', command=clear, bg="gray", fg="white")
            b.place(x=150, y=350)

    except:

        disp5= Label(text="please enter valid number", fg="red", font=("Castellar", 10))
        disp5.place(x=10, y=240)


b=Button(text='Generator\nPassword',command=Print,bg="gray",fg="white")
b.place(x=150,y=300)




root.mainloop()
