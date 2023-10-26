
from argparse import Action
from distutils import command
import customtkinter
import tkinter.messagebox as mbox
from discordwebhook import Discord

def Main():
    root = customtkinter.CTk()
    root.config(width=400,height=300)
    root.maxsize(400,300)
    root.minsize(400,300)
    root.title('FPS BOOSTER')
    LoadLabels(root)
    
    root.mainloop()

def LoadLabels(root):
    titleLabel = customtkinter.CTkLabel(root,text="FPS BOOSTER",font=("Fixedsys",21),text_color="black")
    titleLabel.place(x=150,y=15)

    cleanMemoryButton = customtkinter.CTkButton(root,text = "Clean Memory",font=("Fixedsys",21),text_color="black",fg_color="lightblue",hover_color="white",command=mess)
    cleanMemoryButton.place(x=30,y=70)
       
def mess():
    mbox.showinfo(title="FPS BOOSTER",message="Memory successfully cleaned.")
Main()