# Kiến trúc hệ thống

> Điền chi tiết ở Tuần 4 khi hệ thống đã hoàn chỉnh: sơ đồ đầy đủ, mô tả từng thành phần, luồng dữ liệu, cách các container giao tiếp qua Docker network.

## Thành phần (dự kiến)
- **crawler**: container Python, crawl dữ liệu, ghi vào `raw_jobs`
- **postgres**: lưu `raw_jobs` và `clean_jobs`
- **airflow**: orchestrate ETL (extract → transform → load) theo lịch hàng ngày
- **grafana**: dashboard trực quan hóa, đọc trực tiếp từ Postgres

## Sơ đồ
<!-- TODO: chèn ảnh sơ đồ hoặc vẽ bằng ASCII/mermaid ở tuần 4 -->

## Luồng dữ liệu
<!-- TODO -->
