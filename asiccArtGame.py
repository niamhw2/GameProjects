# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:22:37 2020

@author: niamh
"""

from PIL import Image

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
filepath = '''C:/Users/niamh/OneDrive/Documents/BasicCodeProjects/ASICC Art/PineappleImage.jpg'''
MAX_PIXEL_VALUE = 255

def getPixels(img,height):    
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def getBrightnessMatrix(data):
    intensity_matrix = []
    for row in data:
        intensity_row = []
        for c in row:
            average = (c[0] + c[1] + c[2])/3
            intensity_row.append(average)
    intensity_matrix.append(intensity_row) 
    return intensity_matrix  
            
def convertToAscii(brightnessArray, ascii):
    asciiMatrix = []
    for row in brightnessArray:
        ascii_row = []
        for p in row:
            ascii_row.append(ascii[int(p/MAX_PIXEL_VALUE * len(ascii)) - 1])
    asciiMatrix.append(ascii_row)
    return asciiMatrix

def printMatrix(asciiMatrix):
    for row in asciiMatrix:
        line = [p+p+p for p in row]
        print( "".join(line))


image = Image.open(filepath)
data = getPixels(image,1000)
brightnessArray = getBrightnessMatrix(data)
asciiMatrix = convertToAscii(brightnessArray, ascii)
printMatrix(asciiMatrix)

    


