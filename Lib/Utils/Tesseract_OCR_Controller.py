import os
import sys
from pathlib import Path
import pytesseract
from PIL import Image


class Tesseract_Controller:

    def __init__(self, tesseract_path_dir: str):
        self.tesseract_path_dir = tesseract_path_dir

    def add_tesseract_to_path(self) -> None:
        """
        Adding the directory for Tesseract OCR to the system environment variables path.
        :return: None
        """
        # adding tesseract directory to the system environment variables using Path
        sys.path.append(str(Path(self.tesseract_path_dir)))
        if self.tesseract_path_dir in sys.path:
            print(f"Tesseract OCR directory has been successfully added to the PATH:"
                  f"\n{self.tesseract_path_dir}")
        else:
            raise SystemError

        # adding tesseract directory to the system environment variables using os
        os.environ["TESSDATA_PREFIX"] = self.tesseract_path_dir + os.sep + "tessdata"

        pytesseract.pytesseract.tesseract_cmd = self.tesseract_path_dir

    @staticmethod
    def perform_ocr(image: Image) -> str:
        """
        Takes an PIL image object and performs the OCR with Tesseract.
        :param image: Image, PIL Image object that is to be passed to Tesseract.
        :return: str, Returns the text contained in the given image.
        """
        return pytesseract.image_to_string(image)
