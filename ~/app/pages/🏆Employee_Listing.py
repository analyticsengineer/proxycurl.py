import requests
import streamlit as st
from PIL import Image
import re
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Employee Listing Endpoint")

st.write("Cost: 3 credits / employee returned.")
st.write("Get a list of employees of a Company.")
st.write("This API endpoint is limited by LinkDB which is populated with profiles in the US, UK, Canada, Israel, Australia, Ireland, New Zealand and Singapore." 
         "As such, this endpoint is best used to list employees working in companies based in those locations only.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'

api_key = st.text_input('Enter your api key')
company = st.text_input('Enter company LinkIn Url')
status_2 = st.text_input('Enter employee status(current, past)')
page_size1 = st.number_input('Enter page size')
role_search1 = st.text_input('Enter employee company role(founder, ceo)')

role1 = re.findall("\D", role_search1)

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'enrich_profiles': 'enrich',
        'role_search': role1,
        'page_size': page_size1,
        'employment_status': status_2,
        'resolve_numeric_id': 'false',
        'url': company,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    respond = st.write(response.json())
    st.write(respond)
    
    if st.button('📥 to csv'):
            df = pd.DataFrame(respond['employees'])
            df.to_csv ('employeelisting.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = 'employeelisting.csv'
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
