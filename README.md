# Identify-Text-and-Rotational-Angle-from-Sample-Images

Instructions for Implementation
Install Required Libraries: Make sure you have OpenCV and Matplotlib installed. You can install them using pip:

pip install opencv-python matplotlib

Create Template Directory: Create a directory named templates in the same directory as your script. This directory should contain images of the alphanumeric characters you want to recognize. For example:

A.png
B.png
1.png
2.png
etc.
Image Files: Replace the paths in the image_files list with the actual paths to the images you want to analyze.

Explanation of the Code
get_angle_and_text: This function reads the image, processes it to find contours, calculates the rotational angle using minAreaRect, and identifies the text using the recognize_text function.

recognize_text: This function performs template matching to identify characters in the ROI (Region of Interest). It compares the cropped image segment against the pre-loaded character templates and returns the best match.

Displaying Results: The code draws rectangles around detected text and shows the detected text with its angle on the original image.
