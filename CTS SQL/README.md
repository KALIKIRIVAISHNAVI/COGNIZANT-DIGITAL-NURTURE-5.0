# ANSI SQL Using MySQL – 25 SQL Practice Questions

This repository contains solutions for 25 ANSI SQL practice questions based on an Event Management Database schema consisting of:

- Users
- Events
- Sessions
- Registrations
- Feedback
- Resources

The exercises cover SQL concepts such as:

- Joins
- Aggregation
- GROUP BY
- HAVING
- Subqueries
- CTEs
- Date Functions
- Window Analysis
- Data Validation
- Reporting Queries

---

# Samlpe DataSet

## Crete Table:
### Code:
```


CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    city VARCHAR(100) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    status ENUM('upcoming','completed','cancelled'),
    organizer_id INT,
    FOREIGN KEY (organizer_id) REFERENCES Users(user_id)
);

CREATE TABLE Sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    title VARCHAR(200) NOT NULL,
    speaker_name VARCHAR(100) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    registration_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Resources (
    resource_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    resource_type ENUM('pdf','image','link'),
    resource_url VARCHAR(255) NOT NULL,
    uploaded_at DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);
```
### Output:
<img width="1600" height="258" alt="WhatsApp Image 2026-06-03 at 9 31 02 PM" src="https://github.com/user-attachments/assets/38864013-1bbf-4004-b9e2-d1f83a887c6c" />

## Insert Data
### Code:
```
INSERT INTO Users (user_id, full_name, email, city, registration_date) VALUES
(1, 'Alice Johnson', 'alice@example.com', 'New York', '2024-12-01'),
(2, 'Bob Smith', 'bob@example.com', 'Los Angeles', '2024-12-05'),
(3, 'Charlie Lee', 'charlie@example.com', 'Chicago', '2024-12-10'),
(4, 'Diana King', 'diana@example.com', 'New York', '2025-01-15'),
(5, 'Ethan Hunt', 'ethan@example.com', 'Los Angeles', '2025-02-01');

INSERT INTO Events
(event_id, title, description, city, start_date, end_date, status, organizer_id)
VALUES
(1,
'Tech Innovators Meetup',
'A meetup for tech enthusiasts.',
'New York',
'2025-06-10 10:00:00',
'2025-06-10 16:00:00',
'upcoming',
1),

(2,
'AI & ML Conference',
'Conference on AI and ML advancements.',
'Chicago',
'2025-05-15 09:00:00',
'2025-05-15 17:00:00',
'completed',
3),

(3,
'Frontend Development Bootcamp',
'Hands-on training on frontend tech.',
'Los Angeles',
'2025-07-01 10:00:00',
'2025-07-03 16:00:00',
'upcoming',
2);

INSERT INTO Sessions
(session_id, event_id, title, speaker_name, start_time, end_time)
VALUES
(1,
1,
'Opening Keynote',
'Dr. Tech',
'2025-06-10 10:00:00',
'2025-06-10 11:00:00'),

(2,
1,
'Future of Web Dev',
'Alice Johnson',
'2025-06-10 11:15:00',
'2025-06-10 12:30:00'),

(3,
2,
'AI in Healthcare',
'Charlie Lee',
'2025-05-15 09:30:00',
'2025-05-15 11:00:00'),

(4,
3,
'Intro to HTML5',
'Bob Smith',
'2025-07-01 10:00:00',
'2025-07-01 12:00:00');

INSERT INTO Registrations
(registration_id, user_id, event_id, registration_date)
VALUES
(1, 1, 1, '2025-05-01'),
(2, 2, 1, '2025-05-02'),
(3, 3, 2, '2025-04-30'),
(4, 4, 2, '2025-04-28'),
(5, 5, 3, '2025-06-15');

INSERT INTO Feedback
(feedback_id, user_id, event_id, rating, comments, feedback_date)
VALUES
(1,
3,
2,
4,
'Great insights!',
'2025-05-16'),

(2,
4,
2,
5,
'Very informative.',
'2025-05-16'),

(3,
2,
1,
3,
'Could be better.',
'2025-06-11');

INSERT INTO Resources
(resource_id, event_id, resource_type, resource_url, uploaded_at)
VALUES
(1,
1,
'pdf',
'https://portal.com/resources/tech_meetup_agenda.pdf',
'2025-05-01 10:00:00'),

(2,
2,
'image',
'https://portal.com/resources/ai_poster.jpg',
'2025-04-20 09:00:00'),

(3,
3,
'link',
'https://portal.com/resources/html5_docs',
'2025-06-25 15:00:00');
```
### Output
<img width="1600" height="251" alt="WhatsApp Image 2026-06-03 at 9 32 41 PM" src="https://github.com/user-attachments/assets/9727f1d0-5841-4fcd-980f-3e39f643ed72" />

