import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Personal Email Lookup Endpoint")

st.write("Cost: 1 credit / email returned.")
st.write("Given an LinkedIn profile, returns a list of personal"
         "emails belonging to this identity. Emails are verified to be deliverable.")

api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-email'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER COMPANY LINKEDIN URL')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'email_validation': 'include',
      'linkedin_profile_url': company,
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
            df.to_csv('personal_email_endpoint.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "personal_email_endpoint.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
