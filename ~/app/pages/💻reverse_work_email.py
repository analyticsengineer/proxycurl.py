import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Reverse Work Email Lookup Endpoint")

st.write("Cost: 3 credits / successful request.")
st.write("Resolve LinkedIn Profile from a work email address")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve/email'

api_key = st.text_input('ENTER YOUR API KEY')
email = st.text_input('ENTER EMAIL ADDRESS')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
       'work_email': email,
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
            df.to_csv('reverse_email_endpoint.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "reverse_email_endpoint.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
