import streamlit as st

from PIL import Image

from steganography import encode_image, decode_image

import io


st.set_page_config(
    page_title="Image Steganography",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 Image Steganography")

tab1, tab2 = st.tabs(["Encode", "Decode"])


####################################################
# ENCODE
####################################################

with tab1:

    st.header("Hide Secret Message")

    uploaded = st.file_uploader(
        "Choose PNG Image",
        type=["png"],
        key="encode"
    )

    secret = st.text_area(
        "Secret Message"
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(image, caption="Original Image")

        if st.button("Encode"):

            encoded = encode_image(image, secret)

            st.success("Message Hidden Successfully")

            st.image(
                encoded,
                caption="Encoded Image"
            )

            buffer = io.BytesIO()

            encoded.save(buffer, format="PNG")

            st.download_button(

                label="Download Encoded Image",

                data=buffer.getvalue(),

                file_name="encoded_image.png",

                mime="image/png"

            )


####################################################
# DECODE
####################################################

with tab2:

    st.header("Decode Hidden Message")

    uploaded2 = st.file_uploader(

        "Upload Encoded Image",

        type=["png"],

        key="decode"

    )

    if uploaded2:

        image = Image.open(uploaded2)

        st.image(image)

        if st.button("Decode"):

            message = decode_image(image)

            st.success("Hidden Message")

            st.text_area(

                "",

                value=message,

                height=150

            )