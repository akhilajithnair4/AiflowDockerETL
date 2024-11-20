from scripts.extraction import extract
from scripts.transform import transform
from scripts.loaddata import load_data,create_table
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago
from airflow.decorators import task


with DAG(
    dag_id="weather_data_postgres",
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False
) as dag:
   
   

    # Define task dependencies
    create_table()
    data=extract() 
    transformed_data=transform(data)
    load_data(transformed_data)

    


