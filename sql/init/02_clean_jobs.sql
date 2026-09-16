-- Tuần 2: bảng chứa dữ liệu đã làm sạch
CREATE TABLE IF NOT EXISTS clean_jobs (
    id SERIAL PRIMARY KEY,
    raw_job_id INTEGER REFERENCES raw_jobs(id),
    title TEXT,
    company TEXT,
    salary_min NUMERIC,
    salary_max NUMERIC,
    skills TEXT[],       -- list các skill đã tách
    posted_date DATE,
    cleaned_at TIMESTAMP DEFAULT NOW()
);
