# 🎨 WearMatch

WearMatch is a Python application that extracts the dominant colours from an image of clothing to help generate a matching smartwatch face or theme.

The project was inspired by a simple problem: **choosing a watch face colour that complements my outfit**. Instead of manually picking colours by eye, WearMatch analyzes an image and suggests representative colours using K-Means clustering.

---

## Features

- 📷 Load images from a folder
- 🖼 Display original and downscaled images
- 📉 Generate an Elbow Plot to determine the optimal number of clusters
- 🖱 Select the desired K value by clicking directly on the plot
- 🎨 Extract dominant colour palettes
- 🌈 Compare palettes for **K-1**, **K**, and **K+1**
- 🟦 Compute the average image colour
- 💾 Save generated palettes and colour swatches

---

## Project Structure

```
WearMatch/
│
├── sample_input/
├── output/
├── src/
│   ├── config.py
│   ├── image_utils.py
│   ├── average_color.py
│   ├── dominant_palette.py
│   ├── visualization.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Technologies

- Python
- Pillow
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## Installation

Clone the repository

```bash
git clone https://github.com/Southern-Equinox/WearMatch.git
```

Move into the project

```bash
cd WearMatch
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Place one or more images inside

```
sample_input/
```

Run

```bash
python src/main.py
```

For each image, WearMatch will

1. Display the original image.
2. Display the resized image used for analysis.
3. Generate an Elbow Plot.
4. Allow you to select the number of colour clusters by clicking the graph.
5. Display:
   - Average colour
   - Palette for K-1
   - Palette for K
   - Palette for K+1
6. Save all generated outputs inside

```
output/<image_name>/
```

---

## Example Workflow

```
Original Image
        │
        ▼
Downscaled Image
        │
        ▼
Elbow Plot
        │
(click K)
        ▼
Average Colour
        │
        ▼
Dominant Palettes
```

---

## Future Improvements

- Automatic K detection
- Background removal
- Clothing segmentation
- Webcam support
- Smartwatch integration
- Desktop GUI
- Mobile application
- Export watch themes
- Colour harmony recommendations

---

## Why I Built This

Most smartwatch companion apps require users to manually choose colours.

I wanted a tool that could analyze a photo of my clothing and recommend colours automatically, making it easier to coordinate my watch face with my outfit.

WearMatch started as a small image-processing experiment and has grown into a modular computer vision project.

---

## License

This project is released under the MIT License.
