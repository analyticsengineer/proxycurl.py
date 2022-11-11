import requests
import streamlit as st
from PIL import Image
from pathlib import Path
import json

image = Image.open('image2.png')
st.image(image)

st.title("Employee Count Endpoint")

st.write("Cost: 1 credit / successful request.")
st.write("Get a number of total employees of a Company.")
st.write("Get an employee count of this company from various sources.")

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/count/'

api_key = st.text_input('ENTER YOUR API KEY')
company = st.text_input('ENTER LINKEDIN COMPANY URL')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'linkedin_employee_count': 'include',
        'employment_status': 'current',
        'url': company,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.json(response)
    
    jsonFile = open("response.json", "w")
    #jsonFile.write(jsonString)
    jsonFile.close()

    if st.button('Convert To Csv File'):
        with open('response.json', 'r') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            df.to_csv('employee_end_point.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "employee_end_point.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')




