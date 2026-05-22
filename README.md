# 🎓 Student Management System
### DBMS Mini Project | Flask + MySQL + HTML/CSS

---

## 📁 Folder Structure

```
StudentManagementSystem/
│
├── app.py                      ← Main Flask application (backend logic)
├── requirements.txt            ← Python packages to install
├── database.sql                ← MySQL setup script (run this first!)
│
├── templates/                  ← HTML pages (Jinja2 templates)
│   ├── base.html               ← Common layout (navbar, footer)
│   ├── index.html              ← View all students (home page)
│   ├── add_student.html        ← Add new student form
│   ├── edit_student.html       ← Edit existing student form
│   └── view_student.html       ← View single student details
│
└── static/
    └── css/
        └── style.css           ← All CSS styling for the UI
```

---

## 🛠️ Setup Instructions (VS Code)

### Step 1 — Install Python
- Download from https://python.org and install.
- Make sure to check "Add Python to PATH" during install.

### Step 2 — Install MySQL
- Download MySQL Community Server from https://dev.mysql.com/downloads/
- Or use XAMPP (includes MySQL + phpMyAdmin) — easier for beginners.

### Step 3 — Open Project in VS Code
```bash
# Open VS Code, then open the StudentManagementSystem folder
File → Open Folder → select StudentManagementSystem
```

### Step 4 — Open Terminal in VS Code
```
View → Terminal  (or press Ctrl + `)
```

### Step 5 — Create Virtual Environment (recommended)
```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 6 — Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 7 — Set Up the Database
Open MySQL Workbench (or phpMyAdmin) and run the contents of `database.sql`:

```sql
CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;
CREATE TABLE IF NOT EXISTS students (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    roll_no    VARCHAR(20)  NOT NULL UNIQUE,
    branch     VARCHAR(50)  NOT NULL,
    year       VARCHAR(10)  NOT NULL,
    email      VARCHAR(100),
    phone      VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Or run via terminal:
```bash
mysql -u root -p < database.sql
```

### Step 8 — Update Database Password in app.py
Open `app.py` and edit the connection details:
```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',        # ← Put your MySQL password here
    database='student_db'
)
```

### Step 9 — Run the Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 10 — Open in Browser
Go to: **http://localhost:5000**

---

## ✅ CRUD Features

| Feature        | Route              | Method     |
|----------------|--------------------|------------|
| View Students  | `/`                | GET        |
| Add Student    | `/add`             | GET + POST |
| Edit Student   | `/edit/<id>`       | GET + POST |
| Delete Student | `/delete/<id>`     | GET        |
| View Student   | `/view/<id>`       | GET        |

---

## 🗄️ Database Table Structure

| Column     | Type         | Description              |
|------------|--------------|--------------------------|
| id         | INT (PK, AI) | Auto-generated unique ID |
| name       | VARCHAR(100) | Student full name        |
| roll_no    | VARCHAR(20)  | Unique roll number       |
| branch     | VARCHAR(50)  | Branch/Department        |
| year       | VARCHAR(10)  | Year of study            |
| email      | VARCHAR(100) | Email (optional)         |
| phone      | VARCHAR(15)  | Phone (optional)         |
| created_at | TIMESTAMP    | Auto-set on insert       |

---

## 🐛 Common Issues & Fixes

**Error: `ModuleNotFoundError: No module named 'flask'`**
→ Run: `pip install flask`

**Error: `Access denied for user 'root'@'localhost'`**
→ Update the password in `app.py` to match your MySQL root password.

**Error: `Unknown database 'student_db'`**
→ Run the `database.sql` script first in MySQL.

**Port already in use:**
→ Change the port: `app.run(debug=True, port=5001)`

---

*Built as a DBMS Lab Mini Project — Flask + MySQL + HTML/CSS*