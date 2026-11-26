# TaskMaster — To-Do Task App
Frantz Fanon University — Django (Advance Python) — Assignment II

## How to run

1. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations (creates the SQLite database and tables):
   ```
   python manage.py migrate
   ```

4. Create an admin/login account (needed to access the "Add Task" page,
   which requires login):
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Open http://127.0.0.1:8000/ in your browser.

## Pages / URLs

| Page                     | URL              | Notes |
|---------------------------|------------------|-------|
| Homepage                  | `/`              | Bootstrap carousel + 7 image cards |
| Task page                 | `/task/`         | Register a task (task name + description) — requires login |
| Task list page             | `/task-list/`    | Retrieves and displays all tasks from the database |
| Contact / contactviewpage  | `/contact/`      | Form (first name, last name, contact number, email); saves and re-displays submissions on the same page; also shows 3 pictures + 2 videos |
| Login                      | `/login/`        | Django built-in auth |
| Logout                     | `/logout/`       | Django built-in auth |
| Admin                      | `/admin/`        | Manage Task / Contact records |

## Requirement checklist (from the assignment sheet)

1. 5 pages: home, task-page, task-list, contactviewpage, plus login/logout — done.
2. Homepage carousel + 7 cards with images — done (`tasks/templates/tasks/home.html`).
3. Task page with task-name & description fields — done (`TaskForm`).
4. Register tasks + view them on task-list page — done.
5. Task list retrieves data from the database and displays it — done (`Task.objects.all()`).
6. Students submit tasks under their name — `student_name` field on `Task`.
7. Contact page: first name, last name, contact number, email — submits to
   the database and displays results on the same page — done (`ContactForm` + `contactviewpage` view).
8. Contactviewpage: 3 pictures + 2 videos — done (gallery section).
9. Login and logout pages — done (Django's built-in auth views).
10. Contact page field layout (FNAME / LNAME / Contact number / Email) — matches form layout.

## About the images/videos

This build was generated in an offline sandbox with no internet access, so
the pictures on the homepage cards, carousel, and contact gallery, and the
two contact-page videos, are original placeholder graphics/clips generated
locally (gradient cards with titles, and short generated video clips) rather
than downloaded photos. They're already wired up correctly in the templates
(`{% static %}` tags) — simply replace the files in
`tasks/static/tasks/images/` and `tasks/static/tasks/videos/` with your own
photos/videos (keep the same filenames, or update the paths in
`tasks/views.py`) to swap in real media.

## Project structure

```
todo_project/
├── manage.py
├── requirements.txt
├── todo_project/          # project settings, urls, wsgi/asgi
└── tasks/                 # the Django app
    ├── models.py           # Task, Contact
    ├── forms.py            # TaskForm, ContactForm
    ├── views.py            # home, task_page, task_list, contactviewpage
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── static/tasks/images/  # 13 generated placeholder images
    ├── static/tasks/videos/  # 2 generated placeholder videos
    └── templates/
        ├── tasks/            # base, home, task_page, task_list, contactviewpage
        └── registration/     # login.html
```
