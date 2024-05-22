import tkinter as tk
import customtkinter as ctk
import pyperclip
import keyboard
from Page import clipboard_to_string
from pynput import mouse
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Texttract")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.text_var = tk.StringVar()
        self.text_var.set("Tutaj Wyświetli się tekst z obrazu")
        self.textbox = ctk.CTkTextbox(master=self, width=590, height=300, font=("Arial", 12),corner_radius=0)
        self.textbox.grid(row=0, column=0, padx=20, pady=20)
        self.textbox.insert("0.0",f"{self.text_var.get()}")

        self.button = ctk.CTkButton(self, text="Copy To Clipboard", command=self.copy_to_clipboard)
        self.button.grid(row=1, column=0, padx=20, pady=20)

        keyboard.add_hotkey("print screen", lambda: keyboard.send("win+shift+s"))
        self.mouse_listener = mouse.Listener(on_click=self.mouse_press)
        self.mouse_listener.start()


    def copy_to_clipboard(self):
        pyperclip.copy(self.text_var.get())
        print("Copied to clipboard")

    def mouse_press(self, x, y, button, pressed):
        if button == mouse.Button.left and not pressed:
            try:
                result_text = clipboard_to_string()
                self.text_var.set(result_text)
                self.textbox.delete("0.0", tk.END)
                self.textbox.insert("0.0", f"{self.text_var.get()}")
            except Exception as e:
                print("Failed to capture screenshot")


def main():
    app = App()
    app.mainloop()