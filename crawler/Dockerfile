FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# TODO (Tuần 1): entrypoint sẽ chạy script crawl chính, ví dụ crawl.py
CMD ["python", "crawl.py"]
