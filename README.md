# 🎓 Student Management System
### DBMS Mini Project | Flask + SQLite + HTML/CSS

---

## 📁 Folder Structure

```
StudentManagementSystem/
│
├── app.py                      ← Main Flask application (backend logic)
├── requirements.txt            ← Python packages to install
├── database.sql                ← SQlite3 setup script (run this first!)
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

### Step 2 — SQLite Database

- SQLite comes built into Python
- No separate installation needed

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

### Step 7 — Database Setup (SQLite)

SQLite database will be created automatically when you run the Flask app.

Database file:
```bash
students.db
```

Run the application:
```bash
python app.py
```

## Step 8 — Run the Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 9 — Open in Browser
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

**Error: Database not opening**
→ Delete students.db and run the app again.

**Error: `Unknown database 'student_db'`**
→ Run the `database.sql` script first in SQLite.

**Port already in use:**
→ Change the port: `app.run(debug=True, port=5001)`

---

*Built as a DBMS Lab Mini Project — Flask + SQLite + HTML/CSS*
