from admin_app.src.utils.utils import create_circular_image


def main():
    # Path to your image
    image_path = "../images/test/test-96.png"

    # Create a circular image with a specified background color
    circular_image = create_circular_image(image_path, size=1000, circle_pad=100, bg_color=(255, 0, 0))  # Red background
    circular_image.show()


if __name__ == "__main__":
    main()
