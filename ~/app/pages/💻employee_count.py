import requests
import streamlit as st

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/count/'
api_key = st.text_input('ENTER YOUR API KEY')
