from tkinter import *
import random

root = Tk()
root.title("Color random doer 🌈")
root.geomwtry("600x600")
root.confic(bg="white")

label_name = Label(root,bg="dark red", font=("Bahnschrift Light",45))
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)

class game:
    def __init__(self):
        self.__score - 0
    
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED"]
