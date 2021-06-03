import streamlit as st


def write():
    st.title('About')

    st.subheader("-> Package")
    st.info(
        """
        Kohokoho (को हो को हो) is a python package that anonymizes a dataset.
        Currently, it is still in its infancy,
        and only support a select few data types:

        - Names
        - IDs (UUID, Numeric IDs etc.)
        - Categorical values
        - Discrete values
        - Continuous values 
        - Date
        - Email


        This is a simple UI wrapper for the package built with Streamlit.
        """
    )
    st.subheader("-> What is anonymization?")
    st.info(
        """
        It is a process of hiding sensitive data. Although there are different variations, 
        Kohokoho was developed to make sure the gist of the data remains the same. That is, 
        anonymize the sensite data but allow insights to be drawn from it to match the trends 
        from the original data. 

        The technique used are Data Masking and Pseudonymization.
        """
    )
    st.subheader("-> Wait, what?")
    st.info(
        """
        Let's look at some examples.

        - "Ayush Subedi" on your original data will be changed to "Rob Garner" (as an example). The next occurance of "Ayush Subedi" will also change to "Rob Garner".   
        
        - All your IDs will be converted to randomly generated IDs but will preserve conversion for same ID. For example, if your book_id=5 on your original dataset, it will be converted into something like book_id=a1e54a59-e1a0-4dd8-a019-957d77658f16 but the next book_id=5 will also be converted to a1e54a59-e1a0-4dd8-a019-957d77658f16.
       
        - All your categorical values will me masked but like before it will preserve conversion.

        - All numeric values will be scaled randomly but the scale will remain consistent. For example, if your column stores "items sold", and the most expensive item is a "monitor", the anon dataset will also have "monitor" (masked to something else), have the highest price. The original dataset range will be respected.
       
        - Dates will be changed to random dates in the same range. Do not change this if you are trying to build anything "timeseries". Instead anon all other columns.

        - Email "ayush.subedi@gmail.com" will be changed to "w5qms8tdg5fu@anonemail.com" (as an example). The next occurance of "ayush.subedi@gmail.com" will also change to "w5qms8tdg5fu@anonemail.com".
        """
    )
    st.subheader("-> Roadmap")
    st.info(
        """
        Data types 
        - [x]  Names
        - [x]  IDs
        - [x]  Categorical values
        - [x]  Discrete values
        - [x]  Continuous values
        - [x]  Date
        - [x]  Email
        - [ ]  Social Security numbers
        - [ ]  DateTime (including date formats inputs)
        - [ ]  Spatial data
        - [ ]  Image URL
        - [ ]  Phone number
        - [ ]  IDENTIFY OTHERS

        Platform
        - [ ]  move away from Streamlit (preferably Flask/Django)
        - [ ]  move away from heroku free tier

        Contributions
        - [ ]  find contributors
        - [ ]  develop contribution guidelines
        """
    )