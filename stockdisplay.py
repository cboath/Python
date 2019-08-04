#!/usr/bin/env python
import sys
import stockget
from xlrd import open_workbook
import time

from PIL import ImageFont

import inkyphat

inkyphat.set_colour("red")

nameFont = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 55)
priceFont = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 40)


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
        
        currPrice = stockget.getStock(name)
        
        myval = quant * medvalue
        totalval = quant * currPrice
        
        s = "%5.2f" % currPrice
        
        print('Neat! ', s)
        
        w, h = nameFont.getsize(name)

        # Center the text and align it with the name strip

        x = 20 #(inkyphat.WIDTH / 2)
        y = 20 - (h / 2)


        currX = 120
        currY = 30 - (h / 2)

        inkyphat.text((x, y), name, inkyphat.BLACK, nameFont)
        inkyphat.text((currX, currY), s, inkyphat.RED, priceFont)

        inkyphat.show()
        
        time.sleep(7)
        inkyphat.clear()

