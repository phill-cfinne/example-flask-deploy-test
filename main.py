-- main - Database Schema for example-flask-deploy-test
-- Created: $(date)

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts table
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(200) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_posts_user_id ON posts(user_id);
CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at);

-- Sample data insertion
INSERT INTO users (username, email, password_hash) VALUES
('john_doe', 'john@example.com', 'hashed_password_123'),
('jane_smith', 'jane@example.com', 'hashed_password_456');

INSERT INTO posts (user_id, title, content) VALUES
(1, 'First Post', 'This is the content of the first post.'),
(2, 'Welcome Post', 'Welcome to our application!');

-- Useful queries
-- Get all posts with user information
SELECT
    p.title,
    p.content,
    p.created_at,
    u.username
FROM posts p
JOIN users u ON p.user_id = u.id
ORDER BY p.created_at DESC;

-- Get user post count
SELECT
    u.username,
    COUNT(p.id) as post_count
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
GROUP BY u.id, u.username;

# Additional Implementation 1760503184

# Additional Implementation 1760503184

# Code Update 1760503184-10342

# Code Update 1760503184-2276

# Additional Implementation 1760503184

# Additional Implementation 1760503184

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Code Update 1760503185-13057

# Code Update 1760503185-11677

# Code Update 1760503185-8686

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Code Update 1760503185-12107

# Additional Implementation 1760503185

# Additional Implementation 1760503185

# Additional Implementation 1760503186

# Additional Implementation 1760503186

# Additional Implementation 1760503186

# Additional Implementation 1760503186

# Code Update 1760503186-18941

# Additional Implementation 1760503186

# Additional Implementation 1760503186

# Code Update 1760503186-7204

# Code Update 1760503186-27191

# Additional Implementation 1760503186

# Additional Implementation 1760503186

# Code Update 1760503186-15920

# Additional Implementation 1760503186

# Code Update 1760503186-19045

# Additional Implementation 1760503187

# Additional Implementation 1760503187

# Code Update 1760503187-18297

# Additional Implementation 1760503187

# Code Update 1760503187-28441

# Code Update 1760503187-21136

# Code Update 1760503188-4323

# Additional Implementation 1760503188

# Code Update 1760503188-4632

# Additional Implementation 1760503188

# Additional Implementation 1760503188

# Code Update 1760503188-27011

# Code Update 1760503188-20076

# Code Update 1760503188-19273

# Code Update 1760503188-29583

# Additional Implementation 1760503189

# Additional Implementation 1760503189

# Code Update 1760503189-17956

# Additional Implementation 1760503189

# Additional Implementation 1760503189

# Additional Implementation 1760503189

# Code Update 1760503189-1074

# Code Update 1760503189-25979

# Additional Implementation 1760503189

# Code Update 1760503189-28519

# Code Update 1760503189-17421

# Additional Implementation 1760503189

# Additional Implementation 1760503189

# Additional Implementation 1760503190

# Additional Implementation 1760503190

# Additional Implementation 1760503190

# Additional Implementation 1760503190
