"""
DAG chính của pipeline: extract -> transform -> load, chạy hàng ngày.
Tuần 2 (DE viết logic, DevOps kiểm tra DAG chạy ổn định qua Airflow UI).
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "jobmarket-team",
    "retries": 1,
}


def extract(**kwargs):
    # TODO: gọi crawler hoặc đọc dữ liệu mới từ raw_jobs
    pass


def transform(**kwargs):
    # TODO: parse lương, tách skills — xem crawler/crawl.py và hàm parse tương ứng
    pass


def load(**kwargs):
    # TODO: insert dữ liệu sạch vào bảng clean_jobs
    pass


with DAG(
    dag_id="job_market_pipeline",
    default_args=default_args,
    description="Extract -> Transform -> Load tin tuyển dụng IT",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["job-market", "etl"],
) as dag:

    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    load_task = PythonOperator(task_id="load", python_callable=load)

    extract_task >> transform_task >> load_task
