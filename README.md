# SACCO-py

A Django-based SACCO (Savings and Credit Cooperative) management system built using an MVC-style structure (Django MVT), with an emphasis on separating concerns between models, views, and templates.

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Project structure](#project-structure)
- [Tech stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run the project](#run-the-project)
- [Configuration](#configuration)
- [Static files](#static-files)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a Django project (`project32`) and Django apps (for example `users`) intended to support common SACCO workflows such as member management and related operations.

> Note: Django commonly refers to its architecture as **MVT (Model–View–Template)**. Many projects describe this as an **MVC-style** pattern because responsibilities map closely to MVC.

## Features

Because SACCO requirements vary by organization, features may differ depending on your configuration and the installed apps. Typical SACCO modules include:

- Member registration and profile management
- User authentication and authorization
- Loan application and approval workflows
- Savings/deposits tracking
- Reports and exports

If you add or remove modules in `project32/app32` or other apps, update this list accordingly.

## Project structure

High-level layout:

- `project32/` — Django project root
  - `manage.py` — Django management entry point
  - `project32/` — Django settings, URLs, WSGI/ASGI
  - `users/` — example Django app (accounts/users)
  - `static/` — static assets (CSS/JS/images)
- `requirements.txt` — Python dependencies

## Tech stack

- **Backend:** Python, Django
- **Frontend:** Django templates, JavaScript, CSS
- **UI:** `bootstrap5` (see `requirements.txt`)
- **Images:** `Pillow` (see `requirements.txt`)
- **Database:** SQLite (development) — `project32/db.sqlite3`

## Prerequisites

- Python 3.10+ (recommended)
- pip
- (Optional) virtualenv / venv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kaggwe-marvin/SACCO-py.git
   cd SACCO-py
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

> If Django is not installed through `requirements.txt` in your current version of the repo, install it explicitly:
>
> ```bash
> pip install django
> ```

## Run the project

From the repository root:

```bash
cd project32
python manage.py migrate
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/

## Configuration

Django settings module is configured in `project32/manage.py`:

- `DJANGO_SETTINGS_MODULE=project32.settings`

Common configuration tasks:

- Update `ALLOWED_HOSTS` for deployment
- Configure static/media paths
- Configure authentication backends (if you extend the `users` app)

## Static files

Static assets are located under:

- `project32/static/`

In production, collect static files:

```bash
python manage.py collectstatic
```

## Database

- Development database: `project32/db.sqlite3`
- To reset (development only), remove the SQLite file and re-run migrations.

## Contributing

Contributions are welcome.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-change`
3. Commit changes: `git commit -m "Add my change"`
4. Push: `git push origin feature/my-change`
5. Open a Pull Request

## License

No license file is currently included in this repository. If you intend others to use, modify, or distribute this project, add a `LICENSE` file (for example MIT, Apache-2.0, or GPL-3.0) and update this section.
