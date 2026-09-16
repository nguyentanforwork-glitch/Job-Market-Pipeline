# Roadmap 4 tuần — Job Market Pipeline

Thời gian: 4 tuần, ~2-4 tiếng/ngày/người.

## Tuần 1 — Nền tảng & crawl dữ liệu thô
**Cột mốc:** `docker compose up` chạy crawler tự lấy dữ liệu và lưu vào Postgres.

| Ngày | DE | DevOps |
|---|---|---|
| T2-T3 | Script crawl 1 trang (BeautifulSoup), ~50-100 tin, in console | Ôn Docker: build/run 1 image đơn giản |
| T4-T5 | Xử lý phân trang, `time.sleep()`, lưu CSV | Viết `Dockerfile` cho crawler |
| T6-CN | Cài Postgres, thiết kế bảng `raw_jobs` | Viết `docker-compose.yml`: `postgres` + `crawler`, volume, `.env` |

## Tuần 2 — Làm sạch dữ liệu & lên lịch
**Cột mốc:** Airflow UI truy cập được, DAG tự chạy đúng giờ, dữ liệu sạch nằm trong `clean_jobs`.

| Ngày | DE | DevOps |
|---|---|---|
| T2-T3 | Parse lương, tách skills thành list | Cài Airflow qua Docker Compose (`LocalExecutor`) |
| T4-T5 | Lưu vào `clean_jobs`, viết unit test | Kết nối Airflow ↔ Postgres, cấu hình network |
| T6-CN | Gộp extract→transform→load thành DAG, schedule hàng ngày | Kiểm tra DAG ổn định, health check cơ bản |

## Tuần 3 — CI + Deploy
**Cột mốc:** CI chạy test tự động, đã deploy thật lên server, truy cập được từ xa.

| Ngày | DE | DevOps |
|---|---|---|
| T2-T3 | SQL tổng hợp: lương TB theo ngôn ngữ, top 15 skill, số tin/tuần | GitHub Actions: push → chạy `flake8` + unit test |
| T4-T5 | Log rõ ràng khi DAG lỗi | Tạo VM free tier, SSH, mở port |
| T6-CN | Kiểm tra lại pipeline | Deploy thủ công 1 lần, có link/IP truy cập Airflow UI |

## Tuần 4 — Dashboard & hoàn thiện
**Cột mốc cuối:** Project chạy được, có dashboard, có link demo, README đầy đủ.

| Ngày | DE | DevOps |
|---|---|---|
| T2-T3 | Dashboard Grafana nối trực tiếp Postgres | Hỗ trợ setup Grafana qua Docker Compose, data source |
| T4-T5 | "Lessons learned" — 2-3 lỗi + cách xử lý | `TROUBLESHOOTING.md`, dọn code, xóa thông tin nhạy cảm |
| T6-CN | **Cùng nhau:** README hoàn chỉnh (kiến trúc, hướng dẫn chạy, ảnh dashboard, phân chia việc) | |

## 3 nguyên tắc
1. Commit đều mỗi ngày, dù chỉ 1-2 dòng.
2. Ghi lại lỗi khi gặp vào `TROUBLESHOOTING.md`.
3. Ưu tiên hoàn thiện hơn thêm tính năng.
