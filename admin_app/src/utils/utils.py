from PIL import Image, ImageDraw, ImageOps


def create_circular_image(image_path, size=100) -> Image:
    """
    Create a circular image with a specified background color. (background is also circular)

    :param image_path: Path to the input image.
    :param size: Size of the circular image.
    :return: A PIL Image with a circular mask applied.
    """
    # Calculate the new size with padding
    img_size = (size, size)

    # Open and resize the image
    img = Image.open(image_path).resize(img_size)

    # Create a circular mask
    mask = Image.new('L', img_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img_size[0], img_size[0]), fill=255)

    img_with_mask = Image.new("RGBA", img_size, (0,0,0,0))
    img_with_mask.paste(img, (0, 0), mask)

    return img_with_mask
