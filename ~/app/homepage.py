from PIL import Image
import streamlit as st

# setting image
image = Image.open('image.png')

col1, col2 = st.columns(2)

col1.header("Proxy Curl - Linkedin API")
title_1 =  '<p style="font-family:sans-serif; color:White;">This Web App is built for</p>'
col1.markdown(title_1, unsafe_allow_html=True)
title_2 =  '<p style="font-family:sans-serif; color:White;">Non programmers who want to use Proxycurl API.</p>'
col1.markdown(title_2, unsafe_allow_html=True)
col2.image(image)

