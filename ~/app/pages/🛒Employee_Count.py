import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Employee Count Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get a number of total employees of a Company.")
st.write("Get an employee count of this company from various sources.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/count/'

api_key = st.text_input('Enter your api key')
company = st.text_input('Enter company LinkedIn Url')
status = st.text_input('Enter employee status(current, past)')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'linkedin_employee_count': 'include',
        'employment_status': status,
        'url': company,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)
   

    st.write(response.json())

