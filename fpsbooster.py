import customtkinter
from PIL import Image
import tkinter.messagebox as mbox
import os

icon = "images/icon.ico"
logo = customtkinter.CTkImage(Image.open("images\Logo.png"), size=(100, 100))
appdata = os.getenv('LOCALAPPDATA')
def windowConfig(window,x,y):
    window.eval('tk::PlaceWindow . center')
    window.maxsize(x,y)
    window.minsize(x,y)
    window.iconbitmap(icon)
    window.wm_iconbitmap(icon)
    window.overrideredirect(True)
    window.title('FPS BOOSTER')

def tempWindow():
    def UpdateW():
         Main(tempw)
    tempw = customtkinter.CTk()
    windowConfig(tempw,300,300)

    displaylogo = customtkinter.CTkLabel(tempw,height=200,width=200,image=logo,text="")
    displaylogo.place(x=50,y=5)

    progressbar = customtkinter.CTkProgressBar(tempw, orientation="horizontal",mode="indeterminate",indeterminate_speed=2,corner_radius=3)
    progressbar.place(x=50,y=200)
    progressbar.start()

    tempw.after(2500,UpdateW)
    tempw.mainloop()

def Main(tempw):
    tempw.destroy()
    root = customtkinter.CTk()
    windowConfig(root,400,300)
    LoadLabels(root)
    root.mainloop()

def LoadLabels(root):
    def start_drag(event):
            global x,y
            x = event.x
            y = event.y
    def move_window(event):
        new_x = (root.winfo_x() + event.x) - x
        new_y = (root.winfo_y() + event.y) - y
        root.geometry(f"+{new_x}+{new_y}")

    border = customtkinter.CTkFrame(root,400,300,border_color="lightblue",border_width=4,bg_color="transparent",fg_color="transparent")

    title_bar = customtkinter.CTkFrame(root,height=25,width=800,bg_color="lightblue",fg_color="lightblue")
    title_bar.bind("<ButtonPress-1>",start_drag)
    title_bar.bind("<B1-Motion>",move_window)
    titleLabel = customtkinter.CTkLabel(root,text="FPS BOOSTER",font=("Arial Baltic",17),height=25,text_color="black",bg_color="lightblue",fg_color="transparent")
    titleLabel.bind("<ButtonPress-1>",start_drag)
    titleLabel.bind("<B1-Motion>",move_window)

    off = customtkinter.CTkImage(Image.open("images\off.png"), size=(15, 15))
    close_button = customtkinter.CTkButton(root,text="",image=off,bg_color="lightblue",fg_color="lightblue",hover_color="lightblue",width=10,height=10,command=root.destroy,font=("verdana bold",15))
    cleanMemoryButton = customtkinter.CTkButton(root,text = "Optimize Windows",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",command=Optimization)
    netOptimizeButton = customtkinter.CTkButton(root,text = "Optimize Internet  ",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",command=NetOptimization)
    fortniteLow = customtkinter.CTkButton(root,text = "Optimize Fortnite",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",command=FortniteLowGraphics)
    fortniteLowLabel = customtkinter.CTkLabel(root,text="(low graphics)",font=("verdana",12),text_color="grey",bg_color="transparent",fg_color="transparent")

    border.place(x=0,y=0)
    title_bar.place(x=0,y=0)
    close_button.place(x=370,y=0)
    titleLabel.place(x=150,y=0)
    cleanMemoryButton.place(x=30,y=70)
    netOptimizeButton.place(x=30,y=125)
    fortniteLowLabel.place(x=255,y=40)
    fortniteLow.place(x=230,y=70)

       
def Optimization():
    autorization = mbox.askquestion(title="Confirmation",message="This will run some commands in your command line, do you want to continue?")
    if autorization == "yes":
        os.startfile(r"files\optimization.bat")
        return
    else:
        mbox.showinfo(title="FPS BOOSTER",message="Operation canceled.")
        return
    
def NetOptimization():
    autorization = mbox.askquestion(title="Confirmation",message="This will run some commands in your command line, do you want to continue?")
    if autorization == "yes":
        os.startfile(r"files\netoptimization.bat")
        return
    else:
        mbox.showinfo(title="FPS BOOSTER",message="Operation canceled.")
        return

def FortniteLowGraphics():
    autorization = mbox.askquestion(title="Confirmation",message="This will replace your GameUserSettings.ini, would you like to continue?")
    if autorization == "yes":
        gameSettingsPath = appdata+fr"\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"
        with open (fr"files\gameusersettingslow.txt","r") as read:
            content = read.read()
        with open(gameSettingsPath,"w") as w:
            w.write(content)
        mbox.showinfo(title="FPS BOOSTER",message="Operation finished!")
        return
    else:
        mbox.showinfo(title="FPS BOOSTER",message="Operation canceled.")
        return
    

tempWindow()