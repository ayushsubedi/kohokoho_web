"""Main module for the streamlit app"""
import streamlit as st
import pages.anonymizer, pages.info
from PIL import Image

PAGES = {
    "Anonymizer": pages.anonymizer,
    "Info and Project Links": pages.info
}


def main():
    """Main function of the App"""
    image = Image.open('static/img/kohokohologo.png')
    st.sidebar.image(image, use_column_width=True)
    selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("About")
    st.sidebar.info(
        """
        Kohokoho is a python package that anonymizes a dataset. Currently, it is still in infancy, and only support a select few data types. This is a UI wrapper for the package. 
        """
    )


if __name__ == "__main__":
    main()