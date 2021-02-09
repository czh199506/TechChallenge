# import import libraries
import numpy as np
import cv2 as cv
import pandas as pd

# Import time to measure the duration
import time

# load the csv data file into the system
data = pd.read_csv(r'C:\Users\caizh\Documents\Technical Challenge Gluxkind\archive\train_labels_.csv')

# check the data loaded by using print
print(data)

# extract the dimension of the data frame
(cols, rows) = data.shape

# Define the dictory to read and store the image
dict = r'C:/Users/caizh/Documents/Technical Challenge Gluxkind/archive/Racoon Images/images/'

# Get the time stamp before the process
start = time.time()

# Create a list to store the name of images haven't processed already
proc_list = []

# Just load one image to test the functionality
for i in range(cols):
    name = data.at[i, 'filename']
    # Add the name to the proceed list and open the original file if not proceeded
    if name not in proc_list:
        proc_list.append(name)
        img = cv.imread(dict + name)

    # If the file name is already in the proceed list, then open the edited file
    else:
        name_ref = name
        name = name[:-4] + '-edited' + name[-4:]
        img = cv.imread(dict + name)
        name = name_ref

    # Extract the location for the rectangles
    xmin  = data.at[i, 'xmin']
    xmax = data.at[i, 'xmax']
    ymin = data.at[i, 'ymin']
    ymax = data.at[i, 'ymax']

    # Extract the size of the image for the text size calculation
    width = data.at[i, 'width']
    height = data.at[i, 'height']

    # Define the color and thickness for the rectangle
    color = (0,0,255)
    thickness = 2
    img = cv.rectangle(img, (xmin, ymin), (xmax, ymax), color, thickness)

    # Write the letter at the center of the rectangle
    # Scale the txt according to the length of the diagonal of the image
    font_scale = 0.8/(300**2+200**2)**0.5*(width**2+height**2)**0.5
    pos = (int((xmin + xmax) / 2.0), int((ymin + ymax) / 2.0))
    cv.putText(img, 'R', pos, cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), 2, cv.LINE_AA)

    # Edited the name
    name = name[:-4] + '-edited' + name[-4:]

    # Save the edited image
    cv.imwrite(dict + name, img)

# Print the result
print("The entire process took {:.6f}s to complete".format(time.time()-start))






