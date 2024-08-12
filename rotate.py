from PIL import Image

def rotate_image(image: Image, rotations: int) -> Image:
    """
    Rotates the given image by 90 degrees counter-clockwise the specified number of times.

    Parameters:
    image (PIL.Image): The image to rotate.
    rotations (int): The number of 90-degree counter-clockwise rotations to apply.

    Returns:
    PIL.Image: The rotated image.
    """
    return image.rotate(rotations * 90)
