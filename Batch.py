import os
from Page import Page

class Batch:
    def __init__(self, path):
        self.path = path
        self.pages = []
        self.output_folder = os.path.join(self.path, 'output_texts')
        os.makedirs(self.output_folder, exist_ok=True)

    def load_pages(self, lang):
        images = [file for file in os.listdir(self.path)]
        for image in images:
            image_path = os.path.join(self.path, image)
            page = Page(image_path, lang)
            self.pages.append(page)

    def save_pages(self):
        for page in self.pages:
            text = page.extract_text()
            txt_file_name = f"{os.path.splitext(page.path)[0]}_text.txt"
            output_file_path = os.path.join(self.output_folder, txt_file_name)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            print(f"Text extracted from {page.path}. Saved to {txt_file_name}")
