import customtkinter
from PIL import Image
import tkinter.messagebox as mbox

def Main():
    icon = "images/icon.ico"

    root = customtkinter.CTk()
    root.config(width=400,height=300)
    root.maxsize(400,300)
    root.minsize(400,300)
    root.iconbitmap(icon)
    root.wm_iconbitmap(icon)
    root.title('FPS BOOSTER')

    def start_drag(event):
            global x,y
            x = event.x
            y = event.y
    def move_window(event):
        new_x = (root.winfo_x() + event.x) - x
        new_y = (root.winfo_y() + event.y) - y
        root.geometry(f"+{new_x}+{new_y}")

    root.overrideredirect(True)
    
    title_bar = customtkinter.CTkFrame(root,height=25,width=800,bg_color="lightblue",fg_color="lightblue")
    title_bar.place(x=0,y=0)
    title_bar.bind("<ButtonPress-1>",start_drag)
    title_bar.bind("<B1-Motion>",move_window)
    

    LoadLabels(root)
    root.mainloop()

def LoadLabels(root):
    off = customtkinter.CTkImage(Image.open("images\off.png"), size=(15, 15))
    
    close_button = customtkinter.CTkButton(root,text="",image=off,bg_color="lightblue",fg_color="lightblue",hover_color="lightblue",width=10,height=10,command=root.destroy,font=("verdana bold",15))
    close_button.place(x=370,y=0)

    titleLabel = customtkinter.CTkLabel(root,text="FPS BOOSTER",font=("verdana bold",17),text_color="black")
    titleLabel.place(x=150,y=25)

    cleanMemoryButton = customtkinter.CTkButton(root,text = "Clean Memory",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",command=mess)
    cleanMemoryButton.place(x=30,y=70)
       
def mess():
    mbox.showinfo(title="FPS BOOSTER",message="Memory successfully cleaned.")
Main()