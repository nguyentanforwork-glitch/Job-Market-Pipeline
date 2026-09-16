-- Tuần 1: bảng chứa dữ liệu thô crawl được
CREATE TABLE IF NOT EXISTS raw_jobs (
    id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    salary_raw TEXT,
    skills_raw TEXT,
    posted_date TEXT,
    crawled_at TIMESTAMP DEFAULT NOW()
);
