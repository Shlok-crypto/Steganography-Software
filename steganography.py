from PIL import Image

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):

        # list of binary codes
        # of given data
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [ value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3] ]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means stop
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# Encode data into image
def encode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
    image.show()

    data = input("Enter data to be encoded : ")
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))




# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

# Main Function
def incript():
    a = int(input(":: Welcome to Steganography ::\n"
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()

    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")




#### MY TRY



# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# rgb_value = [(27, 64, 164), (248, 244, 194), (174, 246, 250),
#              (149, 95, 232), (188, 156, 169), (71, 167, 127),
#              (132, 173, 97), (113, 69, 206), (255, 29, 213),
#              (53, 153, 220), (246, 225, 229), (142, 82, 175)]
# cols, rows = 3, 12
# rgb = [[0 for i in range(cols)] for j in range(rows)]
#
# for p in range(0, 12):
#     for j in range(0, 3):
#         rgb[p][j] = rgb_value[p][j]
#
# print(rgb)
# print("\nogg\n")
#
# bi = format(ord("H"), '08b')
# print(bi)
#
# # bi => 01001000
# # if 0 then even ie: 2,4
# # if 1 then odd  ie: 3,5
# i = 0
#
# for p in range(0, 9):
#     for j in range(0, 3):
#         if i <8:
#             # making even value odd = 3 => 2
#             if (bi[i] == '0' and rgb[p][j] % 2 != 0):
#                 rgb[p][j] -= 1
#                 print("1i=>",i,bi[i])
#                 i += 1
#             # making odd value even = 2 => 1
#             elif (bi[i] == '1' and rgb[p][j] % 2 == 0):
#                 if (rgb[p][j] != 0):
#                     rgb[p][j] -= 1
#                     print("2i=>", i, bi[i])
#                     i += 1
#                 else:
#                     rgb[p][j] += 1
#                     print("3i=>", i, bi[i])
#                     i += 1
#             else:
#                 print(bi[i],i)
#                 i += 1
#                 print("did  not enter")
#
# print(rgb)
#
# print("done")
