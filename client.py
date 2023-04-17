import socket
from tkinter import *
import tkinter as tk


def get_ip():
    return entree_ip.get()

fenetre = Tk()
fenetre.geometry("300x200")
fenetre.resizable(width=False, height=False)
fenetre.title("Bombparty(Client) - Initialisation")
fenetre.configure(bg='#2c2f33')

user_input = StringVar(fenetre)
entree_ip=Entry(fenetre, textvariable=user_input)
entree_ip.grid(row=3,column=0,padx=10)
button = tk.Button(fenetre, text="Get Text", command=get_ip)
fenetre.mainloop()

serverAddressPort   = (get_ip(), 20001)              #(ip,port)
bufferSize  = 1024
print(serverAddressPort)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(str.encode(pseudo), serverAddressPort)
