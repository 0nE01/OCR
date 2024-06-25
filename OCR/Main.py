#Modules
import easyocr
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Define a reader and select every language you want.
reader = easyocr.Reader(['fa','en'])
# Detect Text in your image.
result = reader.readtext('Path_to_image')

# Get text within your image.
text = ""
for i in range(len(result)):
  text += result[i][1] + " "
# Print the text.
print(text)

# Read your image and draw bounding boxes for texts in your image.
img = cv.imread('Path_to_image')
for i in range(len(result)):
    top_left = tuple(result[i][0][0])
    bottom_right = tuple(result[i][0][2])
    text = result[0][1]
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv.putText(img,text,top_left, font, 0.5,(255,255,255),2,cv.LINE_AA)

#Show the image.
plt.imshow(img)
plt.show()
