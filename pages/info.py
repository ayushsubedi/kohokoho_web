import streamlit as st


def write():
    st.title('Why?')

    st.subheader("-> About")
    st.info(
        """
        Kohokoho (को हो को हो) is a python package that anonymizes a dataset.
        Currently, it is still in its infancy,
        and only support a select few data types.

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

        -> "Ayush Subedi" on your original data will be changed to "Rob Garner" (as an example). The next occurance of "Ayush Subedi" will also change to "Rob Garner".   
        
        -> sdf
        """
    )