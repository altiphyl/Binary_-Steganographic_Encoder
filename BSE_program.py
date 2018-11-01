from PIL import Image
#test

img = Image.open(input("Input directory: "))

data = input("Type message: ")

imagePixelData = img.getdata()

def binaryData(data):
    dataArray = []

    for i in data:
        dataArray.append(format(ord(i), "08b"))

    return (dataArray)


def modPixelarrayHelper(dataArray, newlist):    # needs to be fixed rn only 7 ormore characters can be encrypted
    i = 0
    j = 0
    tempnewlist = newlist

    while i < ((len(dataArray) + 1) * 8):
        tempnewlist[i] = dataArray[j][0]
        tempnewlist[i + 1] = dataArray[j][1]
        tempnewlist[i + 2] = dataArray[j][2]
        tempnewlist[i + 3] = dataArray[j][3]
        tempnewlist[i + 4] = dataArray[j][4]
        tempnewlist[i + 5] = dataArray[j][5]
        tempnewlist[i + 6] = dataArray[j][6]
        tempnewlist[i + 7] = dataArray[j][7]
        tempnewlist[i + 8] = 5
        i = i + 9

        if j == 6:
            break
        else:
            j = j + 1

    return tempnewlist


def pixelModifier(imagePixelData, dataArray):
    imagePixelDataLen = len(imagePixelData)

    # converting pixel data in groups of three to one single list
    singleDataList = []

    for i in range(0, imagePixelDataLen):
        for j in range(0, len(imagePixelData[0])):
            singleDataList.append(imagePixelData[i][j])

    # encoding binary data into pixel data
    binPixeldata = modPixelarrayHelper(dataArray, singleDataList)

    # converting modified pixel data in single form to pixel format
    l = 0
    modpixeldata = []

    while l < (len(binPixeldata) - (len(imagePixelData[0]) - 1)):
        templist2 = []
        for m in range(0, len(imagePixelData[0])):
            templist2.append(int(binPixeldata[l + m]))

        modpixeldata.append(tuple(templist2))
        l = l + (len(imagePixelData[0]))

    return modpixeldata


def encode_enc(dataArray):

    (x,y) = (img.size[0],img.size[1])

    newimg = Image.new('RGB', (x, y))
    newimg.putdata(pixelModifier(imagePixelData, dataArray))

    return newimg


dataArray = binaryData(data)

modifiedImage=encode_enc( dataArray)

modifiedImage.save(input("Output directory: "))


