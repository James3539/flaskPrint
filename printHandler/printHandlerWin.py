import os
import win32print
import win32ui
from PIL import Image, ImageWin


def printImageArgox(image):
    bmp = Image.open(image)
    bmp = bmp.transpose(Image.ROTATE_180)
    print('Image Size:',bmp.size)
    printer_name = 'Argox iX4-250 PPLB'
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    printable_area = hDC.GetDeviceCaps(8), hDC.GetDeviceCaps(10)
    printer_size = hDC.GetDeviceCaps(110), hDC.GetDeviceCaps(111)
    hDC.StartDoc('tempPrintDoc')
    hDC.StartPage()
    dib = ImageWin.Dib(bmp)
    dib.draw(hDC.GetHandleOutput(),(0,0,printer_size[0],printer_size[1]))
    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()
    print('Image Printed')
    removeImage(image)


def removeImage(image):
    os.remove(image)

def listPrinters():
    printers = win32print.EnumPrinters(2)
    for printer in printers:
        print(printer)

