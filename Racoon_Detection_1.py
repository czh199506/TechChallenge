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

# Just load one image to test the functionality
for i in range(cols):
    name = data.at[i, 'filename']
    img = cv.imread(dict + name)

    # Extract the location for the rectangles
    xmin  = data.at[i, 'xmin']
    xmax = data.at[i, 'xmax']
    ymin = data.at[i, 'ymin']
    ymax = data.at[i, 'ymax']

    # Define the color and thickness for the rectangle
    color = (0,0,255)
    thickness = 2
    img = cv.rectangle(img, (xmin, ymin), (xmax, ymax), color, thickness)

    # Write the letter at the center of the rectangle
    pos = (int((xmin + xmax) / 2.0), int((ymin + ymax) / 2.0))
    cv.putText(img, 'R', pos, cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

    # Edited the name
    name = name[:-4] + '-edited' + name[-4:]

    # Save the edited image
    cv.imwrite(dict + name, img)

# Print the result
print("The entire process took {:.6f}s to complete".format(time.time()-start))






