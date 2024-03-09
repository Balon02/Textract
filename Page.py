import cv2
import pytesseract
import os
import uuid


pytesseract.pytesseract.tesseract_cmd = r'H:\Program Files\Tesseract-OCR\tesseract.exe'


class Page:
    def __init__(self, path, lang):
        self.id = str(uuid.uuid4())
        self.path = path
        self.lang = lang
        self.image = cv2.imread(self.path)

    def text_cutout(self, cordx1, cordx2, cordy1, cordy2):
        self.image = self.image[cordy1:cordy2, cordx1:cordx2]

    def extract_text(self):
        return pytesseract.image_to_string(self.image, lang=self.lang, config='--psm 6')

    def review_text(self):
        #add review function using chosen API later
        return 0

