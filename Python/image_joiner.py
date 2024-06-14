import os
from PIL import Image
from typing import Optional

def join_images(image_left_path: str, image_right_path: str, separation: int, border: int = 0, 
                new_width_left: Optional[int] = None, new_height_left: Optional[int] = None, 
                new_width_right: Optional[int] = None, new_height_right: Optional[int] = None, 
                background: str = 'none') -> Image.Image:
    """
    Joins two images side by side with optional resizing and borders.
    
    Parameters:
    - image_left_path: Path to the left image.
    - image_right_path: Path to the right image.
    - separation: Pixels of separation between the images.
    - border: Pixels of border around the images.
    - new_width_left: Optional new width for the left image.
    - new_height_left: Optional new height for the left image.
    - new_width_right: Optional new width for the right image.
    - new_height_right: Optional new height for the right image.
    - background: Background color ('black', 'white', 'none').
    
    Returns:
    - A PIL Image object of the joined images.
    """
    # Assert that image paths exist and are valid images
    if not os.path.exists(image_left_path):
        raise FileNotFoundError(f"File {image_left_path} does not exist.")
    if not os.path.exists(image_right_path):
        raise FileNotFoundError(f"File {image_right_path} does not exist.")
    if not image_left_path.lower().endswith(('png', 'jpg', 'jpeg')):
        raise ValueError(f"File {image_left_path} is not a valid image format.")
    if not image_right_path.lower().endswith(('png', 'jpg', 'jpeg')):
        raise ValueError(f"File {image_right_path} is not a valid image format.")
    
    # Load images
    image_left = Image.open(image_left_path).convert("RGBA")
    image_right = Image.open(image_right_path).convert("RGBA")
    
    # Resize images if dimensions are provided
    if new_width_left and new_height_left:
        image_left = image_left.resize((new_width_left, new_height_left))
    if new_width_right and new_height_right:
        image_right = image_right.resize((new_width_right, new_height_right))
    
    # Calculate the size of the new image
    total_width = image_left.width + image_right.width + separation + 2 * border
    max_height = max(image_left.height, image_right.height) + 2 * border
    
    # Determine background color
    if background == 'black':
        bg_color = (0, 0, 0, 255)
    elif background == 'white':
        bg_color = (255, 255, 255, 255)
    else:  # 'none'
        bg_color = (255, 255, 255, 0)
    
    # Create a new blank image with the calculated size
    new_img = Image.new('RGBA', (total_width, max_height), bg_color)
    
    # Paste the images onto the new image with border
    new_img.paste(image_left, (border, border), image_left)
    new_img.paste(image_right, (image_left.width + separation + border, border), image_right)
    
    return new_img

# Example usage
if __name__ == "__main__":
    image_left = "./images_to_join/plot1a.png"
    image_right = "./images_to_join/plot1b.png"
    result = join_images(image_left, image_right, separation=50, border=20, background='white')
    result.save('./joined_images/joined_image.png')
    result.show()