import ctypes
import subprocess
import time
import customtkinter
from PIL import Image
import tkinter.messagebox as mbox
import os
import shutil
import pyuac
import requests
from io import BytesIO

def GetImages(url): # This function is used to download the images stored online
    image_url = url
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        mbox.showerror(title="FPS BOOSTER",message="Failed to retrieve data. Contact owner")
        exit()

appdata = os.getenv('LOCALAPPDATA') # Program configurations
temp = os.getenv('TEMP')
radius = 20                         # Program configurations                          
canSwitch = True                    # Program configurations
i = 0                               # Program configurations

def windowConfig(window,x,y): # Window Configuration for Code Efficiency
    window.eval('tk::PlaceWindow . center')
    window.maxsize(x,y)
    window.minsize(x,y)
    window.overrideredirect(True)
    window.title('FPS BOOSTER')

def set_window_shape(window, radius): # Window with round corners
        hwnd = window.winfo_id()
        window.update_idletasks()
        
        region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, window.winfo_width(), window.winfo_height(), radius, radius)
        ctypes.windll.user32.SetWindowRgn(hwnd, region, True)

def tempWindow(): # Temporary window to load all assets (Loading Screen)
    global offImage

    offImage = GetImages("https://i.ibb.co/P4sDBP1/off.png")
    logo = customtkinter.CTkImage(GetImages("https://i.ibb.co/305xDz7/Logo.png"), size=(100, 100))

    def UpdateW():
         Main(tempw)

    tempw = customtkinter.CTk()
    windowConfig(tempw,300,300)

    displaylogo = customtkinter.CTkLabel(tempw,height=200,width=200,image=logo,text="")
    displaylogo.place(x=50,y=5)

    progressbar = customtkinter.CTkProgressBar(tempw, orientation="horizontal",mode="indeterminate",indeterminate_speed=4,corner_radius=3)
    progressbar.place(x=50,y=200)
    progressbar.start()
    
    set_window_shape(tempw, radius)
    tempw.after(1500,UpdateW)
    tempw.mainloop()

def SwitchMode(): # Switch used for Night/Light mode
    global canSwitch,i
    currentSelection = bgswitch.get()

    def NoSpam(): # Color Gradiation for Code Efficiency
        border.configure(bg_color=color_code)
        cleanMemoryButton.configure(bg_color=color_code)
        netOptimizeButton.configure(bg_color=color_code)
        fortniteLow.configure(bg_color=color_code)
        fortniteLowLabel.configure(bg_color=color_code)
    
    if canSwitch:
        canSwitch = False
        if i != 85:
            for i in range(260,80,-5):
                color_code = "#{:02X}{:02X}{:02X}".format(i, i, i)
                NoSpam()
                root.update()
                time.sleep(0.01)
            if i == 85: 
                NoSpam()
                root.update()
                canSwitch = True
        else:
            for i in range(80,260,5):
                    color_code = "#{:02X}{:02X}{:02X}".format(i, i, i)
                    NoSpam()
                    root.update()
                    time.sleep(0.01)
            if i == 255: 
                NoSpam()
                root.update()
                canSwitch = True
    else:
        bgswitch.select(currentSelection)

def Main(tempw): # Main Window
    global root,bgswitch
    tempw.destroy()
    root = customtkinter.CTk()
    windowConfig(root,400,300)
    LoadLabels(root)
    set_window_shape(root, radius)
    root.mainloop()

