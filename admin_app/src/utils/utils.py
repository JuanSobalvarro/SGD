from PIL import Image, ImageDraw, ImageOps


def create_circular_image(image_path, size=100, circle_pad: int = 0, bg_color=(0,0,0,0)) -> Image:
    """
    Create a circular image with a specified background color. (background is also circular)

    :param image_path: Path to the input image.
    :param size: Size of the circular image.
    :param circle_pad: Padding of the circle around the image.
    :param bg_color: Background color in RGB format.
    :return: A PIL Image with a circular mask applied and background color visible.
    """
    # Calculate the new size with padding
    crop_img_size = (size - 2 * circle_pad, size - 2 * circle_pad)

    # Open and resize the image
    img = Image.open(image_path).resize(crop_img_size)

    bg_img = Image.new('RGBA', crop_img_size, bg_color)

    # Create a circular mask
    mask = Image.new('L', crop_img_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, crop_img_size[0], crop_img_size[0]), fill=255)

    img_with_mask = Image.new("RGBA", crop_img_size, (0,0,0,0))
    img_with_mask.paste(img, (0, 0), mask)

    img_with_bg = Image.alpha_composite(bg_img, img_with_mask)

    # create the bigger circular mask

    # final image
    final_img = Image.new()

    return img_with_bg
