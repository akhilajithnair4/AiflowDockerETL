import pandas
from scripts.extraction import extract
from airflow.decorators import task

# Task2  Transform the data 
@task
def transform(data):
   

    data_dict={}

    data_dict['location']=data.get('location').get('name')
    data_dict['latitude']=data.get('location').get('lat')
    data_dict['longitude']=data.get('location').get('lon')
    data_dict['datetime']=data.get('location').get('localtime')
    data_dict['temperature']=data.get('current').get('temperature')
    data_dict['weather_description']=data.get('current').get('weather_descriptions')[0]

    return data_dict

