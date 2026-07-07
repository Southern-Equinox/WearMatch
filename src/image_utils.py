"""
image_utils.py

Utility functions for loading, resizing and saving images.
"""

from pathlib import Path
from PIL import Image

from config import (
    INPUT_DIR,
    OUTPUT_DIR,
    SUPPORTED_EXTENSIONS,
    MAX_PIXELS,
)


def get_input_images():
    """
    Returns a sorted list of all supported images inside sample_input.
    """

    images = []

    for file in INPUT_DIR.iterdir():

        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            images.append(file)

    return sorted(images)


def load_image(image_path: Path):
    """
    Loads an image and converts it to RGB.

    Parameters
    ----------
    image_path : Path

    Returns
    -------
    PIL.Image
    """

    return Image.open(image_path).convert("RGB")


def resize_image(image):
    """
    Resize image if it exceeds MAX_PIXELS.

    Returns
    -------
    resized_image
    """

    width, height = image.size

    total_pixels = width * height

    if total_pixels <= MAX_PIXELS:
        return image

    scale_factor = (MAX_PIXELS / total_pixels) ** 0.5

    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    return image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )


def create_output_folder(image_path: Path):
    """
    Creates an output folder for an image.

    Example:

    output/
        shirt/
            palette.png
            average.png
    """

    folder = OUTPUT_DIR / image_path.stem

    folder.mkdir(parents=True, exist_ok=True)

    return folder


def save_image(image, output_path: Path):
    """
    Save PIL image.
    """

    image.save(output_path)


def get_image_info(image):
    """
    Returns useful information about the image.
    """

    width, height = image.size

    return {
        "width": width,
        "height": height,
        "pixels": width * height,
    }