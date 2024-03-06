import tkinter as tk
from tkinter import StringVar, TOP, filedialog
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL


class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
def get_path(event):
    pathLabel.configure(text = event.data)

def example():
    finishLabel.configure(text = "Text extracted!")


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("all files","*.*"),("jpg","*.jpg")))
    pathLabel.configure(text = filename)

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
extracted_text_option_1 = ctk.CTkFrame(root, width=300, height=200,border_width=2,border_color="gray",fg_color="white")
extracted_text_option_1.grid_propagate(False)
extracted_text_option_1.grid(rowspan=3,columnspan=3,row=4,column=0, padx=5, pady=5)

extracted_text_option_2_label = ctk.CTkLabel(root, text="Extracted Text Option 1")
extracted_text_option_2_label.grid(row=3,column=4, padx=5, pady=5)
extracted_text_option_2 = ctk.CTkFrame(root, width=300, height=200,border_width=2,border_color="gray",fg_color="white")
extracted_text_option_2.grid_propagate(False)
extracted_text_option_2.grid(rowspan=3,columnspan=3,row=4,column=3, padx=5, pady=5)

finishLabel = ctk.CTkLabel(extracted_text_option_1, text="")
finishLabel.grid(row=0,column=0, padx=5, pady=5)


#Run app
root.mainloop()