import tkinter
from tkinter import *
from tkinter import ttk

# functions
def Exit():
    exit()


# Tools Design
App=Tk()
App.geometry("400x350")
App.title("Dashboard")
App.configure(bg="lightcyan3")

# title
title_label=ttk.Label(App,text="Dashboard",background="black",foreground="white",font="Calibre 20 bold",width=25, anchor="center")
title_label.grid(row=0,column=0,pady=10,columnspan=4,ipady=10)

# buttons for dataentry
dataentry =ttk.Button(App,text="Data Entry",width=28)
dataentry.grid(row=1,column=0,padx=10,pady=10,columnspan=2,sticky="we",ipady=10)

inputs =ttk.Button(App,text="Querys",width=28)
inputs.grid(row=1,column=2,padx=10,pady=10,columnspan=2,sticky="we",ipady=10)

show =ttk.Button(App,text="Show Products",width=28)
show.grid(row=2,column=0,padx=10,pady=10,columnspan=2,sticky="we",ipady=10)

Exit =ttk.Button(App,text="Exit",width=28,command=Exit)
Exit.grid(row=2,column=2,padx=10,pady=10,columnspan=2,sticky="we",ipady=10)

App.mainloop()
