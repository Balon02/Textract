import os
from Page import Page

class Batch:
    def __init__(self, path):
        self.path = path
        self.pages = []
        self.output_folder = os.path.join(self.path, 'output_texts')
        os.makedirs(self.output_folder, exist_ok=True)
