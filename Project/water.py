import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5xD5hKh_wzwIB0ojR7WOo__uvAvqJrktXQ66XcPxuAqb"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field":[["STATION CODE", "LOCATIONS", "STATE", "Temp", "D.O.", "PH", "CONDUCTIVITY", "B.O.D.", "NITRATENAN N+ NITRITENANN", "FECAL COLIFORM", "TOTAL COLIFORM", "year"]]     , "values":[[-0.67512366, -0.05584458, -0.20875388,  0.06397444,  0.89759086,
       -0.03841183,  0.64184078]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/84ebcda8-fa9d-4a58-b017-1faf38db51d3/predictions?version=2021-08-04', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
print(predictions['predictions'][0]['values'][0][0])