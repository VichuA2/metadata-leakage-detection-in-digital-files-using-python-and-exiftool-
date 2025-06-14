# 🧐 Metadata Leakage Detection in Digital Images

This project aims to **detect and extract metadata from digital images (like .jpg or .png)** and **analyze whether the photo contains sensitive information such as geolocation (GPS)**. It also provides a way to **classify images as “secure” or “not secure”** based on their metadata criteria.

## 🔹 Features

- **Extract EXIF metadata:** Retrieve camera make, model, dimensions, orientation, GPS info, and more.
- **Classify Security:** Determine whether an image is “secure” or “not secure” based on predefined criteria.
- **Analyze Location:** If GPS metadata is present, extract latitude and longitude and visualize it on a map.
- **User Friendly UI:** Built with Streamlit for convenient file upload and analysis.

## 🔹 Tools & Tech Stack

- **Python**
- **Streamlit**
- **Pillow (PIL)**
- **Pandas**
- **Exiftool (optional)** — for adding or modifying metadata externally.

## 🔹 Installation && Run

1. **Clone this repository:**

```bash
git clone https://github.com/{your-username}/metadata-leakage-detection.git



streamlit run main.py
