import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Person Profile Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get structured data of a Personal Profile.")

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

api_key = st.text_input('ENTER YOUR API KEY')
url = st.text_input('ENTER USER LINKEDIN PROFILE LINK')


if st.button('Get Data'):
    params = {
        'url': url,
        'fallback_to_cache': 'on-error',
        'use_cache': 'if-present',
        'skills': 'include',
        'inferred_salary': 'include',
        'personal_email': 'include',
        'personal_contact_number': 'include',
        'twitter_profile_id': 'include',
        'facebook_profile_id': 'include',
        'github_profile_id': 'include',
        'extra': 'include',
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)
    st.write(response.json())
    
    jsonFile = open("response.json", "w")
    #jsonFile.write(jsonString)
    jsonFile.close()

    if st.button('Convert To Csv File'):
        with open('response.json', 'r') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            df.to_csv('personal_profile.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "personal_profile.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
