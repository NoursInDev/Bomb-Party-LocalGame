import socket
from tkinter import *
import tkinter as tk
fenetre = Tk()
fenetre.geometry("300x200")
fenetre.resizable(width=False, height=False)
fenetre.title("Bombparty(Client) - Initialisation")
fenetre.configure(bg='#2c2f33')
user_input = StringVar(fenetre,)
entry_one=Entry(fenetre, textvariable=user_input)
entry_one.grid(row=3,column=0,padx=10)
fenetre.mainloop()