import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Jobs Listing Count Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Count number of jobs posted by a company on LinkedIn")


api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job/count'

api_key = st.text_input('Enter your api key')
searc = st.text_input('Enter LinkedIn company search Id')
keyword = st.text_input('Enter job title')
geo_1 = st.text_input('Enter company geo id')
jobs_1 = st.text_input('Enter job flexibility(remote, full-time, part-time, contract)')
when_1 = st.text_input('Enter job time frame(past-month, this-month, today)')



if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'when': when_1,
       'flexibility': jobs_1,
       'geo_id': geo_1,
       'keyword': keyword,
       'search_id': searc,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    respond = st.write(response.json())
    st.write(respond)

    
   
