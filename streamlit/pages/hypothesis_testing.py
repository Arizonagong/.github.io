# The purpose of this page is to visualize t-value and p-value calculation 
# functions with matplotlib

# -----. Import Libraries
import matplotlib as map
import matplotlib.pyplot as plt
import scipy.stats as sts
from scipy.stats import t
import re
from streamlit_sortables import sort_items
import streamlit as st
from streamlit_extras.stodo import to_do


# -----. CSS Integration
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
   
# -----. Layout

col1, col2 = st.columns(2)

with col1:
    # -----. Input Config
    
    # Input1: Hypothesis
    with st.container():
        null = st.text_input('Write Your Null Hypothesis')
        smpl_m = st.number_input('What is your sample mean')
        smpl_std = st.number_input('What is your sample standard deviation')
        smpl_n = st.number_input('What is your sample size')
        sig = st.number_input('What is your significance level', placeholder=0.05)

with col2:
    # Testing Types using Regex
    # reference: https://pythex.org/
    null_rgx_lower = re.search("(\D+(>=|=>)(\s+|\d+)\d+)", null)
    null_rgx_upper = re.search("(\D+(<=|=<)(\s+|\d+)\d+)", null)
    null_rgx_two = re.search("(\D+(=)(\s+|\d+)\d+)", null)

    # Extracting hv value from the input string
    hv = re.findall(r'\d+', null)

    # Output in text
    if null != '':
        st.write('H0:', null)
        if null_rgx_lower:
            st.markdown(f'Ha: mu < {hv[0]}.')
            st.markdown('Your testing is: Lower Tailed Testing')
            st.markdown(f"Sample mean:{smpl_m}")
            st.markdown(f"Sample standard deviation: {smpl_std}")
            st.markdown(f"Sample size: {smpl_n}")
            st.markdown(f"Sample size: {smpl_n}")
        elif null_rgx_upper:
            st.write(f'Ha: mu > {hv[0]}. ')
            st.write('Your testing is: Upper Tailed Testing')
            st.write(f"Sample mean:{smpl_m}")
            st.write(f"Sample standard deviation: {smpl_std}")
            st.write(f"Sample size: {smpl_n}")
        elif null_rgx_two:
            st.write(f'Ha: mu = {hv[0]}. ')
            st.write('Your testing is: Two Tailed Testing')
            st.write(f"Sample mean:{smpl_m}")
            st.write(f"Sample standard deviation: {smpl_std}")
            st.write(f"Sample size: {smpl_n}")
        else: 
            st.write('Your input is not a valid format.')
            st.write(f"Sample mean:{smpl_m}")
            st.write(f"Sample standard deviation: {smpl_std}")
            st.write(f"Sample size: {smpl_n}")

# Sortable inputs
# reference: https://github.com/ohtaman/streamlit-sortables
original_items = [
    {'header': 'Select Library or Module',  'items': ['np', 'pd', 'sts', 'plt']},
    {'header': 'Select Module or Function', 'items': ['t', 'ppf', 'cdf', 'sqrt']},
    {'header': 'Drag and Drop your library, module, and function', 'items': []},
]

sorted_items = sort_items(original_items, multi_containers=True)

# Your code chunks selected
code_slt=list(sorted_items[2].values())[1] # Extract element value of list
code_input=f"({sig},{smpl_n-1})"

# join the list element with "." as separator
code_final=f'{".".join(code_slt)}{code_input}'
st.write(f'Your code: {code_final}')


# Executing string as a code in python
# reference: https://www.geeksforgeeks.org/execute-string-code-python/
result=eval(code_final)
st.write(result)