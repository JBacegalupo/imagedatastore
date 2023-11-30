from PIL import Image as image
import PIL
import binascii
from textwrap import wrap
x = 0
y = 0
binnum = ""
finaltext = ""
colourdictionary = {
    "0,0,0" : "Pass",
    "0,0,1" : "0000",
    "0,1,1" : "0001",
    "1,1,1" : "0010",
    "1,1,2" : "0011",
    "1,2,1" : "0100",
    "2,1,1" : "0101",
    "2,1,2" : "0110",
    "2,2,2" : "0111",
    "2,2,3" : "1000",
    "2,3,2" : "1001",
    "3,2,2" : "1010",
    "3,2,3" : "1011",
    "3,3,3" : "1100",
    "3,3,4" : "1101",
    "3,4,3" : "1110",
    "4,3,3" : "1111"
}





def imagedecrypt():
    global binnum
    global x
    global y
    with image.open("C:\\Users\\Jay bodger\\Desktop\\HiddenData.tiff") as im:
        pixels = im.load()
        for j in range(im.size[0]):
            for i in range(im.size[1]):
                #print(im.getpixel((i,j)))
                #print(f"X:{i},Y:{j}")
                if im.getpixel((i,j)) == (0, 0, 0):
                    RgbDecrypt()
                else:
                    binnum += colourdictionary[str(im.getpixel((i,j))).strip("( ) ").replace(" ","")]
                    print(binnum)
                    if len(binnum) % 8 == 0:
                        RgbDecrypt(binnum)
                        binnum = ""

    RgbDecrypt()

def RgbDecrypt(BinChar = None):
    global finaltext
    if BinChar == None:
        print(finaltext)
        exit()
    else:
        n = int((BinChar), 2)
        finaltext += n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()



def imgprocessing(colour):
    global x
    global y
    colour = colour.split(",")
    with image.open("C:\\Users\\Jay bodger\\Desktop\\HiddenData.tiff") as im:
        pixels = im.load()
        print (colour)
        pixels[x,y] = (int(colour[0]), int(colour[1]),int(colour[2]))
        if x != im.size[0]:
            x += 1
            print(f"X:{x} , Y:{y}")
        else:
            y +=1
            x = 0
    im.save("C:\\Users\\Jay bodger\\Desktop\\HiddenData.tiff")

def canvascreation():
    im = PIL.Image.new(mode="RGB", size=(2000, 2000))
    im.save("C:\\Users\\Jay bodger\\Desktop\\HiddenData.tiff")


def coversionandcolourlinking(userinput):
    for element in userinput:
        bineq = f"{ord(element):08b}"
        bineqlst = wrap(bineq, 4)
        for index in range(0,2):
            imgprocessing(list(colourdictionary.keys())[list(colourdictionary.values()).index(bineqlst[index])])
    pass

if __name__ == '__main__':

    #canvascreation()
    #userinput = input("Please enter a string to be encrypted: ")


    #coversionandcolourlinking(userinput)
    imagedecrypt()