```sql
-- src/database/init_db.sql

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128)
);

-- Create scan_results table
CREATE TABLE scan_results (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    api_id VARCHAR(64) NOT NULL,
    cloud_provider VARCHAR(64) NOT NULL,
    scan_date TIMESTAMP NOT NULL,
    vulnerabilities TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```
