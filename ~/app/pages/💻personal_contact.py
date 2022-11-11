import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Personal Contact Number Lookup Endpoint")

st.write("Cost: 1 credit / contact number returned.")
st.write("Given an LinkedIn profile, returns a list of personal contact numbers belonging to this identity.")

api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-contact'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER COMPANY LINKDIN URL')


if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
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
            df.to_csv('personal_contact_number.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "personal_contact_number.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
