from bs4 import BeautifulSoup
from flask import render_template
import imgkit
import time
from printHandler import printHandlerPi

def renderHTML(data):
    LabelName = data['LabelName']
    html = render_template(LabelName)
    addTextFromJSON(html, data)

def addTextFromJSON(html, data):
    soup = BeautifulSoup(html, 'html.parser')
    for e, i in data.items():
        try:
           elm = soup.find_all(id=e)
           for eelms in elm:
                eelms.clear()
                eelms.append(i)
        except Exception as e:
            print(e)
        finally:
            pass
    if 'ARGOX_iX4-250_PPLB' == data['Printer']:
        printImageArgox(str(soup))
    else:
        printImageOther(html)

def printImageArgox(html):
    tme = int(time.time())
    img_file_name = '/home/pi/flaskprint/images/' + str(tme) + '.bmp'
    options = {'format': 'bmp', 'width': '1421', 'disable-smart-width': '', 'height': '735'}
    imgkit.from_string(html, img_file_name , options=options)
    printHandlerPi.printImageArgox(img_file_name)

def printImageOther(html):
    tme = int(time.time())
    img_file_name = '/home/pi/flaskprint/images/' + str(tme) + '.bmp'
    options = {'format': 'bmp', 'width': '820', 'disable-smart-width': '', 'height': '650'}
    imgkit.from_string(html, img_file_name, options=options)

