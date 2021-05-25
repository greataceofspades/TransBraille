import cv2, time
import kivy
import argparse
import numpy as np
import PIL.ImageOps
import os
import requests
from matplotlib import pyplot as plt
from PIL import Image
from resizeimage import resizeimage


#Selecting and opening image file
def pre(path):
    img= cv2.imread(path,0)
    #Invert the image
    img = 255 - img
    ret, thresh = cv2.threshold(img, 110, 225, cv2.THRESH_BINARY)
    blur = cv2.blur(thresh,(5,5))
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(blur,kernel,iterations = 1)
    ret, thresh2 = cv2.threshold(erosion, 12, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,2),np.uint8)
    mask = cv2.dilate(thresh2,kernel,iterations = 1)
    rows,cols=mask.shape
    cv2.imwrite('image.png',mask)
    paths = "image.png"
    return paths

#Resizing image for excess spaces on splitted image
def resize2(path):
    with open(path, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [72, 99])
            cover.save(path, image.format)
    return path

#Splitting the splitted cells to 6
def cell(path): #split cell to 6 parts
    img = cv2.imread(path)
    dimensions = img.shape
    height = img.shape[0] 
    width = img.shape[1] 
    channels = img.shape[2] 
    x=0
    for r in range(0,img.shape[0],int(height/3)):
        for c in range(0,img.shape[1],int(width/2)):
            x=x+1
            cv2.imwrite(f"image{x}.png",img[r:r+int(height/3), c:c+int(width/2),:])           
    code=""
    for k in range(int(x)):
        k=k+1
        imgh = Image.open(f"image{k}.png")
        temp = Image.open('see.png')
        k = np.array(imgh)
        y = np.array(temp)
        if (k==y).all():
            code=code+"0"
        else:
            code=code+"1"
    
    f = open("code.txt", "a")
    
    if code == '000000':
        f.write("\n" + code + "\n")
    else:
        f.write(code + " ")
    f.close()
    return code

#Conversion of number code to alpha numeric keys
def numbers(string):
    word = ''
    if string == "100000":
        word = '1'
    if string == "110000":
        word = '2'
    if string == "100100":
        word = '3'
    if string == "100110":
        word = '4'
    if string == "100010":
        word = '5'
    if string == "110100":
        word = '6'
    if string == "110110":
        word = '7'
    if string == "110010":
        word = '8'
    if string == "010100":
        word = '9'
    if string == "010110":
        word = '0'
    word = word.strip()
    return word

def sletters(string):
    word = ''
    if string == "100000":
        word = 'a'
    if string == "101000":
        word = 'b'
    if string == "110000":
        word = 'c'
    if string == "110100":
        word = 'd'
    if string == "100100":
        word = 'e'
    if string == "111000":
        word = 'f'
    if string == "111100":
        word = 'g'
    if string == "101100":
        word = 'h'
    if string == "011000":
        word = 'i'
    if string == "011100":
        word = 'j'
    if string == "100010":
        word = 'k'
    if string == "101010":
        word = 'l'
    if string == "110010":
        word = 'm'
    if string == "110110":
        word = 'n'
    if string == "100110":
        word = 'o'
    if string == "111010":
        word = 'p'
    if string == "111110":
        word = 'q'
    if string == "101110":
        word = 'r'
    if string == "011010":
        word = 's'
    if string == "011110":
        word = 't'
    if string == "100011":
        word = 'u'
    if string == "101011":
        word = 'v'
    if string == "011101":
        word = 'w'
    if string == "110011":
        word = 'x'
    if string == "110111":
        word = 'y'
    if string == "100111":
        word = 'z'
    word = word.strip()
    return word

def punctuation(string):
    word = ''
    if string == "":
        word = ','
    if string == "":
        word = ';'
    if string == "":
        word = ':'
    if string == "":
        word = '.'
    if string == "":
        word = '!'
    if string == "":
        word = '('
    if string == "":
        word = ')'
    if string == "":
        word = '“'
    if string == "":
        word = '”'
    if string == "":
        word = '?'
    if string == "":
        word = '/'
    if string == "":
        word = '#'
    if string == "":
        word = '’'
    if string == "":
        word = '­'
    if string == "":
        word = '-'
    if string == "":
        word = '‐'
    if string == "":
        word = '‑'
    if string == "":
        word = '‒'
    if string == "":
        word = '–'
    if string == "":
        word = '—'
    if string == "":
        word = '―'
    word = word.strip()
    return word

