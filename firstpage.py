# import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime

# creating instance of TK
root = Tk()

root.configure(background="white")


# root.geometry("300x300")

def function1():
    os.system("py dataset_capture.py")


def function2():
    os.system("py training_dataset.py")


def function3():
    os.system("py recognizer.py")


def attend():
    os.startfile(os.getcwd() + "/firebase/attendance_files/attendance" + str(datetime.now().date()) + '.xls')


# stting title for the window
root.title("Système de pointage des employées")

# creating a text label
Label(root, text="Système de pointage des employées", font=("times new roman", 20), fg="white", bg="maroon",
      height=2).grid(row=0, rowspan=1, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Ajouter un employé", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function1).grid(
    row=3, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="Entrainer le model", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function2).grid(
    row=4, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="Pointage", font=('times new roman', 20), bg="#0D47A1", fg="white",
       command=function3).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating attendance button
Button(root, text="Liste de pointage", font=('times new roman', 20), bg="#0D47A1", fg="white", command=attend).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

root.mainloop()
