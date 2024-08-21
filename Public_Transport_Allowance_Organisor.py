import sys
from pathlib import Path


def main():

    tesseract_path: str = "C:\Program Files\Tesseract"

    #todo: add tesseract to the PATH
    try:
        sys.path.append(str(Path(tesseract_path)))
        if tesseract_path in sys.path:
            print(f"Tesseract OCR directory has been successfully added to the PATH:"
                  f"\n{tesseract_path}")
        else:
            raise SystemError
    except SystemError:
        print("Failed to add Tesseract OCR to the system path.")
        sys.exit()

    receipt_path: str = " "

if __name__ == "__main__":
    main()