def LoadLabels(root): # Load all labels inside the main window
    global bgswitch,border,cleanMemoryButton,netOptimizeButton,fortniteLow,fortniteLowLabel 
    def start_drag(event): #Drag window by the custom title bar
            global x,y
            x = event.x
            y = event.y
    def move_window(event): #Drag window by the custom title bar
        new_x = (root.winfo_x() + event.x) - x
        new_y = (root.winfo_y() + event.y) - y
        root.geometry(f"+{new_x}+{new_y}")
    
    border = customtkinter.CTkFrame(root,400,300,border_color="lightblue",border_width=4,bg_color="white",fg_color="transparent")

    title_bar = customtkinter.CTkFrame(root,height=25,width=800,bg_color="lightblue",fg_color="lightblue")
    titleLabel = customtkinter.CTkLabel(root,text="FPS BOOSTER",font=("Arial Baltic",17),height=25,text_color="black",bg_color="lightblue",fg_color="transparent")
    title_bar.bind("<ButtonPress-1>",start_drag)
    title_bar.bind("<B1-Motion>",move_window)
    titleLabel.bind("<ButtonPress-1>",start_drag)
    titleLabel.bind("<B1-Motion>",move_window)

    bgswitch = customtkinter.CTkSwitch(root,corner_radius=10,text="",bg_color="lightblue",button_color="grey",fg_color="white",progress_color="black",command=SwitchMode)
    off = customtkinter.CTkImage(offImage, size=(15, 15))
    close_button = customtkinter.CTkButton(root,text="",image=off,bg_color="lightblue",fg_color="lightblue",hover_color="lightblue",width=10,height=10,command=root.destroy,font=("verdana bold",15))
    cleanMemoryButton = customtkinter.CTkButton(root,text = "Optimize Windows ",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",corner_radius=9,command=Optimization)
    netOptimizeButton = customtkinter.CTkButton(root,text = "Optimize Internet  ",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",corner_radius=9,command=NetOptimization)
    tempFilesRemover = customtkinter.CTkButton(root,text = "Clear Temp Files   ",font=("verdana",15),text_color="black",fg_color="lightblue",hover_color="white",corner_radius=9,command=TempRemover)
    fortniteLow = customtkinter.CTkButton(root,text = "Optimize Fortnite",font=("verdana",15),text_color="black",fg_color="lightblue",bg_color="transparent",hover_color=None,corner_radius=9,command=FortniteLowGraphics)
    fortniteLowLabel = customtkinter.CTkLabel(root,text="(low graphics)",font=("verdana",12),text_color="grey",bg_color="transparent",fg_color="transparent")
  
    border.place(x=0,y=0)
    title_bar.place(x=0,y=0)
    bgswitch.place(x=10,y=0)
    close_button.place(x=370,y=0)
    titleLabel.place(x=150,y=0)
    cleanMemoryButton.place(x=30,y=70)
    netOptimizeButton.place(x=30,y=125)
    tempFilesRemover.place(x=30,y=180)
    fortniteLowLabel.place(x=255,y=40)
    fortniteLow.place(x=230,y=70)

def OptimizationNoSpam(url): # Optimization for Code Efficiency
    autorization = mbox.askquestion(title="Confirmation",message="This will run some commands in your command line, do you want to continue?")
    if autorization == "yes":
        response = requests.get(url)
        if response.status_code == 200:
            text_data = response.text
            with open (fr"temp.bat","w") as temp:
                temp.write(text_data)
                time.sleep(0.2)
        else:
            mbox.showerror(title="FPS BOOSTER",message="Failed to retrieve data. Contact owner")
            return
        os.startfile(fr"temp.bat")
        return
    else:
        mbox.showinfo(title="FPS BOOSTER",message="Operation canceled.")
        return
    
def Optimization(): # Windows Optimization
    OptimizationNoSpam("https://pastebin.com/raw/ba14Y15t")
    
def NetOptimization(): # Internet Optimization
    OptimizationNoSpam("https://pastebin.com/raw/Wvj1HDSi")

def TempRemover(): # Removes all temporary files
    for file in os.listdir(temp):
        try:
            
            shutil.rmtree(temp+fr"\\"+file)
        except:
            continue
    for file in os.listdir(temp):
        try:
            os.remove(temp+fr"\\"+file)
        except:
            continue
    mbox.showinfo("FPS BOOSTER","Operation Finished.")

def FortniteLowGraphics(): # Fortnite Optimization
    autorization = mbox.askquestion(title="Confirmation",message="This will replace your GameUserSettings.ini, would you like to continue?")
    if autorization == "yes":
        gameSettingsPath = appdata+fr"\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"
        pastebin_url = "https://pastebin.com/raw/DCNnK2J8"
        response = requests.get(pastebin_url)
        if response.status_code == 200:
            text_data = response.text
        else:
            mbox.showerror(title="FPS BOOSTER",message="Failed to retrieve data. Contact owner")
            return
        try:
            with open(gameSettingsPath,"w") as w:
                w.write(text_data)
        except FileNotFoundError:
            mbox.showerror(title="FPS BOOSTER",message="Fortnite GameUserSettings.ini not found. Check fortnite instalation..")
            return
        mbox.showinfo(title="FPS BOOSTER",message="Operation finished!")
        return
    else:
        mbox.showinfo(title="FPS BOOSTER",message="Operation canceled.")
        return

 
if __name__ == "__main__":
    if pyuac.isUserAdmin():
        tempWindow()
    else:
        pyuac.runAsAdmin()