def contracted(string):
    word = ''
    if string == "101000":
        word = 'bakit'
    if string == "110000":
        word = 'kanya'
    if string ==  "110100":
        word = 'dahil'
    if string == "111000":
        word = 'paano'
    if string == "111100":
        word = 'gaano'
    if string == "101100":
        word = 'hindi'
    if string == "011100":
        word = 'hakbang'
    if string == "100010":
        word = 'kaya'
    if string == "101010":
        word = 'lamang'
    if string == "110110":
        word = 'ngayon'
    if string ==  "111010":
        word = 'kailan'
    if string == "111110":
        word = 'rin'
    if string == "011010": 
        word = 'sang-ayon'
    if string == "011110":
        word = 'tayo'
    if string == "100011":
        word = 'upang'
    if string == "101011":
        word = 'bagamat'
    if string ==  "110011":
        word = 'ito'
    if string == "110111":
        word = 'yaman'
    if string == "100111":
        word = 'sa'
    if string == "111111":
        word = 'mahal'
    if string == "101111":
        word = 'hanggang'
    if string == "011101":
        word = 'wala'
    if string == "011000":
        word = 'ikaw'
    if string == "110010":
        word = 'mga'
    word = word.strip()
    return word

#Deleting images
def remove():
    os.remove("image.png")
    os.remove("code.txt")
    os.remove("converted.txt")
    os.remove("result.txt")
    sample = 6
    for x in range(sample):
        if (x<=125):
            x = x+1
            os.remove(f"image{x}.png")

#Deleting text
def removetxt():
    if (os.path.exists('code.txt')== "True"):
        os.remove("code.txt")
    if (os.path.exists('converted.txt')== "True"):
        os.remove("converted.txt")
    if (os.path.exists('result.txt')== "True"):
        os.remove("result.txt")
    
#Converting of numbers to text files
def singular(string):
    finalword = ""
    wordtemp = ""
    temp = ""
    x = 0
    word = string.split(" ")
    for words in word:
        wordtemp = ""
        if word[x-1] == "000001":                                               #capital symbol
            wordtemp = sletters(word[x]).upper()
            finalword = finalword + wordtemp
            x = x+1
            continue
        if word[x-1] == "001111":                                               #number symbol
            wordtemp = numbers(word[x])
            finalword = finalword + wordtemp
            x = x+1
            continue
        else:
            wordtemp = sletters(word[x])
            finalword = finalword + wordtemp
        x = x+1
    finalword = finalword+ " "
    return finalword

#Adding an enter line
def algo():
    f = open ("code.txt", "r")
    listOfLines = f.readlines()
    f.close()
    f = open("converted.txt", "a")
    wordtext = ""
    for line in listOfLines:
        wordtext = ""
        if line.strip() == "000000":
            f.write("")
        if line.strip() == "":
            f.write("")
        wordtext = wordtext + contracted(line.strip())
        if wordtext == "":
            wordtext = wordtext + singular(line.strip())
        f.write(wordtext + "\n")
    f.close()

#Displaying of result
def result():
    f = open ("result.txt", "r")
    listOfLines = f.readlines()
    print (listOfLines)
    f.close()
    
#Removing excess spaces
def spaces():
    f = open ("converted.txt", "r")
    listOfLines = f.readlines()
    f.close()
    f = open("result.txt", "a")
    wordtext = ""
    for line in listOfLines:
        if line.strip() != "":
            f.write(line.strip() + " ")           
    f.close()

#main code
array = ['array from john']         #accepting and storing of array
removetxt()                         #removing txtfiles
word = []                           #Storing array for the write
for x in array:
    r = requests.get(x, allow_redirects=True)
    open('imagedl.png', 'wb').write(r.content)
    path = 'imagedl.png'
    imgprc = pre(path)              #Black and white process
    trial = resize2(imgprc)         #resizing
    conv = cell(trial)              #Splitting image to 6
    word.append(conv)               #Adding the new letter to the word
algo()                              #Adding new line
spaces()                            #Removing excess spaces
result()                            #Displaying of results  
remove()                            #removing image files
