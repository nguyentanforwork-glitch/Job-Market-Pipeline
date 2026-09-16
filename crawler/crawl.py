"""
Crawler chính — thu thập tin tuyển dụng IT.

Tuần 1 (DE):
- Viết logic crawl 1 trang tuyển dụng bằng BeautifulSoup
- Xử lý phân trang + time.sleep() giữa các request
- Lưu tạm ra CSV để test trước khi nối vào Postgres
"""
import os
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = os.getenv("CRAWL_BASE_URL", "https://example.com/jobs")
SLEEP_SECONDS = float(os.getenv("CRAWL_SLEEP_SECONDS", "1"))


def fetch_page(url: str) -> BeautifulSoup:
    # TODO: request + parse HTML
    raise NotImplementedError


def parse_job_listings(soup: BeautifulSoup) -> list[dict]:
    # TODO: trích xuất title, company, salary_raw, skills_raw, posted_date
    raise NotImplementedError


def save_to_csv(jobs: list[dict], path: str = "raw_jobs.csv") -> None:
    # TODO: dùng pandas hoặc csv module
    raise NotImplementedError


def main():
    # TODO: vòng lặp phân trang, gọi fetch_page -> parse_job_listings -> gom kết quả
    # TODO: sau khi ổn định, thay save_to_csv bằng insert thẳng vào Postgres (bảng raw_jobs)
    pass


if __name__ == "__main__":
    main()
