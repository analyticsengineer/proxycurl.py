import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Company Lookup Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Resolve Company LinkedIn Profile from company name, domain name and location.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/resolve'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER COMPANY URL')
name =  st.text_input('ENTER COMPANY NAME')
location =  st.text_input('ENTER COMPANY LOCATION')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'company_location': location,
       'company_domain': company,
       'company_name': name,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
