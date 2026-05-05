# Django REST Framework CRUD API

A simple CRUD API built with Django REST Framework.  
This project demonstrates how to create, read, update, and delete student records using function-based API views.

---

## Features

- Create Student
- Get All Students
- Get Single Student
- Update Student
- Delete Student
- JSON Responses
- Django REST Framework API

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students/` | Get all students |
| POST | `/students/` | Create new student |
| GET | `/students/<id>/` | Get single student |
| PUT | `/students/<id>/` | Update student |
| DELETE | `/students/<id>/` | Delete student |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sohailkhansohail6300-bit/Django-RestFramwork.git
```

### Go To Project Folder

```bash
cd Django-RestFramwork
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Mac/Linux

```bash
source env/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Server

```bash
python manage.py runserver
```

---

## Example JSON

```json
{
    "name": "Ali",
    "age": 22,
    "email": "ali@gmail.com"
}
```

---

## Project Structure

```bash
project/
│
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

## Author

Muhammad Sohail

GitHub:
https://github.com/sohailkhansohail6300-bit
