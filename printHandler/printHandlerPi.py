# Example of getting a list of printers
import cups
from PIL import Image
conn = cups.Connection()

def printImageArgox(image):
    printer_name = 'ARGOX_iX4-250_PPLB'
    conn.printFile(printer_name, image, "FlaskPrint", {})

def displayPrinter():
    conn = cups.Connection()
    printers = conn.getPrinters()
    for printer in printers:
        print(printer)
