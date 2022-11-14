import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('proxycurl.png')
st.image(image)

st.title("Jobs Listing Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("List jobs posted by a company on LinkedIn")
st.write("The search_id of the company on LinkedIn."
         "You can get the search_id of a LinkedIn company via"
         "Company Profile API.")

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'

api_key = st.text_input('Enter your api key')
search = st.text_input('Enter LinkedIn company search Id')


if st.button('📥'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'search_id': search,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    respond = st.write(response.json())
    st.write(respond)
    
    if st.button('📥 to csv'):
        with open('joblisting.json', 'w') as outfile:
            json.dump(respond, outfile)
            df = pd.read_json ('joblisting.json')
            df.to_csv ('joblisting.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = 'joblisting.csv'
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
                      