# SQL Exercises

## 1. User Upcoming Events
### Problem Statement
List the top 5 users who have submitted the most feedback entries.
### Query
```
SELECT u.full_name, e.title, e.city, e.start_date
FROM Users u
JOIN Registrations r ON u.user_id = r.user_id
JOIN Events e ON r.event_id = e.event_id
WHERE e.status = 'upcoming'
AND u.city = e.city
ORDER BY e.start_date;
```
### Output
<img width="941" height="348" alt="WhatsApp Image 2026-06-03 at 2 08 23 PM" src="https://github.com/user-attachments/assets/8db1b83d-db35-4ea3-b429-0eb0edd85c69" />

## 2. Top Rated Events
### Problem Statement
Identify events with the highest average rating, considering only those that have received at 
least 10 feedback submissions.
### Query
```
SELECT e.event_id, e.title, AVG(f.rating) AS avg_rating
FROM Events e
JOIN Feedback f ON e.event_id = f.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(f.feedback_id) >= 10
ORDER BY avg_rating DESC;
```
### Output
Empty Set
<img width="942" height="357" alt="WhatsApp Image 2026-06-03 at 2 08 49 PM" src="https://github.com/user-attachments/assets/1615ac40-3d59-414a-9690-ccd4669ec8a6" />

## 3. Inactive Users
### Problem Statement
Retrieve users who have not registered for any events in the last 90 days.
### Query
```
SELECT u.*
FROM Users u
LEFT JOIN Registrations r
ON u.user_id = r.user_id
AND r.registration_date >= CURDATE() - INTERVAL 90 DAY
WHERE r.registration_id IS NULL;
```
### Output
<img width="931" height="328" alt="WhatsApp Image 2026-06-03 at 2 10 33 PM" src="https://github.com/user-attachments/assets/fe82cf71-5307-4e33-bde8-cc6cc851de29" />

## 4. Peak Session Hours
### Problem Statement
Count how many sessions are scheduled between 10 AM to 12 PM for each event. 
### Query
```
SELECT e.title,
COUNT(s.session_id) AS session_count
FROM Events e
LEFT JOIN Sessions s
ON e.event_id = s.event_id
WHERE TIME(s.start_time) BETWEEN '10:00:00' AND '12:00:00'
GROUP BY e.event_id, e.title;
```
### Output
<img width="935" height="341" alt="WhatsApp Image 2026-06-03 at 2 27 34 PM" src="https://github.com/user-attachments/assets/2443300d-6bde-400b-aa61-75bacb43bcf0" />

## 5. Most Active Cities
### Problem Statement
List the top 5 cities with the highest number of distinct user registrations.
### Query
```
SELECT u.city,
COUNT(DISTINCT r.user_id) AS registrations
FROM Users u
JOIN Registrations r
ON u.user_id = r.user_id
GROUP BY u.city
ORDER BY registrations DESC
LIMIT 5;
```
### Output
<img width="931" height="324" alt="WhatsApp Image 2026-06-03 at 2 37 22 PM" src="https://github.com/user-attachments/assets/d82d19e8-ce58-4d25-8dc3-7d779a1f87c7" />

## 6. Event Resource Summary
### Problem Statement
### Query
```
SELECT e.title,
SUM(CASE WHEN r.resource_type='pdf' THEN 1 ELSE 0 END) AS pdf_count,
SUM(CASE WHEN r.resource_type='image' THEN 1 ELSE 0 END) AS image_count,
SUM(CASE WHEN r.resource_type='link' THEN 1 ELSE 0 END) AS link_count
FROM Events e
LEFT JOIN Resources r
ON e.event_id = r.event_id
GROUP BY e.event_id, e.title;
```
### Output
<img width="929" height="320" alt="image" src="https://github.com/user-attachments/assets/5e5af296-a074-43b1-9e07-7785aab4fe2c" />


## 7. Low Feedback Alerts
### Problem Statement
### Query
```
SELECT u.full_name,
f.comments,
e.title
FROM Feedback f
JOIN Users u ON f.user_id = u.user_id
JOIN Events e ON f.event_id = e.event_id
WHERE f.rating < 3;

```
### Output
<img width="938" height="332" alt="WhatsApp Image 2026-06-03 at 5 20 00 PM" src="https://github.com/user-attachments/assets/1dc176b5-9312-4e07-8f89-6176d8e84901" />

