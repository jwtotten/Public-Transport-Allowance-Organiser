import easyocr
import os

reader = easyocr.Reader(['en'])
result = reader.readtext(os.getcwd() + os.sep + ".." + os.sep + ".." + os.sep + 'Docs/Test_Images/TUI.png')

for (bbox, text, prob) in result:
    print(text)
