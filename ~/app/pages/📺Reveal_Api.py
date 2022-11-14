import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Reveal Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Deanonymize an IPv4 address and associate the Company behind the IPv4 address.")

api_endpoint = 'https://nubela.co/proxycurl/api/reveal/company'

api_key = st.text_input('Enter your api')
role = st.text_input('Enter user company job role')
ip = st.text_input('Enter user IPV4 address')

if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'role_contact_number': 'include',
        'role_personal_email': 'include',
        'role': role,
        'ip': ip,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    respond = st.write(response.json())
    st.write(respond)
    
    if st.button('📥 to csv'):
        with open('revealapi.json', 'w') as outfile:
            json.dump(respond, outfile)
            df = pd.read_json ('revealapi.json')
            df.to_csv ('revealapi.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = 'revealapi.csv'
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
