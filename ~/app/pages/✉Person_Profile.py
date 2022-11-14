import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Person Profile Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get structured data of a Personal Profile.")

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

api_key = st.text_input('Enter your api key')
url = st.text_input('Enter user LinkedIn profile Url')


if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
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
    respond = st.write(response.json())
    st.write(respond)
    
    if st.button('📥 to csv'):
        with open("personprofile.json", "w") as outfile:
            json.dump(respond, outfile)
            df = pd.read_json (r'personprofile.json')
            df.to_csv (r'personprofile.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = 'company_profile_endpoint.csv'
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
