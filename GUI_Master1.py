
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fire Detection Systemm")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('f.webp')
image2 = image2.resize((1700, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Fire Detection System",font=("Times New Roman", 35, 'bold'),
                    background="black", fg="white", width=55, height=1)
label_l1.place(x=0, y=0)




def log():
    from subprocess import call
    call(["python","video-detection.py"])
    
def reg():
    from subprocess import call
    call(["python","GUI_Master.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Fire Detection System Live", command=log,width=20, height=2,bd=5,font=('times', 20, ' bold '), bg="red", fg="white")
button1.place(x=620, y=100)

button2 = tk.Button(root, text="Fire Detection System Video", command=reg,width=20,height=2,bd=5,font=('times', 20, ' bold '), bg="red", fg="white")
button2.place(x=620, y=200)


button3 = tk.Button(root, text="Exit",command=window,width=17, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button3.place(x=645, y=300)

root.mainloop()