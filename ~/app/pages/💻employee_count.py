import requests
import streamlit as st
from PIL import Image

image = Image.open('image2.png')
st.image(image)

st.write("Cost: 1 credit / successful request.")
st.write("Get a number of total employees of a Company.")
st.write("Get an employee count of this company from various sources.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/count/'
api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER LINKEDIN COMPANY URL')

header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_employee_count': 'include',
    'employment_status': 'current',
    'url': company,
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

st.write(response.json)



