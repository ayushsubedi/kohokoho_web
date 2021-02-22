"""Main module for the streamlit app"""
import streamlit as st
import pages.page1, pages.page2
from PIL import Image

PAGES = {
    "page1": pages.page1,
    "page2": pages.page2
}


def main():
    """Main function of the App"""
    image = Image.open('static/img/logo.png')
    st.sidebar.image(image, use_column_width=True)
    selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("Objectives")
    st.sidebar.info(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et posuere nisi, 
        vitae condimentum odio. Donec a feugiat nisi. Phasellus imperdiet libero mi, 
        eu vulputate lacus lacinia a. Orci varius natoque penatibus et magnis dis 
        """
    )


if __name__ == "__main__":
    main()