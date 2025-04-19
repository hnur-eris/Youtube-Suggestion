-- Insert users
INSERT INTO users (email, username, hashed_password, is_active, created_at, updated_at) VALUES
('tech_enthusiast@example.com', 'tech_lover', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ai_researcher@example.com', 'ai_expert', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('data_scientist@example.com', 'data_analyst', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('data_engineer@example.com', 'big_data', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('web_developer@example.com', 'web_dev', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('frontend_dev@example.com', 'ui_expert', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('new_user1@example.com', 'newbie1', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('new_user2@example.com', 'newbie2', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert videos
INSERT INTO videos (title, description, url, thumbnail_url, category, duration, views, created_at, updated_at) VALUES
('Introduction to Machine Learning', 'Learn ML basics and applications', 'https://example.com/videos/ml-intro', 'https://example.com/thumbnails/ml-intro.jpg', 'AI', 1800, 1000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Deep Learning Fundamentals', 'Neural networks and deep learning', 'https://example.com/videos/deep-learning', 'https://example.com/thumbnails/deep-learning.jpg', 'AI', 5400, 800, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Machine Learning Projects', 'Practical ML project walkthroughs', 'https://example.com/videos/ml-projects', 'https://example.com/thumbnails/ml-projects.jpg', 'AI', 7200, 2000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Python Programming Tutorial', 'Python programming guide', 'https://example.com/videos/python-tutorial', 'https://example.com/thumbnails/python-tutorial.jpg', 'Programming', 3600, 2500, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Advanced Python Techniques', 'Advanced Python concepts', 'https://example.com/videos/advanced-python', 'https://example.com/thumbnails/advanced-python.jpg', 'Programming', 4500, 1200, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Data Science Projects', 'Data science using Python', 'https://example.com/videos/data-science', 'https://example.com/thumbnails/data-science.jpg', 'Data Science', 2700, 1500, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Big Data Processing', 'Big data processing guide', 'https://example.com/videos/big-data', 'https://example.com/thumbnails/big-data.jpg', 'Data Science', 4800, 900, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Web Development Basics', 'HTML, CSS, JavaScript basics', 'https://example.com/videos/web-dev', 'https://example.com/thumbnails/web-dev.jpg', 'Web Development', 2400, 3000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Modern Frontend Development', 'Advanced frontend techniques', 'https://example.com/videos/frontend', 'https://example.com/thumbnails/frontend.jpg', 'Web Development', 3600, 1800, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert user interactions
INSERT INTO user_interactions (user_id, video_id, watch_time, is_completed, rating) VALUES
-- Tech Enthusiast's watch history
(1, 1, 1800, true, 4.5),
(1, 2, 4000, false, 4.0),
(1, 4, 3600, true, 5.0),

-- AI Researcher's watch history
(2, 1, 1800, true, 4.8),
(2, 2, 5400, true, 4.9),
(2, 3, 6000, false, 4.5),

-- Data Scientist's watch history
(3, 6, 2700, true, 4.7),
(3, 7, 4000, false, 4.2),
(3, 4, 3000, false, 4.0),

-- Data Engineer's watch history
(4, 6, 2700, true, 4.6),
(4, 7, 4800, true, 4.8),
(4, 5, 3500, false, 4.3),

-- Web Developer's watch history
(5, 8, 2400, true, 4.7),
(5, 9, 3000, false, 4.0),
(5, 4, 2500, false, 4.2),

-- Frontend Developer's watch history
(6, 8, 2400, true, 4.9),
(6, 9, 3600, true, 4.8),
(6, 5, 2000, false, 4.1); 