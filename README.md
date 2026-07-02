# WearMatch

A Python tool that extracts the dominant color from a photograph of clothing.

## Why?

Many smartwatches allow users to customize the watch face color, but selecting a matching color manually is tedious and often inaccurate.

I built this project to automatically identify the most representative color from a shirt or T-shirt so it can be used as the watch face accent color.

## How it works

1. Capture a photo of the clothing.
2. Resize the image for faster processing.
3. Use K-Means clustering to identify dominant colors.
4. Return the most prominent color along with a color palette.

## Technologies

- Python
- Pillow
- NumPy
- SciPy
- Matplotlib

## Future Improvements

- Live camera support
- Mobile app
- Automatic smartwatch integration
- Background removal for more accurate color extraction