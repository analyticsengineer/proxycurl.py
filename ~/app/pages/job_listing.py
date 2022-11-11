import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Jobs Listing Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("List jobs posted by a company on LinkedIn")
st.write("The search_id of the company on LinkedIn."
         "You can get the search_id of a LinkedIn company via"
         "Company Profile API."

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'

api_key = st.text_input('ENTER YOUR API KEY')
search = st.text_input('ENTER COMPANY LINKEDIN SEARCH ID')


if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
      'search_id': search,
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
