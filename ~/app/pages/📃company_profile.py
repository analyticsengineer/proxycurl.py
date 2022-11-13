import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Company Profile Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get structured data of a Company Profile")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'

api_key = st.text_input('Enter your api')
company = st.text_input('Enter company LinkedIn Url')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'resolve_numeric_id': 'true',
       'categories': 'include',
       'funding_data': 'include',
       'extra': 'include',
       'exit_data': 'include',
       'acquisitions': 'include',
       'url': company,
       'use_cache': 'if-present',
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
    
   
   

    if st.button('📥 to csv'):
        jsonFile = open("response.json", "w")
        jsonFile.close()
        with open('response.json', 'r') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            df.to_csv('company_profile_endpoint.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "company_profile_endpoint.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
