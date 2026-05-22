-- ============================================================
-- Student Management System - Database Setup Script
-- Run this in MySQL Workbench or phpMyAdmin or MySQL CLI
-- ============================================================

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS student_db;

-- Step 2: Select the database to use
USE student_db;

-- Step 3: Create the students table
CREATE TABLE IF NOT EXISTS students (
    id       INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each student (auto-generated)
    name     VARCHAR(100) NOT NULL,            -- Student full name
    roll_no  VARCHAR(20)  NOT NULL UNIQUE,     -- Roll number (must be unique)
    branch   VARCHAR(50)  NOT NULL,            -- Branch/Department (e.g., CSE, ECE)
    year     VARCHAR(10)  NOT NULL,            -- Year of study (1st, 2nd, 3rd, 4th)
    email    VARCHAR(100),                     -- Email address (optional)
    phone    VARCHAR(15),                      -- Phone number (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date/time of record creation
);

-- Step 4: Insert some sample student records for testing
INSERT INTO students (name, roll_no, branch, year, email, phone) VALUES
('Aarav Sharma',    '21CS001', 'Computer Science',        '3rd Year', 'aarav@example.com',    '9876543210'),
('Priya Patel',     '21EC002', 'Electronics',             '3rd Year', 'priya@example.com',    '9876543211'),
('Rohit Verma',     '22ME003', 'Mechanical Engineering',  '2nd Year', 'rohit@example.com',    '9876543212'),
('Sneha Iyer',      '22CS004', 'Computer Science',        '2nd Year', 'sneha@example.com',    '9876543213'),
('Karthik Reddy',   '21CE005', 'Civil Engineering',       '3rd Year', 'karthik@example.com',  '9876543214');

-- Verify the table was created and data inserted
SELECT * FROM students;
