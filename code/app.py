import pandas as pd
import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS
from fractions import Fraction

def classify_image_security(exifdata):
    secure_criteria = {
        "Make": "SecureMake",
        "Model": "SecureModel",
    }

    for tag_id, criteria_value in secure_criteria.items():
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id, b"")
        if isinstance(data, bytes):
            data = data.decode("utf-8", "ignore")

        if data == criteria_value:
            return "Secure"

    return "Not Secure"

def extract_geolocation(exifdata):
    gps_info = exifdata.get(34853)  # EXIF tag for GPSInfo
    if gps_info:
        def convert_to_degrees(value):
            d = float(value[0])
            m = float(value[1])
            s = float(value[2])
            return d + (m / 60.0) + (s / 3600.0)

        lat = convert_to_degrees(gps_info[2])
        if gps_info[1] == 'S':
            lat = -lat

        lon = convert_to_degrees(gps_info[4])
        if gps_info[3] == 'W':
            lon = -lon

        return lat, lon
    return None

def display_map(location):
    if location:
        st.subheader('Image Location on Map')
        map_data = pd.DataFrame({'lat': [location[0]], 'lon': [location[1]]})
        st.map(map_data)
    else:
        st.subheader("No location details")

def load_image():
    uploaded_file = st.sidebar.file_uploader(label='Pick an image to test')
    if uploaded_file and st.sidebar.button('Load'):
        image = Image.open(uploaded_file)
        exifdata = image._getexif()

        with st.expander('Selected Image', expanded=True):
            st.image(image, use_container_width=True)

        st.subheader('Image Exchange Information')
        info_dict = {
            "Filename": uploaded_file.name,
            "Image Size": image.size,
            "Image Width": image.width,
            "Image Height": image.height,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        for label, value in info_dict.items():
            st.markdown(f"{label:25}: {value}")

        if exifdata is not None:
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id, b"")
                if isinstance(data, bytes):
                    data = data.decode("utf-8", "ignore")
                st.markdown(f"{tag:25}: {data}")

            image_security = classify_image_security(exifdata)
            st.subheader('Image Security Classification')
            st.write(f"This image is: {image_security}")

            location = extract_geolocation(exifdata)
            display_map(location)
        else:
            st.subheader('Image Security Classification')
            st.write('This image does not have metadata or does not match secure criteria.')

def main():
    st.title('Image EXIF Data Analysis With Location Tracing')
    st.sidebar.title("Upload an Image")
    st.sidebar.write("Click 'Load' to analyze metadata and location.")
    load_image()

if __name__ == '__main__':
    main()
