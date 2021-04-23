# TKinter is python's standard GUI(Graphic User Interface) Toolkit package
# It is a thin object-oriented layer on top of Tk

########### Show a window ###############
from tkinter import *
# root = Tk(className="My first GUI")
# root.mainloop()

########### Label ###############
# import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="Hello World", font=("times",20,"bold") ,padx=10, pady=10)
# label.pack()
# root.mainloop()

########### Label in a class ###############
# import tkinter as tk
# class Root(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
#         self.label.pack()
# if __name__ == "__main__":
#     root = Root()
#     root.mainloop()

########### Labels & Packing ###############
# from tkinter import Tk, Label, Y, RIGHT, LEFT
# root = Tk()
# label1 = Label(root, text="Yellow!", background="yellow")
# label2 = Label(root, text="Orange?", background="orange")

# label1.pack(fill=Y, padx=25, ipady=15, side=LEFT)
# label2.pack(fill=Y, padx=25, ipady=15, side=RIGHT)
# root.mainloop()

########### Input box & colors ###############
# from tkinter import *
# color = ["red","green","orange","white","yellow","blue"]
# r = 0
# for c in color:
#     Label(text=c, relief=RIDGE, width=15).grid(row=r, column=0)
#     Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1)
#     r = r + 1
# mainloop()

########### Buttons Calls ###############
from tkinter import *
def Pressed():
    print("Hello, Press me again")
root =Tk()
button = Button(root, text="Press Me", command = Pressed)
button.pack(pady=40, padx=40)
root.mainloop()
