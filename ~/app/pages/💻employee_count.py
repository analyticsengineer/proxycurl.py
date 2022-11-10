import requests
import streamlit as st

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



