📝 Django Task Manager – Simple CRUD App
A beginner-friendly Task Management app built using Django. This project covers all the core CRUD (Create, Read, Update, Delete) functionalities while keeping the codebase clean and easy to understand.

🚀 What’s Inside?
✅ Add new tasks with a title, description, and completion status

📖 View your task list in a neat, responsive UI

✏️ Edit tasks and update their status

🗑️ Delete tasks safely with confirmation prompts

🎨 Stylish Bootstrap-based design

📱 Fully responsive and mobile-friendly

⚡ Instant UI feedback with real-time status updates

🛠️ Tech Stack
Framework: Django 4.x

Database: SQLite (default)

Frontend: HTML5, CSS3, Bootstrap 5.1.3

Language: Python 3.8+

📋 Requirements
Before you get started, make sure you have:

Python 3.8 or above

pip installed

Git (optional, but helpful for cloning the repo)

🔧 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
Alternatively, you can download the ZIP file and extract it manually.

2. Set Up a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
# Activate it
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3. Install Required Packages
bash
Copy
Edit
pip install django
4. Project Folder Structure
Your project should look like this:

Copy
Edit
task_manager/
├── manage.py
├── requirements.txt
├── task_manager/
│   └── ...
├── tasks/
│   └── ...
├── templates/
│   └── ...
5. Migrate the Database
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. (Optional) Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
Use the credentials you set here to log in to the Django admin panel.

7. Start the Development Server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the app in your browser.

💡 How to Use It
Homepage: View all tasks

Create: Click “New Task” to add one

Edit: Update task details or status

Delete: Confirm and remove tasks

Mark Complete: Use the checkbox on forms

Admin Panel: Log in at /admin/ to manage data via Django admin

📁 Project Structure Overview
Models (tasks/models.py)
Defines the Task model with title, description, status, and timestamps.

Views (tasks/views.py)
task_list – View all tasks

task_create – Add a new task

task_detail – See full details

task_update – Edit a task

task_delete – Remove a task

Templates
base.html – Base layout

task_list.html – All tasks

task_form.html – Create/edit form

task_detail.html – Single task view

task_confirm_delete.html – Deletion confirmation

URLs (tasks/urls.py)
/ – Home

/create/ – New task

/task/<id>/ – Task details

/task/<id>/update/ – Edit

/task/<id>/delete/ – Delete

🎨 Customizing the App
Add Your Own Styles
Create a static/css/ folder

Add your CSS files there

In settings.py:

python
Copy
Edit
STATICFILES_DIRS = [BASE_DIR / 'static']
In templates:

html
Copy
Edit
{% load static %}
<link rel="stylesheet" href="{% static 'css/custom.css' %}">
