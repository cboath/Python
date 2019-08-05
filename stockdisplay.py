#!/usr/bin/env python
import stockget
from xlrd import open_workbook
import time

from PIL import ImageFont

import inkyphat

inkyphat.set_colour("red")

nameFont = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 55)
priceFont = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 40)
ownsFont = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 30)

while True:
    wb = open_workbook('mystocks.xls')
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        items = []

        rows = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value  = (sheet.cell(row,col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
                    
            name = values[0]
            quant = values[1]
            medvalue = values[2]
            
            intquant = int(quant)
            mvf = float(medvalue)
            
            currPrice = stockget.getStock(name)
            
            myval = intquant * mvf
            totalval = intquant * currPrice
            
            
            
            GT = 'BLACK'
            LT = 'inkyphat.RED'
            
            s = "%5.2f" % currPrice
            t = "%5.2f" % totalval
            u = "--------------------"
            
            print('Neat! ', s)
            
            w, h = nameFont.getsize(name)

            x = 20 #(inkyphat.WIDTH / 2)
            y = 20 - (h / 2)


            currX = 120
            currY = 30 - (h / 2)

            inkyphat.text((x, y), name, inkyphat.BLACK, nameFont)
            inkyphat.text((currX, currY), s, inkyphat.RED, priceFont)
            inkyphat.text((50, 60), quant, inkyphat.BLACK, ownsFont)
            inkyphat.text((120, 60), t, inkyphat.RED, ownsFont)
            inkyphat.text((0, 35), u, inkyphat.BLACK, ownsFont)

            inkyphat.show()
            
            time.sleep(7)
            inkyphat.clear()



