import numpy as np


def get_average_color(image):
    """
    Returns:
        (R, G, B)
    """

    img = np.array(image)

    avg = img.reshape(-1, 3).mean(axis=0)

    return tuple(avg.astype(int))