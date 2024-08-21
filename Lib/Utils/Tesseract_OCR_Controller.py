import sys
from pathlib import Path


class Tesseract_Controller:

    def __init__(self, tesseract_path_dir: str):
        self.tesseract_path_dir = tesseract_path_dir

    def add_tesseract_to_path(self) -> None:
        """
        Adding the directory for Tesseract OCR to the system environment variables path.
        :return: None
        """
        sys.path.append(str(Path(self.tesseract_path_dir)))
        if self.tesseract_path_dir in sys.path:
            print(f"Tesseract OCR directory has been successfully added to the PATH:"
                  f"\n{self.tesseract_path_dir}")
        else:
            raise SystemError
