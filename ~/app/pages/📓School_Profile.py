import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("School Profile Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get structured data of a LinkedIn School Profile")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/school'

api_key = st.text_input('Enter your api key')
url = st.text_input('Enter school LinkedIn profile Url')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'url': url,
       'use_cache': 'if-present',
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    respond = st.write(response.json())
    st.write(respond)
    
    if st.button('📥 to csv'):
        with open('schoolrofile.json', 'w') as outfile:
            json.dump(respond, outfile)
            df = pd.read_json ('schoolprofile.json')
            df.to_csv ('schoolprofile.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = 'schoolprofile.csv'
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
