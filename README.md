# Textract

# Text Extractor

## Overview

Text Extractor is a handy utility that allows users to select an area on their monitor and extract the text within that area. The extracted text is then automatically copied to the clipboard for immediate use. This tool is perfect for quickly capturing text from images, PDFs, videos, or any other on-screen content that isn't easily selectable.

## Features

- **Area Selection**: Select a rectangular area on your screen to capture the text.
- **Text Recognition**: Use OCR (Optical Character Recognition) to extract text from the selected area.
- **Clipboard Integration**: Automatically copies the extracted text to your clipboard.
- **User-Friendly Interface**: Simple and intuitive interface for ease of use.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/TextExtractor.git
    cd TextExtractor
    ```

2. **Install dependencies:**
    Ensure you have Python installed, then install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Tesseract OCR:**
    Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract). Make sure to add Tesseract to your system path.

4. **Run the application:**
    ```bash
    python main.py
    ```

## Usage

1. **Launch the application:**

2. **Select the area:**
Use the mouse to draw a rectangle around the area on your screen from which you want to extract text.

3. **Extract and copy text:**
The text within the selected area will be extracted using OCR and automatically copied to your clipboard.

##**Dependencies**
```bash
Python 3.6+
PyQt5 (for GUI)
Pillow (for image processing)
Pytesseract (Python wrapper for Tesseract OCR)
OpenCV (for advanced image processing)
```
##**Contributing**
We welcome contributions! If you have suggestions for improvements or have found bugs, please open an issue or submit a pull request. Make sure to follow the contribution guidelines.

##**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

##**Contact** 
For any questions or feedback, feel free to reach out:

**GitHub:** PawWin, Balon02

##Thank you for using Text Extractor! We hope it makes your text extraction tasks easier and more efficient.
