from PIL import Image
from datetime import datetime
import os

# Create the image based on parameters
def image_create(size: list, source: list, blank_map: list, out_name: str = None | str, out_path: str = None | str, show_outcome: bool = False) -> int:
    if size == None or source == None or blank_map == None:
        return -1
    
    # Create and load image
    image = Image.new('RGBA', size)
    pixels = image.load()

    # Color the pixels
    for x in range(size[0]):
        for y in range(size[1]):
            alpha = 255
            # Search if the current pixel should be blank
            for blank in blank_map:
                if blank[0] == x and blank[1] == y:
                    alpha = 0
                    break

            rgb_color = [0, 0, 0, alpha]
            if alpha > 0:
                for k in range(3): # Setup the current RGB color chanels
                    rgb_color[k] = source[x][k]
            
            rgb_color_tuple = tuple(rgb_color)
            pixels[y, x] = rgb_color_tuple

    # If the user doesn't specified the output directory set it to default
    directory: str = "img_out"

    # Get the time to make the file name unique if the user doesn't specified it
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fileName = f"img#{current_time}"

    # If the user specified the output path
    if out_path is not None:
        directory = out_path
        # savePath = f"{directory}/{fileName}"

    # If the user specified the file name
    if out_name is not None:
        out_name = str.strip(out_name, ".png")
        fileName = out_name
        # savePath = f"{directory}/{out_name}.png"

    savePath = f"{directory}/{fileName}.png"

    # Create "img" directory if it does not exists
    if not os.path.exists(directory):
        print(f"Directory not found!\nCreating directory \"{directory}\" ...\n")
        os.makedirs(directory)

    # Save the image and show if it is specified
    image.save(savePath)
    if show_outcome is True:
        image.show()
        print(f"Image saved as ~ {fileName} ~")
    
    return 0
