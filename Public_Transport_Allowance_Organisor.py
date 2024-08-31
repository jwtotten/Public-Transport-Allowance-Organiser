import sys
from Lib.Utils.Tesseract_OCR_Controller import Tesseract_Controller
from PIL import Image


def main():
    tesseract_path: str = "C:\Program Files\Tesseract-OCR"
    tesseract = Tesseract_Controller(tesseract_path)

    try:
        tesseract.add_tesseract_to_path()
    except SystemError:
        print("Failed to add Tesseract OCR to the system path.")
        sys.exit()

    receipt_path: str = "Docs/Test_Images/TUI.png"
    img: Image = Image.open(receipt_path)

    image_text = tesseract.perform_ocr(Image.open(receipt_path))
    print(image_text)


if __name__ == "__main__":
    main()
