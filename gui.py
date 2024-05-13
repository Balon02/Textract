import tkinter as tk
import customtkinter as ctk
import pyperclip
import keyboard
import time
from cos import extract_text_from_clipboard
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Texttract")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.text_var = tk.StringVar()
        self.text_var.set("Hello World")
        self.textbox = ctk.CTkTextbox(master=self, width=590, height=300, font=("Arial", 12),corner_radius=0)
        self.textbox.grid(row=0, column=0, padx=20, pady=20)
        self.textbox.insert("0.0",f"{self.text_var.get()}")

        self.button = ctk.CTkButton(self, text="Copy To Clipboard", command=self.copy_to_clipboard)
        self.button.grid(row=1, column=0, padx=20, pady=20)

        keyboard.on_press_key("Print Screen", self.shortcut_press)

    def copy_to_clipboard(self):
        pyperclip.copy(self.text_var.get())
        print("Copied to clipboard")

    def shortcut_press(self, event):
        try:
            time.sleep(5)
            result_text = extract_text_from_clipboard()
            self.text_var.set(result_text)
            self.textbox.delete("0.0", tk.END)
            self.textbox.insert("0.0", f"{self.text_var.get()}")
        except Exception as e:
            print("Failed to capture screenshot")
    def remap_key(self):
        keyboard.remap_key(44, "win+shift+s")
        keyboard.wait()

def main():
    app = App()
    app.mainloop()