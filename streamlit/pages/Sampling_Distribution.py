import streamlit as st
import pandas as pd
import matplotlib as map
import matplotlib.pyplot as plt
from func.chart import sample_dist_chart
from func.model import sample_dist_cal
from template import side_background

# Sidebar Config
# st.set_page_config(page_title="Plotting Demo", page_icon="📈")

side_background()

# ---. Description & Config
st.sidebar.header("Sampling Distribution")
st.markdown("# Sampling and Sampling Distribution")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# ---. Session State Control

if 'counter' not in st.session_state:
    st.session_state.counter = 0
    a=[]
    
if 'samples' not in st.session_state:
    # Session state to save 'samples'
    st.session_state.samples = []
    # Session state to unnest and print 'samples'
    st.session_state.samples_print = "empty"
    
if 'sample_mean' not in st.session_state:
    # Session state to save 'sample_mean'
    st.session_state.sample_mean = []
    # Session state to unnest and print 'sample_mean'
    st.session_state.sample_mean_print = "empty"
    
if 'chart' not in st.session_state:
    st.session_state.chart = "empty"
    
# ---. Inputs
c1, c2, c3 = st.columns(3)
with c1:
    button1 = st.button('Increment(by One)')
with c2:
    button2 = st.button('Increment(by 10)')
with c3:
    button3 = st.button('Reset')

if button1:
    
    # Update session state counter by 1 for every click
    st.session_state.counter += 1
    a=sample_dist_cal(30,1,"EAI","Annual_Salary")
    st.session_state.samples.append(a[0])
    st.session_state.samples_print=[num for sublist in st.session_state.samples for num in sublist]
    st.session_state.sample_mean.append(a[1])
    st.session_state.sample_mean_print=[num for sublist in st.session_state.sample_mean for num in sublist]
    # Previous chart with different highlight color
    st.session_state.sample_mean_print_pre=st.session_state.sample_mean_print[:len(st.session_state.sample_mean_print)-1]
    fig=sample_dist_chart(30,
                          st.session_state.counter,
                          st.session_state.samples_print[st.session_state.counter-1],
                          st.session_state.sample_mean_print,
                          st.session_state.sample_mean_print_pre,
                          15)
    st.session_state.chart=fig

    
if button2:
    # Update session state counter by 10 for every click
    st.session_state.counter += 10
    a=sample_dist_cal(30,10,"EAI","Annual_Salary")
    st.session_state.samples.append(a[0])
    st.session_state.samples_print=[num for sublist in st.session_state.samples for num in sublist]
    st.session_state.sample_mean.append(a[1])
    st.session_state.sample_mean_print=[num for sublist in st.session_state.sample_mean for num in sublist]
    # Previous chart with different highlight color
    st.session_state.sample_mean_print_pre=st.session_state.sample_mean_print[:len(st.session_state.sample_mean_print)-10]
    fig=sample_dist_chart(30,
                          st.session_state.counter,
                          st.session_state.samples_print[st.session_state.counter-1],
                          st.session_state.sample_mean_print,
                          st.session_state.sample_mean_print_pre,
                          15)
    st.session_state.chart=fig
    
if button3:
    a=[]
    st.session_state.counter = 0
    st.session_state.samples = []
    st.session_state.samples_print = []
    st.session_state.sample_mean = []
    st.session_state.chart = "empty"
    



# ---. Output Display

st.write('Counter = ', st.session_state.counter)

# Tabs
tab1, tab2, tab3 = st.tabs(["Samples", 
                      "Sampling Distribution", 
                      "Charts"])
with tab1:
    st.write(st.session_state.samples_print)
    st.write(a[0])
with tab2:
    st.write(st.session_state.sample_mean_print)
    
with tab3:
    st.pyplot(st.session_state.chart[2])
    #st.write(a[1])
    st.write(st.session_state.sample_mean_print_pre)
    #st.write(st.session_state.chart)
