from PIL import Image
import random

img_black = Image.open('./images/input/black.png')
img_white = Image.open('./images/input/white.png')
img_ca = Image.open('./images/input/ca-flag.gif')
img_ks = Image.open('./images/input/ks-flag.gif')

def create_mixed_image_different_sizes(image1, image2, sections_x, sections_y):    
    # Resize both images to the same dimensions (based on the smaller image)
    min_width = min(image1.width, image2.width)
    min_height = min(image1.height, image2.height)
    
    image1_resized = image1.resize((min_width, min_height))
    image2_resized = image2.resize((min_width, min_height))
    
    # Calculate section widths and heights
    # Distribute the leftover pixels equally among sections
    base_width = min_width // sections_x
    base_height = min_height // sections_y
    extra_width = min_width % sections_x
    extra_height = min_height % sections_y
    
    # Compute cumulative widths and heights for accurate box placement
    section_widths = [base_width + (1 if i < extra_width else 0) for i in range(sections_x)]
    section_heights = [base_height + (1 if i < extra_height else 0) for i in range(sections_y)]
    
    # Calculate the starting positions of each section
    x_positions = [sum(section_widths[:i]) for i in range(sections_x)] + [min_width]
    y_positions = [sum(section_heights[:i]) for i in range(sections_y)] + [min_height]
    
    # Create a new blank image
    result_image = Image.new("RGB", (min_width, min_height))
    
    # Loop through the sections
    for y in range(sections_y):
        for x in range(sections_x):
            # Define the section box
            left = x_positions[x]
            upper = y_positions[y]
            right = x_positions[x + 1]
            lower = y_positions[y + 1]
            box = (left, upper, right, lower)
            
            # Choose randomly between the two images for this section
            source_image = random.choice([image1_resized, image2_resized])
            section = source_image.crop(box)
            
            # Paste the chosen section into the result image
            result_image.paste(section, box)

    result_image.show()

def create_mixed_image_different_sizes(image1, image2, sections_x, sections_y, weight_firstImg):
        # Resize both images to the same dimensions (based on the smaller image)
    min_width = min(image1.width, image2.width)
    min_height = min(image1.height, image2.height)
    
    image1_resized = image1.resize((min_width, min_height))
    image2_resized = image2.resize((min_width, min_height))
    
    # Calculate section widths and heights
    # Distribute the leftover pixels equally among sections
    base_width = min_width // sections_x
    base_height = min_height // sections_y
    extra_width = min_width % sections_x
    extra_height = min_height % sections_y
    
    # Compute cumulative widths and heights for accurate box placement
    section_widths = [base_width + (1 if i < extra_width else 0) for i in range(sections_x)]
    section_heights = [base_height + (1 if i < extra_height else 0) for i in range(sections_y)]
    
    # Calculate the starting positions of each section
    x_positions = [sum(section_widths[:i]) for i in range(sections_x)] + [min_width]
    y_positions = [sum(section_heights[:i]) for i in range(sections_y)] + [min_height]
    
    # Create a new blank image
    result_image = Image.new("RGB", (min_width, min_height))
    
    # Loop through the sections
    for y in range(sections_y):
        for x in range(sections_x):
            # Define the section box
            left = x_positions[x]
            upper = y_positions[y]
            right = x_positions[x + 1]
            lower = y_positions[y + 1]
            box = (left, upper, right, lower)
            
            # Choose randomly between the two images for this section
            source_image = random.choices(
                                population=[image1_resized, image2_resized],
                                weights=[weight_firstImg, 1 - weight_firstImg],
                                k=1
                            )
            print(source_image)
            section = source_image[0].crop(box)
            
            # Paste the chosen section into the result image
            result_image.paste(section, box)

    result_image.show()

create_mixed_image_different_sizes(img_ca, img_ks, 10, 10, 0.05)
# create_mixed_image_different_sizes(img_white, img_black, 10, 10, 0.005)