import requests
import streamlit as st

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/count/'
api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER COMPANY LINKEDIN URL')

st.write(requests.get(company).json())
