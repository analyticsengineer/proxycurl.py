import requests
import streamlit as st
from PIL import Image

image = Image.open('image2.png')
st.image(image)

st.title("Company Profile Picture Endpoint")

st.write("Cost: 0 credit / successful request.")
st.write("Get the profile picture of a company")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/profile-picture'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER LINKEDIN COMPANY URL')

if st.button('Get Data'):
  header_dic = {'Authorization': 'Bearer ' + api_key}
  params = {
     'linkedin_company_profile_url': 'https://www.linkedin.com/company/apple/',
  }
  response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response)
    
    with open("profile_image.png", "rb") as file:
      btn = st.download_button(
            label="Download image",
            data=file,
            file_name="profile_image.png",
            mime="image/png"
          )
