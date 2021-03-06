DROP TABLE IF EXISTS Pages CASCADE;
CREATE TABLE Pages (id SERIAL PRIMARY KEY, url VARCHAR, is_scraping BOOLEAN DEFAULT FALSE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
DROP TABLE IF EXISTS Links CASCADE;
CREATE TABLE Links (id SERIAL PRIMARY KEY, page_id INTEGER , url VARCHAR, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (page_id) REFERENCES Pages(id));