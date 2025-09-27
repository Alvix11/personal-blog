# Personal Blog

A personal blog web application built with Django.  
It allows authenticated users to create, list, edit, and delete posts, with admin panel access and user authentication.  
The interface uses Bootstrap for a modern look and includes access control for administrators.

## Features

- User authentication (login, logout, register)
- Admin-only post creation, update, and delete
- List and detail views for blog posts
- Responsive Bootstrap UI
- Django admin panel
- Environment variable support via `.env`

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/personal-blog.git
   cd personal-blog
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env` and fill in your values.

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the blog at `http://127.0.0.1:8000/`
- Admin panel at `http://127.0.0.1:8000/admin/`
- Register and login as a regular user to view posts.
- **To create, edit, or delete posts, you must be an admin user.**
- Create a superuser with Django (`python manage.py createsuperuser`) and log in with those credentials to access admin-only features.

## Folder Structure

- `personal_blog/` – Django project settings and configuration
- `blog/` – Main app: models, views, forms, templates
- `requirements.txt` – Python dependencies
- `.env.example` – Example environment variables

## Based on

This project is based on the learning and practice projects suggested by roadmap.sh, a popular resource for developers.

## License

MIT License. See [LICENSE](LICENSE) for details.