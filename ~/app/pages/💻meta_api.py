import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Meta API")

st.write("Cost: 0 credit / successful request.")
st.write("Get your current credit(s) balance")

api_endpoint = 'https://nubela.co/proxycurl/api/credit-balance'

api_key = st.text_input('ENTER YOUR API KEY')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    response = requests.get(api_endpoint,
                        headers=header_dic)

    st.write(response.json())
