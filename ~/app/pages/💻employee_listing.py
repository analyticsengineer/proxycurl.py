import requests
import streamlit as st
from PIL import Image
from pathlib import Path
import json

image = Image.open('image2.png')
st.image(image)

st.title("Employee Listing Endpoint")

st.write("Cost: 3 credits / employee returned.")
st.write("Get a list of employees of a Company.")
st.write("This API endpoint is limited by LinkDB which is populated with profiles in the US, UK, Canada, Israel, Australia, Ireland, New Zealand and Singapore." 
         "As such, this endpoint is best used to list employees working in companies based in those locations only.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER LINKEDIN COMPANY URL')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'enrich_profiles': 'enrich',
        'role_search': '[Ff][Oo][Uu][Nn][Dd][Ee][Rr]',
        'page_size': '100',
        'employment_status': 'current',
        'resolve_numeric_id': 'false',
        'url': company,
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
            df.to_csv('employee_listing_endpoint.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "employee_listing_endpoint.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
