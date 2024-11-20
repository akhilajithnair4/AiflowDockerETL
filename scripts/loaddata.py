from scripts.transform import transform
import mysql.connector
from airflow.decorators import task
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook


@task 
def create_table():
    postgres_hook=PostgresHook(postgres_conn_id="postgres_connection")

    create_table_query="""
    CREATE TABLE IF NOT EXISTS weather(
        id SERIAL PRIMARY KEY,
        location VARCHAR(255),
        latitude FLOAT,
        longitude FLOAT,
        datetime TIMESTAMP,
        temperature FLOAT,
        weather_description VARCHAR(255) 
    )
"""

    postgres_hook.run(create_table_query)

@task
def load_data(data_dict):
    postgres_hook = PostgresHook(postgres_conn_id="postgres_connection")
    
    insert_query = """
    INSERT INTO weather(location, latitude, longitude, datetime, temperature, weather_description)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    values = (
        data_dict.get('location'),
        data_dict.get('latitude'),
        data_dict.get('longitude'),
        data_dict.get('datetime'),
        data_dict.get('temperature'),
        data_dict.get('weather_description')
    )

    # Use the `run` method with parameters
    postgres_hook.run(insert_query, parameters=values)




