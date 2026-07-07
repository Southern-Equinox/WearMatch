"""
config.py

Stores project-wide configuration values and commonly used paths.
"""

from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

# WearMatch/
ROOT_DIR = Path(__file__).resolve().parent.parent

SRC_DIR = ROOT_DIR / "src"
INPUT_DIR = ROOT_DIR / "sample_input"
OUTPUT_DIR = ROOT_DIR / "output"

# Create output directory automatically
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Supported Image Formats
# ==========================================================

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
    ".tif",
    ".tiff",
    ".avif",
}

# ==========================================================
# Image Processing
# ==========================================================

# Resize very large images for faster K-Means processing.
# Images smaller than this limit will not be resized.
MAX_PIXELS = 100_000

# ==========================================================
# K-Means Settings
# ==========================================================

# Elbow plot range
MIN_K = 1
MAX_K = 10

# Default value (used if user presses Enter)
DEFAULT_K = 5

# ==========================================================
# Visualization
# ==========================================================

SHOW_ORIGINAL = True
SHOW_RESIZED = True
SHOW_ELBOW = True
SHOW_AVERAGE = True
SHOW_PALETTE = True

# ==========================================================
# Output Settings
# ==========================================================

SAVE_RESULTS = True

SAVE_AVERAGE_IMAGE = True
SAVE_PALETTE_IMAGE = True
SAVE_ELBOW_PLOT = True

# Folder structure:
#
# output/
# ├── shirt/
# │   ├── average.png
# │   ├── palette.png
# │   ├── elbow.png
# │   └── report.txt
#

# ==========================================================
# Matplotlib
# ==========================================================

FIGURE_DPI = 150