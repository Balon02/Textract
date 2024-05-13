import cv2
import pytesseract
import uuid
import pyperclip
import numpy as np
import io
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\chope\Desktop\Tesseract\tesseract.exe'


class Page:
    def __init__(self, path, lang):
        self.id = str(uuid.uuid4())
        self.path = path
        self.lang = lang
        self.image = cv2.imread(self.path)
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]

    def text_cutout(self, cordx1, cordx2, cordy1, cordy2):
        self.image = self.image[cordy1:cordy2, cordx1:cordx2]
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]

    def extract_text(self):
        print(pytesseract.image_to_string(self.image, lang=self.lang, config='--psm 6'))
        return pytesseract.image_to_string(self.image, lang=self.lang, config='--psm 6')

    def review_text(self):
        #add review function using chosen API later
        return 0

    def clipboard_to_string(self):
        clipboard_content = pyperclip.paste()

        # Check if clipboard contains an image
        if "image" in clipboard_content.lower():
            try:
                image = Image.open(io.BytesIO(clipboard_content))
                image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                extracted_text = self.extract_text(image_cv)
                return extracted_text
            except Exception as e:
                print("Error:", e)
                return None
        else:
            print("Clipboard does not contain an image.")
            return None