"""
main.py

Entry point for WearMatch.
"""

from config import *

from image_utils import (
    get_input_images,
    load_image,
    resize_image,
    create_output_folder,
)

from average_color import get_average_color

from dominant_palette import (
    prepare_pixels,
    calculate_elbow,
    extract_multiple_palettes,
)

from visualization import (
    show_image_comparison,
    choose_k_from_plot,
    show_average_color,
    show_multiple_palettes,
    save_average_color,
    save_multiple_palettes,
    save_elbow_plot,
)


def process_image(image_path):
    """
    Process a single image.
    """

    print(f"\n{'=' * 60}")
    print(f"Processing : {image_path.name}")
    print(f"{'=' * 60}")

    output_folder = create_output_folder(image_path)

    # ------------------------------------------
    # Load image
    # ------------------------------------------

    original = load_image(image_path)

    resized = resize_image(original)

    # ------------------------------------------
    # Show original & resized
    # ------------------------------------------

    if SHOW_ORIGINAL or SHOW_RESIZED:
        show_image_comparison(
            original,
            resized
        )

    # ------------------------------------------
    # Prepare dataframe
    # ------------------------------------------

    df = prepare_pixels(resized)

    # ------------------------------------------
    # Elbow plot
    # ------------------------------------------

    ks, distortions = calculate_elbow(
        df,
        MAX_K
    )

    save_elbow_plot(
        ks,
        distortions,
        output_folder
    )

    k = choose_k_from_plot(
        ks,
        distortions
    )

    print(f"\nSelected K = {k}")

    # ------------------------------------------
    # Average colour
    # ------------------------------------------

    average_colour = get_average_color(
        resized
    )

    show_average_color(
        average_colour
    )

    save_average_color(
        average_colour,
        output_folder
    )

    # ------------------------------------------
    # Palettes
    # ------------------------------------------

    palettes = extract_multiple_palettes(
        df,
        k
    )

    show_multiple_palettes(
        palettes
    )

    save_multiple_palettes(
        palettes,
        output_folder
    )

    print("\nFinished!")

    print(f"Saved to : {output_folder}")


def main():

    images = get_input_images()

    if len(images) == 0:

        print(
            "No images found inside sample_input."
        )

        return

    print(f"\nFound {len(images)} image(s).\n")

    for image in images:

        process_image(image)

    print("\nAll images processed.")


if __name__ == "__main__":
    main()