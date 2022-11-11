import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Person Lookup Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Resolve LinkedIn Profile")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'

api_key = st.text_input('ENTER YOUR API KEY')
url = st.text_input('ENTER COMPANY URL')
location = st.text_input('ENTER USER LOCATION')
title = st.text_input('ENTER USER COMPANY TITLE')
last = st.text_input('ENTER USER LAST NAME')
first = st.text_input('ENTER USER FIRST NAME')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'company_domain': url,
      'location': location,
      'title': title,
      'last_name': last,
      'first_name': first,
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
            df.to_csv('company_lookup_endpoint.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "company_lookup_endpoint.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')