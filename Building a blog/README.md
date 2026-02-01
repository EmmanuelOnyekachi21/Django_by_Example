# Building a Blog

A Django blog application with comprehensive features including post management, commenting, tagging, and sharing capabilities.

## Features

- **Post Management**: Create, edit, and publish blog posts
- **Tagging System**: Organize posts with tags and find similar content
- **Comments**: User engagement through post comments
- **Email Sharing**: Share posts via email
- **Pagination**: Navigate through posts efficiently
- **Admin Interface**: Django admin for content management

## Project Structure

```
Building a blog/
├── apps/
│   ├── blog/           # Main blog application
│   │   ├── models.py   # Post, Comment, Tag models
│   │   ├── views.py    # Blog views and logic
│   │   ├── forms.py    # Comment and email forms
│   │   ├── admin.py    # Admin configuration
│   │   ├── urls.py     # URL patterns
│   │   ├── templates/  # HTML templates
│   │   └── static/     # CSS and static files
│   └── urls.py         # App-level URL configuration
├── mysite/             # Django project settings
│   ├── settings.py     # Project configuration
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database
└── populate_data.py    # Sample data generator
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install django
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Populate Sample Data** (optional):
   ```bash
   python populate_data.py
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

## Key Components

- **Models**: Post, Comment, and Tag models with relationships
- **Views**: List, detail, comment, and share functionality
- **Templates**: Responsive HTML templates with pagination
- **Forms**: Comment submission and email sharing forms
- **Admin**: Customized Django admin interface

## URLs

- `/` - Blog post list
- `/post/<id>/` - Individual post detail
- `/post/<id>/share/` - Share post via email
- `/admin/` - Django admin interface