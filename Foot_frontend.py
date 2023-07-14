## https://www.wheeloratings.com/afl_stats.html to download csv

import streamlit as st
import pandas as pd
import numpy as np
import Foot_back as Fb

Fb.intro()
    
uploaded_file = st.file_uploader(" ")
if uploaded_file is not None:
    st.markdown("<h4 style='text-align: center; color: black;'>I ate the file...</h4>", unsafe_allow_html=True)

    Fb.run_program(uploaded_file)
else:
    st.markdown("<h4 style='text-align: center; color: black;'>Feed me file to work...</h4>", unsafe_allow_html=True)
    st.divider()




