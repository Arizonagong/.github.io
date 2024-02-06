import streamlit as st
from streamlit_extras.app_logo import add_logo 
from template import side_background, side_content

  
# Page Config
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Sidebar Config
#add_logo("img/david_eccles_logo.png",height=50)
side_background()
#side_content()
#st.sidebar.image("img/david_eccles_logo.png", use_column_width=True)

with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white'>About</h1>", unsafe_allow_html=True)
st.write("# Welcome to Streamlit! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)