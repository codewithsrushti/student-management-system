# ============================================================
# Student Management System - Main Application File
# Backend: Flask | Database: MySQL
# ============================================================
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret"
import sqlite3
def get_db_conn():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_conn()

conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    branch TEXT,
    year TEXT,
    email TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()
# ============================================================
# ROUTE: HOME PAGE - View All Students
# ============================================================
@app.route('/')
def index():

    conn = get_db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

# ============================================================
# ROUTE: ADD STUDENT - Show Form & Handle Submission
# ============================================================
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Show add form on GET; insert student on POST."""
    if request.method == 'POST':
        # Get form data
        name    = request.form['name'].strip()
        roll_no = request.form['roll_no'].strip()
        branch  = request.form['branch'].strip()
        year    = request.form['year'].strip()
        email   = request.form['email'].strip()
        phone   = request.form['phone'].strip()

        # Basic validation
        if not name or not roll_no or not branch or not year:
            flash('Please fill in all required fields!', 'Exception')
            return render_template('add_student.html')

        conn = get_db_conn()
        if conn:
            try:
                cursor = conn.cursor()
                # Insert new student record
                sql = """INSERT INTO students (name, roll_no, branch, year, email, phone)
                         VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(sql, (name, roll_no, branch, year, email, phone))
                conn.commit()  # Save changes
                flash('Student added successfully!', 'success')
                cursor.close()
                conn.close()
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Exception adding student: {e}', 'Exception')
                conn.close()

    return render_template('add_student.html')


# ============================================================
# ROUTE: EDIT STUDENT - Show Pre-filled Form & Handle Update
# ============================================================
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    """Show edit form on GET; update student on POST."""
    conn = get_db_conn()
    student = None

    if conn:
        cursor = conn.cursor()

        if request.method == 'POST':
            # Get updated form data
            name    = request.form['name'].strip()
            roll_no = request.form['roll_no'].strip()
            branch  = request.form['branch'].strip()
            year    = request.form['year'].strip()
            email   = request.form['email'].strip()
            phone   = request.form['phone'].strip()

            try:
                # Update existing student record
                sql = """UPDATE students SET name=?, roll_no=?, branch=?,
                         year=?, email=?, phone=? WHERE id=?"""
                cursor.execute(sql, (name, roll_no, branch, year, email, phone, id))
                conn.commit()
                flash('Student updated successfully!', 'success')
                cursor.close()
                conn.close()
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Exception updating student: {e}', 'Exception')

        else:
            # Fetch existing student data to pre-fill form
            cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
            student = cursor.fetchone()

        cursor.close()
        conn.close()

    return render_template('edit_student.html', student=student)


# ============================================================
# ROUTE: DELETE STUDENT
# ============================================================
@app.route('/delete/<int:id>')
def delete_student(id):
    """Delete a student record by ID."""
    conn = get_db_conn()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (id,))
            conn.commit()
            flash('Student deleted successfully!', 'success')
            cursor.close()
            conn.close()
        except Exception as e:
            flash(f'Exception deleting student: {e}', 'Exception')

    return redirect(url_for('index'))


# ============================================================
# ROUTE: VIEW SINGLE STUDENT DETAILS
# ============================================================
@app.route('/view/<int:id>')
def view_student(id):
    """View detailed information of a single student."""
    conn = get_db_conn()
    student = None

    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
        student = cursor.fetchone()
        cursor.close()
        conn.close()

    return render_template('view_student.html', student=student)


# ============================================================
# RUN THE APP
# ============================================================

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)