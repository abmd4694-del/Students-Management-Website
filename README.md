# Student Management System (SMS) with ToDo & API

A full-stack Django application that serves as a modern institutional management portal. It features a premium "Website-like" UI, a robust Student Directory with search/filtering, a personal ToDo application, and a secure REST API.

## 🚀 Key Features

### 💻 Student Management

- **Directory**: Card-based layout with search (Name, Dept, Email) and pagination.
- **Profile**: Detailed student profiles including `Phone`, `Address`, `Date of Birth`, and Profile Image.
- **Actions**: Add, Update, and Delete students (Protected by login).

### ✅ Personal ToDo App

- **Task Manager**: A private, user-specific ToDo list (`/todos/`).
- **Features**: Add tasks, toggle completion status, delete tasks.
- **UI**: Clean, modern checklist interface.

### 🎨 Premium UI/UX

- **Website Experience**: Rich Home page with Stats, Testimonials, and Call-to-Action.
- **Modern Design**: Glassmorphism effects, 3D abstract headers, and responsive grid layouts.
- **Pages**:
  - **Home**: Landing page with marketing content.
  - **About**: Feature grid and institutional info.
  - **Contact**: Split layout with contact form and details.

### 🔌 REST API

- **Base URL**: `/api/students/`
- **Features**:
  - **Search**: `?search=query`
  - **Ordering**: `?ordering=name`
  - **Pagination**: Limit 10 per page.
  - **Security**: Read-only for guests, Write access for authenticated users.

## 🛠 Tech Stack

- **Backend**: Django 4.2+, Django Rest Framework (DRF).
- **Database**: PostgreSQL.
- **Frontend**: HTML5, CSS3 (Custom Premium Styles), FontAwesome.

## ⚙️ Installation & Setup

1.  **Clone & Setup Environment**

    ```bash
    git clone <repo_url>
    cd student_management_full
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

2.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Database Setup (PostgreSQL)**

    - Ensure PostgreSQL is running.
    - Create a database named `Django_db`.
    - Update credentials in `student_management/settings.py` if needed.
    - Run migrations:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```

4.  **Create Admin User**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Run Server**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/`

## 🧪 Quick Start Guide

1.  **Register/Login**: Create an account to access write features options.
2.  **Add Student**: Navigate to "Students" -> "Add New".
3.  **Manage Tasks**: Go to "My Tasks" to track your work.
4.  **Explore**: Check out the "About" and "Contact" pages to see the new design.
