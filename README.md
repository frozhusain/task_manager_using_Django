# Django Task Manager - CRUD Application

A beginner-friendly Task Management System built with Django that demonstrates all CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

- ✅ **Create** new tasks with title, description, and completion status
- 📖 **Read** and view all tasks in a clean, responsive interface
- ✏️ **Update** existing tasks and mark them as completed
- 🗑️ **Delete** tasks with confirmation prompts
- 🎨 Beautiful Bootstrap-styled responsive UI
- 📱 Mobile-friendly design
- ⚡ Real-time status updates and notifications

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, Bootstrap 5.1.3
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed
- pip (Python package installer)
- Git (optional, for cloning)

## 🔧 Installation & Setup

### 1. Clone or Download the Project

```bash
# Option 1: Clone with Git
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager

# Option 2: Download and extract the ZIP file
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Project Structure Setup

Ensure your project has this structure:

```
task_manager/
├── task_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── tasks/
│       ├── task_list.html
│       ├── task_form.html
│       ├── task_detail.html
│       └── task_confirm_delete.html
├── manage.py
└── requirements.txt
```

### 5. Database Setup

```bash
# Create database migrations
python3 manage.py makemigrations

# Apply migrations to create database tables
python3 manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python3 manage.py createsuperuser
```

Follow the prompts to create an admin user for accessing the Django admin panel.

### 7. Run the Development Server

```bash
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application!

## 🎯 Usage

### Basic Operations

1. **View Tasks**: Visit the homepage to see all your tasks
2. **Create Task**: Click "Create New Task" to add a new task
3. **View Details**: Click "View" on any task to see full details
4. **Edit Task**: Click "Edit" to modify a task
5. **Delete Task**: Click "Delete" and confirm to remove a task
6. **Mark Complete**: Use the checkbox when creating/editing tasks

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` with your superuser credentials to:
- Manage tasks through Django's admin interface
- View database records
- Perform bulk operations

## 📁 Application Structure

### Models (`tasks/models.py`)
- **Task Model**: Defines the structure of tasks with fields for title, description, completion status, and timestamps

### Views (`tasks/views.py`)
- **task_list**: Display all tasks (READ)
- **task_create**: Create new tasks (CREATE)
- **task_detail**: Show individual task details (READ)
- **task_update**: Edit existing tasks (UPDATE)
- **task_delete**: Remove tasks (DELETE)

### Templates
- **base.html**: Base template with navigation and Bootstrap styling
- **task_list.html**: Homepage showing all tasks in cards
- **task_form.html**: Form for creating and updating tasks
- **task_detail.html**: Detailed view of a single task
- **task_confirm_delete.html**: Confirmation page for task deletion

### URLs (`tasks/urls.py`)
- `/` - Task list (homepage)
- `/create/` - Create new task
- `/task/<id>/` - Task detail view
- `/task/<id>/update/` - Update task
- `/task/<id>/delete/` - Delete task

## 🎨 Customization

### Adding Custom Styles

1. Create a `static` folder in your project root
2. Add CSS files to `static/css/`
3. Update `settings.py`:
   ```python
   STATICFILES_DIRS = [BASE_DIR / 'static']
   ```
4. Load static files in templates:
   ```html
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/custom.css' %}">
   ```

### Extending the Model

To add new fields to tasks:

1. Update the `Task` model in `models.py`
2. Update the form in `forms.py`
3. Run migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

## 🚀 Deployment

### For Production

1. Update `settings.py`:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. Set up a production database (PostgreSQL recommended)

3. Configure static files:
   ```python
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

4. Run collectstatic:
   ```bash
   python manage.py collectstatic
   ```

