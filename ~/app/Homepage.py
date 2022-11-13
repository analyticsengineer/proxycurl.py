from PIL import Image
import streamlit as st

# setting image
image = Image.open('image.png')
image2 = Image.open('proxycurl.png')

col1, col2 = st.columns(2)
col1.image(image2)

col1.title("Proxy Curl - Linkedin API")
title_1 =  '<p style="font-family:sans-serif; color:White;">This Web App is built for Non programmers</p>'
col1.markdown(title_1, unsafe_allow_html=True)
title_2 =  '<p style="font-family:sans-serif; color:White;">Who would like to use Proxycurl API.</p>'
col1.markdown(title_2, unsafe_allow_html=True)
col2.image(image)

col1.write("[![Project Page](https://img.icons8.com/ios-glyphs/20/ffffff/github.png)](https://github.com/anuoluwapods/proxycurl.py) Github Page") 
col1.write("[![Instagram page](https://img.icons8.com/fluency/20/null/instagram-new.png)](https://instagram.com/anuoluwapods) Instagram page")
col1.write("[![Instagram page](https://img.icons8.com/color/20/null/twitter--v1.png)](https://twitter.com/AnuoluwapoDs) Twitter Page")
col1.write("[![Instagram page](https://img.icons8.com/color/20/null/linkedin.png)](https://www.linkedin.com/in/anuoluwapo-abiodun-balogun-64b977186/) Linkedin Page")
col1.write("[![Instagram page](https://img.icons8.com/fluency/20/null/facebook-new.png)](https://facebook.com/ifeoluwapo.balogun) Facebook Page")

