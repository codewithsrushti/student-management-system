# ============================================================
# Student Management System - Main Application File
# Backend: Flask | Database: MySQL
# ============================================================

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

# ============================================================
# DATABASE CONNECTION FUNCTION
# ============================================================
def get_db_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # MySQL server host
            user='root',           # Your MySQL username
            password='',           # Your MySQL password (change if needed)
            database='student_db'  # Database name
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None


# ============================================================
# ROUTE: HOME PAGE - View All Students
# ============================================================
@app.route('/')
def index():
    """Display all students from the database."""
    connection = get_db_connection()
    students = []

    if connection:
        cursor = connection.cursor(dictionary=True)  # Returns rows as dicts
        cursor.execute("SELECT * FROM students ORDER BY id DESC")
        students = cursor.fetchall()  # Fetch all student records
        cursor.close()
        connection.close()

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
            flash('Please fill in all required fields!', 'error')
            return render_template('add_student.html')

        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Insert new student record
                sql = """INSERT INTO students (name, roll_no, branch, year, email, phone)
                         VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (name, roll_no, branch, year, email, phone))
                connection.commit()  # Save changes
                flash('Student added successfully!', 'success')
                cursor.close()
                connection.close()
                return redirect(url_for('index'))
            except Error as e:
                flash(f'Error adding student: {e}', 'error')
                connection.close()

    return render_template('add_student.html')


# ============================================================
# ROUTE: EDIT STUDENT - Show Pre-filled Form & Handle Update
# ============================================================
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    """Show edit form on GET; update student on POST."""
    connection = get_db_connection()
    student = None

    if connection:
        cursor = connection.cursor(dictionary=True)

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
                sql = """UPDATE students SET name=%s, roll_no=%s, branch=%s,
                         year=%s, email=%s, phone=%s WHERE id=%s"""
                cursor.execute(sql, (name, roll_no, branch, year, email, phone, id))
                connection.commit()
                flash('Student updated successfully!', 'success')
                cursor.close()
                connection.close()
                return redirect(url_for('index'))
            except Error as e:
                flash(f'Error updating student: {e}', 'error')

        else:
            # Fetch existing student data to pre-fill form
            cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
            student = cursor.fetchone()

        cursor.close()
        connection.close()

    return render_template('edit_student.html', student=student)


# ============================================================
# ROUTE: DELETE STUDENT
# ============================================================
@app.route('/delete/<int:id>')
def delete_student(id):
    """Delete a student record by ID."""
    connection = get_db_connection()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            connection.commit()
            flash('Student deleted successfully!', 'success')
            cursor.close()
            connection.close()
        except Error as e:
            flash(f'Error deleting student: {e}', 'error')

    return redirect(url_for('index'))


# ============================================================
# ROUTE: VIEW SINGLE STUDENT DETAILS
# ============================================================
@app.route('/view/<int:id>')
def view_student(id):
    """View detailed information of a single student."""
    connection = get_db_connection()
    student = None

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        student = cursor.fetchone()
        cursor.close()
        connection.close()

    return render_template('view_student.html', student=student)


# ============================================================
# RUN THE APP
# ============================================================

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)