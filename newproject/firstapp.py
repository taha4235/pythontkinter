from tkinter import *
import os
root = Tk()
root.title("python application by taha")
root.geometry("700x400+300+50")
root.resizable(FALSE, FALSE)
label1 = Label(text="registration system", font=(
    'Courier', 18), fg="white", bg="lime")
label1.pack(fill=X)
image1 = PhotoImage(file="ux.png")
lab1 = Label(image=image1)
lab1.place(x=0, y=40, width=350, height=370)
# new label
new_label = Label(root, text="register now to use the \nplatform",
                  font=('Courier', 13), fg="black")
new_label.place(x=400, y=50)
frame1 = Frame(root, bg="white")
frame1.place(x=350, y=100, width=350, height=300)
# display function


def registermessage():
    if en1 == "" and en2 == "" and en3 == "" and en4 == "":
        print("you have to enter a data inside the input")
    else:
        import tkinter
        import time
        root = Tk()
        root.configure(background="white")
        root.title("welcome in the main page")
        root.resizable(FALSE, FALSE)
        root.geometry("700x100+300+50")
        labeldescription = Label(
        root, text="[+]you logged in succesfully please wait a few times..", fg="lime", bg="white", font=("Courier", 13))
        labeldescription.place(x=90, y=20)
        root.mainloop()
        time.sleep(10)
def login():
    import tkinter
    import os
    root = Tk()
    root.title("python application by taha")
    root.geometry("700x400+300+50")
    root.resizable(FALSE, FALSE)
    label1 = Label(text="registration system", font=(
    'Courier', 18), fg="white", bg="lime")
    label1.pack(fill=X)
    image1 = PhotoImage(file="ux.png")
    lab1 = Label(image=image1)
    lab1.place(x=0, y=40, width=350, height=370)
# new label
    new_label = Label(root, text="login now to use the \nplatform",
                  font=('Courier', 13), fg="black")
    new_label.place(x=400, y=50)
    frame1 = Frame(root, bg="white")
    frame1.place(x=350, y=100, width=350, height=300)
    labelen1 = Label(frame1,text="first name:",font=('Courier',13),fg="black",bg="white")
    labelen1.place(x=20,y=5)
    en1 = Entry(frame1)
    en1.place(x=20,y=30,width=300,height=20)
    labelen2 = Label(frame1,text="last name:",font=('Courier',13),fg="black",bg="white")
    labelen2.place(x=20,y=60)
    en2 = Entry(frame1)
    en2.place(x=20,y=90,width=300,height=20)
# label3 
    label3 = Label(frame1,text="email address:",font=('Courier',13),fg="black",bg="white")
    label3.place(x=20,y=120)
    en3=Entry(frame1)
    en3.place(x=20,y=150,width=300,height=20)
# rate the app
    label4 = Label(frame1,text="enter a password:",font=("Courier",13),fg="black",bg="white")
    label4.place(x=20,y=180)
    en4=Entry(frame1)
    en4.place(x=20,y=210,width=300,height=20)
# button to submit the data
    button1 = Button(frame1,text="Register",font=("Courier",13),fg="white",bg="royalblue",cursor="hand2",command=registermessage)
    button1.place(x=20,y=250,width=150,height=40)
# login container
    button2 = Button(frame1,text="login",font=("Courier",13),fg="white",bg="red",cursor="hand2")
    button2.place(x=150,y=250,width=180,height=40)
    root.mainloop()

# display function
# adding the input inside the frame
labelen1 = Label(frame1,text="first name:",font=('Courier',13),fg="black",bg="white")
labelen1.place(x=20,y=5)
en1 = Entry(frame1)
en1.place(x=20,y=30,width=300,height=20)
labelen2 = Label(frame1,text="last name:",font=('Courier',13),fg="black",bg="white")
labelen2.place(x=20,y=60)
en2 = Entry(frame1)
en2.place(x=20,y=90,width=300,height=20)
# label3 
label3 = Label(frame1,text="email address:",font=('Courier',13),fg="black",bg="white")
label3.place(x=20,y=120)
en3=Entry(frame1)
en3.place(x=20,y=150,width=300,height=20)
# rate the app
label4 = Label(frame1,text="enter a message:",font=("Courier",13),fg="black",bg="white")
label4.place(x=20,y=180)
en4=Entry(frame1)
en4.place(x=20,y=210,width=300,height=20)
# button to submit the data
button1 = Button(frame1,text="Register",font=("Courier",13),fg="white",bg="royalblue",cursor="hand2",command=registermessage)
button1.place(x=20,y=250,width=150,height=40)
# login container
button2 = Button(frame1,text="login",font=("Courier",13),fg="white",bg="red",cursor="hand2",command=login)
button2.place(x=150,y=250,width=180,height=40)

root.mainloop()