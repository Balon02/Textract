from PIL import Image
import pytesseract
import os


class Text:
    def __init__(self, path, lang):
        self.path = path
        self.lang = lang
        self.text = pytesseract.image_to_string(Image.open(path), lang=lang, config='--psm 6')