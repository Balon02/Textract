from PIL import Image
import pytesseract
import os


def extract_text_from_images(folder_path, image_extensions):

    output_folder = os.path.join(folder_path, 'output_texts')
    os.makedirs(output_folder, exist_ok=True)

    image_files = [file for file in os.listdir(folder_path) if any(file.lower().endswith(ext.lower()) for ext in image_extensions)]
    print(image_files)
    for image_file in image_files:

        image_path = os.path.join(folder_path, image_file)

        text = pytesseract.image_to_string(Image.open(image_path), lang='eng', config='--psm 6')
        print(text)

        txt_file_name = f"{os.path.splitext(image_file)[0]}_text.txt"
        output_file_path = os.path.join(output_folder, txt_file_name)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)

        print(f"Text extracted from {image_file}. Saved to {txt_file_name}")


supported_formats = list(Image.registered_extensions().values())

pytesseract.pytesseract.tesseract_cmd = r'H:\Program Files\Tesseract-OCR\tesseract.exe'
# os.putenv('TESSDATA_PREFIX', r'H:\Program Files\tesseract languages\eng.traineddata')


# Example usage
folder_path = r'C:\Users\cooba\Documents\GitHub\Textract\OCR-tests'
extract_text_from_images(folder_path,supported_formats)