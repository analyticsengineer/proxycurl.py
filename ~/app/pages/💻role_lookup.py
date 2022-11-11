import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Role Lookup Endpoint")

st.write("Cost: 3 credits / successful request.")
st.write("Finds the closest (person) profile with a given role in a Company."
         "For example, you can use this endpoint to find the CTO of Apple. This API endpoint returns only one result that is the closest match."
         "There is also a role search under the Employee Listing Endpoint if you require:"
         "precision on the target company"
         "a list of employees that matches a role (instead of one result).")

api_endpoint = 'https://nubela.co/proxycurl/api/find/company/role'

api_key = st.text_input('ENTER YOUR API KEY')
role = st.text_input('ENTER USER ROLE IN COMPANY')
name = st.text_input('ENTER COMPANY NAME')


if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'role': role,
      'company_name': name,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