## 8. Sessions per Upcoming Event
### Problem Statement
### Query
```
SELECT e.title,
COUNT(s.session_id) AS total_sessions
FROM Events e
LEFT JOIN Sessions s
ON e.event_id = s.event_id
WHERE e.status='upcoming'
GROUP BY e.event_id, e.title;
```
### Output
<img width="936" height="318" alt="WhatsApp Image 2026-06-03 at 5 20 56 PM" src="https://github.com/user-attachments/assets/a997e599-ab28-4959-8616-129a749f04b7" />

## 9. Organizer Event Summary
### Problem Statement
### Query
```
SELECT u.full_name,
e.status,
COUNT(e.event_id) AS total_events
FROM Users u
JOIN Events e
ON u.user_id = e.organizer_id
GROUP BY u.full_name, e.status;
```
### Output
<img width="935" height="328" alt="WhatsApp Image 2026-06-03 at 5 21 45 PM" src="https://github.com/user-attachments/assets/2fbf0424-7162-45f4-905c-758d4e7014d3" />

## 10. Feedback Gap
### Problem Statement
### Query
```
SELECT DISTINCT e.title
FROM Events e
JOIN Registrations r
ON e.event_id = r.event_id
LEFT JOIN Feedback f
ON e.event_id = f.event_id
WHERE f.feedback_id IS NULL;
```
### Output
<img width="938" height="330" alt="WhatsApp Image 2026-06-03 at 5 22 52 PM" src="https://github.com/user-attachments/assets/70ab05fe-5ba0-444b-a91e-c832a39cda6d" />

## 11. Daily New User Count
### Problem Statement
### Query
```
SELECT registration_date,
COUNT(*) AS new_users
FROM Users
WHERE registration_date >= CURDATE() - INTERVAL 7 DAY
GROUP BY registration_date
ORDER BY registration_date;
```
### Output
<img width="940" height="327" alt="WhatsApp Image 2026-06-03 at 5 24 41 PM" src="https://github.com/user-attachments/assets/734bc102-7493-4947-98d2-4d46f2cc4b21" />

## 12. Event with Maximum Sessions
### Problem Statement
### Query
```
SELECT e.title,
COUNT(s.session_id) AS total_sessions
FROM Events e
JOIN Sessions s
ON e.event_id = s.event_id
GROUP BY e.event_id, e.title
HAVING COUNT(s.session_id) =
(
SELECT MAX(session_count)
FROM
(
SELECT COUNT(*) AS session_count
FROM Sessions
GROUP BY event_id
) t
);
```
### Output
<img width="931" height="324" alt="WhatsApp Image 2026-06-03 at 5 25 30 PM" src="https://github.com/user-attachments/assets/d8d17415-5ec8-4024-b1b9-05e51622ba89" />

## 13. Average Rating per City
### Problem Statement
### Query
```
SELECT e.city,
AVG(f.rating) AS avg_rating
FROM Events e
JOIN Feedback f
ON e.event_id = f.event_id
GROUP BY e.city;
```
### Output
<img width="951" height="326" alt="WhatsApp Image 2026-06-03 at 5 26 21 PM" src="https://github.com/user-attachments/assets/347b6d2a-c60a-49ec-a2f9-5a49cb48890d" />

## 14. Most Registered Events
### Problem Statement
### Query
```
SELECT e.title,
COUNT(r.registration_id) AS total_registrations
FROM Events e
JOIN Registrations r
ON e.event_id = r.event_id
GROUP BY e.event_id, e.title
ORDER BY total_registrations DESC
LIMIT 3;
```
### Output
<img width="937" height="329" alt="WhatsApp Image 2026-06-03 at 5 27 22 PM" src="https://github.com/user-attachments/assets/b98d3016-3005-497f-8c7c-eeedacd60df7" />

## 15. Event Session Time Conflict
### Problem Statement
### Query
```
SELECT
s1.event_id,
s1.title AS session1,
s2.title AS session2
FROM Sessions s1
JOIN Sessions s2
ON s1.event_id = s2.event_id
AND s1.session_id < s2.session_id
AND s1.start_time < s2.end_time
AND s1.end_time > s2.start_time;
```
### Output
<img width="940" height="336" alt="WhatsApp Image 2026-06-03 at 5 28 24 PM" src="https://github.com/user-attachments/assets/e59f7e7b-21a7-44d7-82b7-3ad6f3c3cc73" />

## 16. Unregistered Active Users
### Problem Statement
### Query
```
SELECT u.*
FROM Users u
LEFT JOIN Registrations r
ON u.user_id = r.user_id
WHERE u.registration_date >= CURDATE() - INTERVAL 30 DAY
AND r.registration_id IS NULL;
```
### Output
<img width="935" height="328" alt="WhatsApp Image 2026-06-03 at 5 29 04 PM" src="https://github.com/user-attachments/assets/2dd05ed1-301a-46db-b3e6-41f74860476a" />

