import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def get_angle_and_text(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
      
        x, y, w, h = cv2.boundingRect(contour)
        
        rect = cv2.minAreaRect(contour)
        angle = rect[2]
        
        if angle < -45:
            angle += 90
        
        roi = image[y:y + h, x:x + w]

        text = recognize_text(roi)
    
        print(f"Detected Text: {text}, Rotation Angle: {angle:.2f} degrees")
       
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"{text}, {angle:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def recognize_text(roi):
    
    template_dir = 'D:/'  # Directory where template images are stored
    templates = {}
    
    for filename in os.listdir(template_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            character = filename[0]  
            template = cv2.imread(os.path.join(template_dir, filename), cv2.IMREAD_GRAYSCALE)
            if template is not None:
                templates[character] = template
            else:
                print(f"Warning: Could not load template {filename}")
    
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    best_match = ""
    best_value = 0  

    for character, template in templates.items():
    
        if roi_gray.shape[0] >= template.shape[0] and roi_gray.shape[1] >= template.shape[1]:
            # Match the template
            result = cv2.matchTemplate(roi_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            
            if max_val > best_value:
                best_value = max_val
                best_match = character
    
    return best_match if best_value > 0.5 else "Unknown"  # Return "Unknown" if no good match found


image_files = [
    "D:/movies/download.png"
    # Add more image paths as needed
]

for image_file in image_files:
    get_angle_and_text(image_file)
