from tkinter import *


def click(event):
    global scval
    text=event.widget.cget('text')
    # print(text)
    if text == "=": 
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:

                value = (eval(screen.get()))
            except Exception as e:
                print(e)
                scval.set("Error")
                scval.update()


        scval.set(value)
        scval.update()

    elif text =="C":
        scval.set("")
        scval.update()
    else:
        scval.set(scval.get() + text)
        scval.update()



root = Tk()


root.title(" Calculator ")
root.geometry("900x1200")
root.wm_iconbitmap("a.ico")

scval = StringVar()
scval.set("")


screen = Entry(root,textvar=scval,font="licida 40 bold")
screen.pack(fill=X,ipadx=50,padx=20,pady=20)



f = Frame(root,bg="grey")

b = Button(f,text="9",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


b = Button(f,text="8",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)

b = Button(f,text="7",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


f.pack()


f = Frame(root,bg="grey")

b = Button(f,text="6",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


b = Button(f,text="5",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)

b = Button(f,text="4",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


f.pack()


f = Frame(root,bg="grey")

b = Button(f,text="3",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


b = Button(f,text="2",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)

b = Button(f,text="1",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root,bg="grey")

b = Button(f,text="0",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=21,pady=10)
b.bind("<Button-1>", click)


b = Button(f,text="*",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=22,pady=10)
b.bind("<Button-1>", click)

b = Button(f,text="/",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=21,pady=10)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root,bg="grey")

b = Button(f,text="+",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


b = Button(f,text="-",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=21,pady=10)
b.bind("<Button-1>", click)

b = Button(f,text="=",font="lucida 15 bold",padx=20,pady=10)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="C", font="lucida 15 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=10)
b.bind("<Button-1>", click)


b = Button(f, text="%", font="lucida 15 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="--", font="lucida 15 bold", padx=20, pady=10)
b.pack(side=LEFT, padx=18, pady=10)
b.bind("<Button-1>", click)


f.pack()


root.mainloop()
