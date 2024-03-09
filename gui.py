import tkinter as tk
from tkinter import StringVar, TOP, filedialog
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL import Image, ImageTk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

first_corner = Point(0, 0)
second_corner = Point(0, 0)
class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
def get_path(event):
    pathLabel.configure(text = event.data)

def example():
    finishLabel.configure(text = "Text extracted!")

def coordinates_first(event):
    first_corner.x = event.x
    first_corner.y = event.y
    print(first_corner.x, first_corner.y)
def coordinates_second(event):
    second_corner.x = event.x
    second_corner.y = event.y
    extracted_text_option_1.create_rectangle(first_corner.x, first_corner.y, second_corner.x, second_corner.y,
                                             outline="#fb0", fill="lightblue")
    print(second_corner.x, second_corner.y)
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("all files","*.*"),("jpg","*.jpg")))
    pathLabel.configure(text = filename)
def selection_popup(witdh,height):
    win = ctk.CTkToplevel()
    win.attributes("-topmost", True)
    win.geometry(f"{witdh}x{height}")
    cos = Image.open("agreed.png")
    img = ctk.CTkImage(cos,size=(witdh,witdh))
    label1 = ctk.CTkLabel(win,image=img)
    label1.image = img
    label1.grid(row=0,column=0)
    win.bind("<Button-1>", coordinates_first)
    win.bind("<ButtonRelease-1>", coordinates_second)

    b = ctk.CTkButton(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)

#Ssytem Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Our app
root = Tk()
root.geometry("640x480")
root.title("Text Trackt")


#UI Elements
#title = ctk.CTkLabel(root, text="Text Trackt", font=("Arial", 20))
#title.pack(pady=10,padx=10)

nameVar = StringVar()

entryWidget = ctk.CTkEntry(root, placeholder_text="Drag and drop file here", height=50,width=150)
entryWidget.grid(rowspan=3,columnspan=2, padx=5, pady=5)

button_explore = ctk.CTkButton(root,
                        text = "Browse Files",
                        command = browseFiles)
button_explore.grid(row=0,column=2, padx=5, pady=5)
pathLabel = ctk.CTkLabel(root, text="Drag and drop file in the entry box")
pathLabel.grid(row=1,column=4, padx=5, pady=5)

entryWidget.drop_target_register(DND_ALL)
entryWidget.dnd_bind("<<Drop>>", get_path)

extractButton = ctk.CTkButton(root, text="Extract Text", command=example)
extractButton.grid(row=1,column=2, padx=5, pady=5)

extracted_text_option_1_label = ctk.CTkLabel(root, text="Extracted Text Option 1")
extracted_text_option_1_label.grid(row=3,column=1, padx=5, pady=5)
extracted_text_option_1 = ctk.CTkCanvas(root, width=300, height=200)
extracted_text_option_1.bind("<Button-1>", coordinates_first)
extracted_text_option_1.bind("<ButtonRelease-1>", coordinates_second)

extracted_text_option_1.grid_propagate(False)
extracted_text_option_1.grid(rowspan=3,columnspan=3,row=4,column=0, padx=5, pady=5)
extracted_text_option_2_label = ctk.CTkLabel(root, text="Extracted Text Option 1")
extracted_text_option_2_label.grid(row=3,column=4, padx=5, pady=5)
extracted_text_option_2 = ctk.CTkFrame(root, width=300, height=200,border_width=2,border_color="gray",fg_color="white")
extracted_text_option_2.grid_propagate(False)
extracted_text_option_2.grid(rowspan=3,columnspan=3,row=4,column=3, padx=5, pady=5)

finishLabel = ctk.CTkLabel(extracted_text_option_1, text="")
finishLabel.grid(row=0,column=0, padx=5, pady=5)

button_bonus = ctk.CTkButton(root, text="Bonuses", command=lambda : selection_popup(300,300))
button_bonus.grid(row=7,column=2, padx=5, pady=5)

#Run app
root.mainloop()