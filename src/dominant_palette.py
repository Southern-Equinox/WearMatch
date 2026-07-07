"""
dominant_palette.py

Functions for extracting dominant colours using K-Means clustering.
"""

import numpy as np
import pandas as pd

from scipy.cluster.vq import (
    whiten,
    kmeans,
)


def prepare_pixels(image):
    """
    Converts a PIL image into a whitened dataframe suitable
    for K-Means clustering.

    Returns
    -------
    DataFrame
    """

    img = np.array(image)

    pixels = img.reshape((-1, 3))

    df = pd.DataFrame(
        pixels / 255,
        columns=[
            "red",
            "green",
            "blue"
        ]
    )

    # Save original standard deviations
    df.attrs["std"] = df.std()

    # Whiten each channel
    df["red_w"] = whiten(df["red"])
    df["green_w"] = whiten(df["green"])
    df["blue_w"] = whiten(df["blue"])

    return df


def calculate_elbow(df, max_k=10):
    """
    Computes distortions for K = 1 ... max_k.

    Returns
    -------
    ks
        list of K values

    distortions
        list of distortion values
    """

    data = df[
        [
            "red_w",
            "green_w",
            "blue_w"
        ]
    ]

    ks = []
    distortions = []

    for k in range(1, max_k + 1):

        _, distortion = kmeans(data, k)

        ks.append(k)
        distortions.append(distortion)

    return ks, distortions


def extract_palette(df, k):
    """
    Returns dominant colours.

    Parameters
    ----------
    df
        Whitened dataframe

    k
        Number of clusters

    Returns
    -------
    List[(R,G,B)]
    """

    data = df[
        [
            "red_w",
            "green_w",
            "blue_w"
        ]
    ]

    centers, _ = kmeans(data, k)

    std = df.attrs["std"]

    palette = []

    for center in centers:

        rgb = np.array([
            center[0] * std["red"],
            center[1] * std["green"],
            center[2] * std["blue"],
        ])

        rgb = np.clip(rgb, 0, 1)

        palette.append(
            tuple(
                (rgb * 255).astype(int)
            )
        )

    return palette

def extract_multiple_palettes(df, k):
    """
    Returns palettes for (k-1), k and (k+1).

    Returns
    -------
    dict

    Example

    {
        4: [...],
        5: [...],
        6: [...]
    }
    """

    palettes = {}

    for kk in range(max(2, k - 1), k + 2):

        palettes[kk] = extract_palette(df, kk)

    return palettes