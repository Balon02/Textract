import cv2
import pytesseract
import uuid


pytesseract.pytesseract.tesseract_cmd = r'H:\Program Files\Tesseract-OCR\tesseract.exe'


class Page:
    def __init__(self, path, lang):
        self.id = str(uuid.uuid4())
        self.path = path
        self.lang = lang
        try:
            self.image = cv2.imread(self.path)
            self.height = self.image.shape[0]
            self.width = self.image.shape[1]
        except Exception as e:
            self.image = None
            self.height = 0
            self.width = 0

    def text_cutout(self, cordx1, cordx2, cordy1, cordy2):
        self.image = self.image[cordy1:cordy2, cordx1:cordx2]
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]

    def extract_text(self):
        return pytesseract.image_to_string(self.image, lang=self.lang, config='--psm 6')

    def review_text(self):
        #add review function using chosen API later
        return 0

