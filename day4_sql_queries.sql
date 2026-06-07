-- =================================================================
-- ROADMAP DAY 4: ADVANCED SQL PRACTICE QUERIES
-- Student: Safiullah Chaudhary
-- Concepts: JOINs, GROUP BY, HAVING, ORDER BY, LIMIT
-- =================================================================

-- -----------------------------------------------------------------
-- SCENARIO 1: LIBRARY MANAGEMENT SYSTEM
-- -----------------------------------------------------------------

-- Task 1: Basic Student-Book Alignment (LEFT JOIN)
SELECT students.name, borrowed_books.book_name 
FROM students 
LEFT JOIN borrowed_books 
ON students.student_id = borrowed_books.student_id;

-- Task 2: Filtering Power Borrowers (GROUP BY & HAVING)
SELECT students.name, COUNT(borrowed_books.book_id) AS Total_books 
FROM students 
JOIN borrowed_books ON students.student_id = borrowed_books.student_id 
GROUP BY students.name 
HAVING COUNT(borrowed_books.book_id) > 1;


-- -----------------------------------------------------------------
-- SCENARIO 2: UNIVERSITY EXAMINATION SYSTEM
-- -----------------------------------------------------------------

-- Task 1: Total Scores per Student (SUM & JOIN)
SELECT students.name, SUM(exam_results.marks) AS Total_Score 
FROM students 
JOIN exam_results ON students.std_id = exam_results.std_id 
GROUP BY students.name;

-- Task 2: High Achievers Filter (AVG & HAVING)
SELECT students.name, AVG(exam_results.marks) AS Average_Marks
FROM students 
JOIN exam_results ON students.std_id = exam_results.std_id 
GROUP BY students.name 
HAVING AVG(exam_results.marks) > 80;

-- Task 3: Specific Course Diagnostics (3-Table Join with WHERE)
SELECT students.name, courses.title, exam_results.marks 
FROM exam_results 
JOIN students ON students.std_id = exam_results.std_id 
JOIN courses ON exam_results.course_id = courses.course_id 
WHERE courses.title = 'Digital Logic Design';


-- -----------------------------------------------------------------
-- SCENARIO 3: SOFTWARE DEVELOPMENT HUB
-- -----------------------------------------------------------------

-- Task 1: Total Commits Tracking (SUM & LEFT JOIN)
SELECT developers.name, SUM(contributions.commits_made) AS Total_Commits 
FROM developers 
LEFT JOIN contributions ON developers.dev_id = contributions.dev_id 
GROUP BY developers.name;

-- Task 2: Top Contributor Isolation (HAVING Filter)
SELECT developers.name, SUM(contributions.commits_made) AS Total_Commits 
FROM developers 
LEFT JOIN contributions ON developers.dev_id = contributions.dev_id 
GROUP BY developers.name  
HAVING SUM(contributions.commits_made) > 15;

-- Task 3: Tech Stack Isolation (3-Table Join & WHERE)
SELECT developers.name, software_projects.project_name, contributions.commits_made 
FROM contributions 
JOIN developers ON contributions.dev_id = developers.dev_id 
JOIN software_projects ON software_projects.project_id = contributions.project_id 
WHERE software_projects.tech_stack = 'Python OOP';


-- -----------------------------------------------------------------
-- SCENARIO 4: E-Commerce Store Dataset
-- -----------------------------------------------------------------

-- Task 1: Geographic Target Grouping (3-Table Join with WHERE)
SELECT customers.name, products.prod_name, orders.quantity 
FROM orders 
JOIN customers ON customers.cust_id = orders.cust_id 
JOIN products ON products.prod_id = orders.prod_id 
WHERE customers.city = 'Sahiwal';

-- Task 2: Bulk Buyers Identification (GROUP BY & HAVING)
SELECT customers.name, SUM(orders.quantity) AS Total_Items 
FROM customers 
JOIN orders ON customers.cust_id = orders.cust_id 
GROUP BY customers.name 
HAVING SUM(orders.quantity) > 1;


-- -----------------------------------------------------------------
-- SCENARIO 5: BOOTCAMP LEADERBOARD ANALYSIS
-- -----------------------------------------------------------------

-- Task 1: Top Rank Identification (ORDER BY & LIMIT)
SELECT participants.name, SUM(submissions.score_achieved) AS Total_Score 
FROM participants 
JOIN submissions ON participants.part_id = submissions.part_id 
GROUP BY participants.name 
ORDER BY Total_Score DESC 
LIMIT 1;

-- Task 2: Segment Specific Metrics (3-Table Join with Multi-Conditional Filters)
SELECT participants.name, challenges.track, submissions.score_achieved 
FROM submissions 
JOIN participants ON participants.part_id = submissions.part_id 
JOIN challenges ON challenges.challenge_id = submissions.challenge_id 
WHERE challenges.track = 'Machine Learning' AND submissions.score_achieved > 85;