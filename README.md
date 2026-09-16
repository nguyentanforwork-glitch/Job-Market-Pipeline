# Job Market Pipeline

Thu thập & phân tích dữ liệu tuyển dụng IT — pipeline end-to-end (crawl → clean → orchestrate → dashboard).

> 📌 File này sẽ được viết lại hoàn chỉnh ở Tuần 4 (sơ đồ kiến trúc, hướng dẫn chạy, ảnh dashboard, phân chia công việc). Bản dưới đây chỉ là khung sườn ban đầu.

## Thành viên
- **[Tên bạn]** — DevOps: Docker, Airflow infra, CI/CD, deploy, monitoring
- **[Tên bạn học]** — Data Engineer: crawl, clean data, transform, DAG logic, SQL, dashboard queries

## Kiến trúc (tạm thời — cập nhật ở tuần 4)

```
[Website tuyển dụng] --crawl--> [crawler container] --> [Postgres: raw_jobs]
                                                              |
                                                        [Airflow DAG]
                                                     extract -> transform -> load
                                                              |
                                                       [Postgres: clean_jobs]
                                                              |
                                                        [Grafana dashboard]
```

## Cách chạy (cập nhật dần theo từng tuần)

```bash
cp .env.example .env   # điền secrets/config trước khi chạy
docker compose up -d
```

- Airflow UI: http://localhost:8080
- Grafana: http://localhost:3000

## Tiến độ theo tuần

- [ ] Tuần 1 — Nền tảng & crawl dữ liệu thô
- [ ] Tuần 2 — Làm sạch dữ liệu & lên lịch (Airflow DAG)
- [ ] Tuần 3 — CI + Deploy lên VM
- [ ] Tuần 4 — Dashboard & hoàn thiện

## Tài liệu liên quan
- [ROADMAP.md](./ROADMAP.md) — kế hoạch chi tiết 4 tuần, chia việc theo người
- [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) — lỗi đã gặp & cách xử lý
- [docs/architecture.md](./docs/architecture.md) — sơ đồ kiến trúc chi tiết (viết ở tuần 4)
