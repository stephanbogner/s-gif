# ----------------------------------------------------------------------------------
# | Settings
# ----------------------------------------------------------------------------------

fileTypesToGif = ["jpg", "jpeg", "png", "tiff", "webp"]
naturalSort = True # numbers will be sorted naturally (1,2,3,4,5,6,7,8,9,10,11) and not computer bullshit (1,10,2,3,etc.)
framesPerSecond = 15
exportLocation = "./" # parent directory


# ----------------------------------------------------------------------------------
# | Code
# ----------------------------------------------------------------------------------


import os
import string
from PIL import Image
from natsort import natsorted
from images2gif import writeGif
from collections import defaultdict

print
print
print
print ("----------------------------------------")
print (" Start")
print ("----------------------------------------")

rootDir = '.' # Set the directory you want to start from
counter = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    print
    print ("Folder: " + dirName)
    gifName = os.path.split( os.path.normpath(dirName) )[1]

    if gifName == ".":
        gifName = "unnamed" + str(counter)

    gifName += ".gif"

    # Sort files
    sortedFileList = fileList
    if naturalSort:
        sortedFileList = natsorted(sortedFileList)

    images = []

    for fileName in sortedFileList:
        fileNameSplitByPeriod = fileName.split(".") #image.jpg -> ['image', 'jpg']
        extension = fileNameSplitByPeriod[len(fileNameSplitByPeriod)-1].lower() # image.jpg ->  'jpg'
        if extension in fileTypesToGif:
            fullPath = os.path.abspath( dirName + "/"+ fileName) #path to file including filename
            images.append(fullPath)

    print "Images found: " + str(images.__len__())
    if images.__len__() > 1:
        numberOfFrames = images.__len__()
        duration = float(numberOfFrames) / framesPerSecond
        durationPerFrame = 1/float(framesPerSecond)
        print gifName + ' (' + str(numberOfFrames) + ' frames -> ' + str(duration) + 's)'

        imgs = []
        for x in xrange(0, images.__len__() - 1):
            img = Image.open(images[x])
            imgs.append(img)
        writeGif(exportLocation + gifName, imgs, durationPerFrame)
        counter += 1
    else:
        print "Not enough images to create animation (needs more than two)"

print
print ("----------------------------------------")
print (" All done - glad I could help :)")
print ("----------------------------------------")
print
print
print