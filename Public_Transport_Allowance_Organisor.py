import sys
from Lib.Utils.Tesseract_OCR_Controller import Tesseract_Controller

def main():

    tesseract_path: str = "C:\Program Files\Tesseract"
    tesseract = Tesseract_Controller(tesseract_path)

    #todo: add tesseract to the PATH
    try:
        tesseract.add_tesseract_to_path()
    except SystemError:
        print("Failed to add Tesseract OCR to the system path.")
        sys.exit()

    receipt_path: str = " "

if __name__ == "__main__":
    main()



