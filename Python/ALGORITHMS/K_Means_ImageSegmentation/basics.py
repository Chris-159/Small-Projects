import os
from datetime import datetime

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

RANGE_DEF = int(256)
OUTPUT_DIR = "out"
OUTPUT_FILE_PREFIX = "output_"

def image_get(file_name:str) -> np.array:
    if file_name is None:
       return None
    
    try:
        img = Image.open(file_name) #open image
    except:
        return None

    gray_img = img.convert("L") #convert to grayscale

    gray_np = np.array(gray_img) #convert to numpy array

    return gray_np

# def create_histogram(image_arr:np.array, range_:int = RANGE_DEF) -> np.array:
#     # creates an array with the length of 256, which contains all color value count
#     return np.bincount(image_arr.flatten(), minlength=range_)

def show_image(image_, title="Image"):
    plt.imshow(image_)
    plt.title(title)
    plt.axis('off')
    plt.show()

def image_save(image):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_name = f"{OUTPUT_FILE_PREFIX}{timestamp}.png"
    output_path = os.path.join(OUTPUT_DIR, file_name)

    plt.imsave(output_path, image)
    print("Image saved.")