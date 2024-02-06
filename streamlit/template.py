import streamlit as st

def side_background():
    st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://eccles.utah.edu/wp-content/uploads/2017/12/Eccles_Logo_Header_Final_Desktop.png);
                    background-repeat: no-repeat;
                    padding-top: 80px;
                    background-position: 20px 20px;
                    background-size: 80%;
                    background-position-x: center;
                }}
            </style>
            """,
        unsafe_allow_html=True,
        )
    
def side_content():
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#2e7bcf,#2e7bcf);
            color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
            )