## 17. Multi-Session Speakers
### Problem Statement
### Query
```
SELECT speaker_name,
COUNT(*) AS total_sessions
FROM Sessions
GROUP BY speaker_name
HAVING COUNT(*) > 1;
```

## 18. Resource Availability Check
### Problem Statement
### Query
```
SELECT e.title
FROM Events e
LEFT JOIN Resources r
ON e.event_id = r.event_id
WHERE r.resource_id IS NULL;
```
### Output
<img width="926" height="332" alt="WhatsApp Image 2026-06-03 at 5 30 50 PM" src="https://github.com/user-attachments/assets/f8b199cb-3a05-470a-be44-72f1d6b43dd2" />

## 19. Completed Events with Feedback Summary
### Problem Statement
### Query
```
SELECT
e.title,
COUNT(DISTINCT r.registration_id) AS total_registrations,
AVG(f.rating) AS average_rating
FROM Events e
LEFT JOIN Registrations r
ON e.event_id = r.event_id
LEFT JOIN Feedback f
ON e.event_id = f.event_id
WHERE e.status='completed'
GROUP BY e.event_id, e.title;
```
### Output
<img width="931" height="329" alt="WhatsApp Image 2026-06-03 at 5 33 05 PM" src="https://github.com/user-attachments/assets/fe38c283-8dd4-49b2-96b6-371f0699ec34" />

## 20. User Engagement Index
### Problem Statement
### Query
```
SELECT
u.full_name,
COUNT(DISTINCT r.event_id) AS attended_events,
COUNT(DISTINCT f.feedback_id) AS feedback_submitted
FROM Users u
LEFT JOIN Registrations r
ON u.user_id = r.user_id
LEFT JOIN Feedback f
ON u.user_id = f.user_id
GROUP BY u.user_id, u.full_name;
```
### Output
<img width="925" height="328" alt="WhatsApp Image 2026-06-03 at 5 33 55 PM" src="https://github.com/user-attachments/assets/83b127a5-6181-4533-8659-7212c6756001" />

## 21. Top Feedback Providers
### Problem Statement
### Query
```
SELECT
u.full_name,
COUNT(f.feedback_id) AS total_feedbacks
FROM Users u
JOIN Feedback f
ON u.user_id = f.user_id
GROUP BY u.user_id, u.full_name
ORDER BY total_feedbacks DESC
LIMIT 5;
```
### Output
<img width="923" height="328" alt="WhatsApp Image 2026-06-03 at 5 35 40 PM" src="https://github.com/user-attachments/assets/99b9de2b-784e-4ac2-92f5-a9ef9189094d" />

## 22. Duplicate Registrations Check
### Problem Statement
### Query
```
SELECT
user_id,
event_id,
COUNT(*) AS duplicate_count
FROM Registrations
GROUP BY user_id, event_id
HAVING COUNT(*) > 1;
```
### Output
<img width="931" height="337" alt="WhatsApp Image 2026-06-03 at 5 37 11 PM" src="https://github.com/user-attachments/assets/bf25607d-5eb8-45a1-b642-7225b4bcecf0" />

## 23. Registration Trends
### Problem Statement
### Query
```
SELECT
YEAR(registration_date) AS year,
MONTH(registration_date) AS month,
COUNT(*) AS registration_count
FROM Registrations
WHERE registration_date >= CURDATE() - INTERVAL 12 MONTH
GROUP BY YEAR(registration_date),
MONTH(registration_date)
ORDER BY year, month;
```
### Output
<img width="926" height="330" alt="WhatsApp Image 2026-06-03 at 5 39 34 PM" src="https://github.com/user-attachments/assets/830aa49c-0a53-4c56-ae32-af7b119e4980" />

## 24. Average Session Duration per Event
### Problem Statement
### Query
```
SELECT
e.title,
AVG(
TIMESTAMPDIFF(
MINUTE,
s.start_time,
s.end_time
)
) AS avg_duration_minutes
FROM Events e
JOIN Sessions s
ON e.event_id = s.event_id
GROUP BY e.event_id, e.title;
```
### Output
<img width="928" height="331" alt="WhatsApp Image 2026-06-03 at 5 40 26 PM" src="https://github.com/user-attachments/assets/ebb06b63-d69f-4efb-8044-185c11560998" />

## 25. Events Without Sessions
### Problem Statement
### Query
```
SELECT e.title
FROM Events e
LEFT JOIN Sessions s
ON e.event_id = s.event_id
WHERE s.session_id IS NULL;
```
### Output
<img width="932" height="331" alt="WhatsApp Image 2026-06-03 at 5 41 07 PM" src="https://github.com/user-attachments/assets/e3c42469-d115-4cf4-b9e7-7bdd6cc1a09c" />
