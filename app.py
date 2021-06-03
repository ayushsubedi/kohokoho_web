"""Main module for the streamlit app"""
import streamlit as st
import pages.anonymizer
import pages.info
import pages.installation
from PIL import Image

PAGES = {
    "Anonymizer": pages.anonymizer,
    "About": pages.info,
    "Installation": pages.installation
}


def main():
    """Main function of the App"""
    image = Image.open('static/img/kohokoho_new.png')
    st.sidebar.image(image, use_column_width=True)
    selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.write()
    st.sidebar.title("Installation")
    st.sidebar.info(
        """
        pip install kohokoho
        """
    )
    st.sidebar.title("Project Links")
    st.sidebar.markdown('[GitHub for this project](https://github.com/ayushsubedi/kohokoho_web)', unsafe_allow_html=True)
    st.sidebar.markdown('[GitHub for the package](https://github.com/ayushsubedi/kohokoho)', unsafe_allow_html=True)  
    st.sidebar.markdown('[PIP link for package](https://pypi.org/project/kohokoho/)', unsafe_allow_html=True)  
    st.sidebar.title("Contribute")
    st.sidebar.info(
        """
        Feel free to create issues, or submit a pull request.
        """
    )
    image_ = Image.open("static/img/license.png")
    st.sidebar.image(image_, use_column_width=True)
if __name__ == "__main__":
    main()
