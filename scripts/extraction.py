import pandas
import requests
from airflow.decorators import task

# The url and API key
# Task 1 Extraxct the data from weatherstack.com and store it in dictionary
@task
def extract(): 
    url="http://api.weatherstack.com//current"
    params = {
            "access_key": "623bef14b1aa2e99991fc1b862bf06f8",  # Replace with your actual API key
            "query": "Trivandrum"              # City for which you want weather data
        }

    response=requests.get(url,params=params)

    data=response.json()
    return data 
    


