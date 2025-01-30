import sys
import os
from PIL import Image, ImageOps

def main():


    #exactly two command-line arguments
    arguments_count = len(sys.argv)
    if arguments_count < 3:
        sys.exit("Too few command-line arguments")
    elif arguments_count > 3:
        sys.exit("Too many command-line arguments")
    else:
        imgInput = sys.argv[1]
        imgOutput = sys.argv[2]

    #opens and validates images
    imageOriginal, imageShirt = openImage(imgInput, imgOutput)

    #paste images together
    imagesComposite = imageComposite(imageOriginal, imageShirt)

    #save image into new file
    saveNewImage(imagesComposite, imgOutput)


def openImage(input, output):

    #file extensions = jpg, jpeg, png, and the same for both entries
    extensionsValid = {".jpg", ".jpeg", ".png"}
    if os.path.splitext(input)[1].lower() in extensionsValid and os.path.splitext(input)[1].lower() == os.path.splitext(output)[1].lower():
        #Validate real input
        try:
            source = Image.open(input)
            shirt = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Not a valid file extension or input and output extensions do not match")

    return source, shirt


def imageCropResize(img, shirt):
    size = shirt.size
    return ImageOps.fit(img, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))


def imageComposite(img, shirt):
    size = shirt.size
    imgCroped = ImageOps.fit(img, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    imgCroped.paste(shirt, (0,0), shirt)
    return imgCroped

def saveNewImage(input, output):
    return input.save(output)


if __name__ == "__main__":
    main()
