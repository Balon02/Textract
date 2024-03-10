import tkinter as tk
from tkinter import StringVar, filedialog
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL import Image, ImageTk
from Page import Page
from Point import Point

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Text Trackt")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.first_corner = Point(0, 0)
        self.second_corner = Point(0, 0)
        self.image_path = r""
        self.page = Page("agreed.png", "eng")
        self.nameVar = StringVar()

        self.entryWidget = ctk.CTkEntry(self, placeholder_text="Drag and drop file here", height=50, width=150)
        self.entryWidget.grid(rowspan=3, columnspan=2, padx=5, pady=5)

        self.button_explore = ctk.CTkButton(self,
                                       text="Browse Files",
                                       command=self.browse_files)
        self.button_explore.grid(row=0, column=2, padx=5, pady=5)
        self.pathLabel = ctk.CTkLabel(self, text="Drag and drop file in the entry box")
        self.pathLabel.grid(row=1, column=4, padx=5, pady=5)

        self.entryWidget.drop_target_register(DND_ALL)
        self.entryWidget.dnd_bind("<<Drop>>", self.get_path)

        self.extractButton = ctk.CTkButton(self, text="Extract Text", command=self.example)
        self.extractButton.grid(row=1, column=2, padx=5, pady=5)

        self.extracted_text_option_1_label = ctk.CTkLabel(self, text="Extracted Text Option 1")
        self.extracted_text_option_1_label.grid(row=3, column=1, padx=5, pady=5)
        self.extracted_text_option_1 = ctk.CTkCanvas(self, width=300, height=200)

        self.extracted_text_option_1.grid_propagate(False)
        self.extracted_text_option_1.grid(rowspan=3, columnspan=3, row=4, column=0, padx=5, pady=5)
        self.extracted_text_option_2_label = ctk.CTkLabel(self, text="Extracted Text Option 1")
        self.extracted_text_option_2_label.grid(row=3, column=4, padx=5, pady=5)
        self.extracted_text_option_2 = ctk.CTkFrame(self, width=300, height=200, border_width=2, border_color="gray",
                                               fg_color="white")
        self.extracted_text_option_2.grid_propagate(False)
        self.extracted_text_option_2.grid(rowspan=3, columnspan=3, row=4, column=3, padx=5, pady=5)

        self.finishLabel = ctk.CTkLabel(self.extracted_text_option_1, text="")
        self.finishLabel.grid(row=0, column=0, padx=5, pady=5)

        self.button_bonus= ctk.CTkButton(self, text="Bonuses", command=lambda : self.selection_popup(self.page.width,self.page.height))
        self.button_bonus.grid(row=7,column=2, padx=5, pady=5)

    def get_path(self,event):
        self.image_path = event.data
        self.image_path = self.image_path.replace("{", "")
        self.image_path = self.image_path.replace("/", "\\")
        print(self.image_path)
        if self.image_path:
            self.page = Page(self.image_path, "eng")
        print(self.page)
        print(self.page.width, self.page.height)

    def example(self):
        text = self.page.extract_text()
        self.finishLabel.configure(text=text)



    def browse_files(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("all files", "*.*"), ("jpg", "*.jpg")))
        self.image_path = filename
        self.image_path = self.image_path.replace("{", "")
        print(self.image_path)
        if self.image_path:
            self.page = Page(self.image_path, "eng")
        self.pathLabel.configure(text=filename)

    def selection_popup(self, witdh, height):

        def coordinates_first(event):
            self.first_corner.x = event.x
            self.first_corner.y = event.y
            print(self.first_corner.x, self.first_corner.y)

        def coordinates_second(event):
            self.second_corner.x = event.x
            self.second_corner.y = event.y
            canvas.create_rectangle(self.first_corner.x, self.first_corner.y, self.second_corner.x,
                                        self.second_corner.y, outline="#fb0", fill="lightblue")
            print(self.second_corner.x, self.second_corner.y)
        win = ctk.CTkToplevel()
        win.attributes("-topmost", True)
        win.geometry(f"{witdh}x{height + 50}")
        canvas = tk.Canvas(win, width=witdh, height=height)
        canvas.grid(row=0, column=0)
        image = Image.open(self.image_path)
        img = tk.PhotoImage(image)
        canvas.create_image(0, 0, image=img, anchor="nw")
        win.bind("<Button-1>", coordinates_first)
        win.bind("<ButtonRelease-1>", coordinates_second)

        b = ctk.CTkButton(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0, padx=5, pady=5)





