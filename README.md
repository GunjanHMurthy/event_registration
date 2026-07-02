# 🎉 Event Registration System

## 📖 Overview

The Event Registration System is a web-based application developed using the Django framework. It enables administrators to create, update, and manage events while allowing participants to register for available events. The application demonstrates Django's Model-View-Template (MVT) architecture, CRUD operations, form handling, URL routing, and database integration.

---

## 🎯 Objectives

* Develop a web application for event management.
* Allow administrators to manage event details.
* Enable participants to register for events.
* Demonstrate CRUD operations using Django.
* Learn Django Models, Forms, Templates, and Class-Based Views.

---

## ✨ Features

* Event Creation
* Event Update
* Event Deletion
* Event Listing
* Participant Registration
* Registration Management
* Django Admin Panel
* User-Friendly Interface
* SQLite Database Integration

---

## 🛠 Technologies Used

| Technology       | Description          |
| ---------------- | -------------------- |
| Python           | Programming Language |
| Django           | Web Framework        |
| HTML5            | Frontend Structure   |
| CSS3             | Styling              |
| SQLite           | Database             |
| Django Templates | Dynamic Web Pages    |

---

## 📂 Project Structure

```text
Event-Registration-System/
│
├── event_registration/
│   ├── migrations/
│   ├── templates/
│   │   ├── event_confirm_delete.html
│   │   ├── event_form.html
│   │   ├── event_list.html
│   │   ├── registration_form.html
│   │   ├── registration_list.html
│   │   ├── registration_update_form.html
│   │   └── success.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── events/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 🚀 Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/GunjanHMurthy/Event-Registration-System.git
```

### Step 2: Move to the Project Folder

```bash
cd Event-Registration-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Step 5: Install Django

```bash
pip install django
```

### Step 6: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create an Admin User

```bash
python manage.py createsuperuser
```

### Step 8: Run the Server

```bash
python manage.py runserver
```

### Step 9: Open in Browser

```
http://127.0.0.1:8000/
```

---


## 📚 Learning Outcomes

Through this project, I learned:

* Django Framework
* Python Web Development
* CRUD Operations
* Django Models
* Django Forms
* Class-Based Views
* URL Routing
* Template Rendering
* Django Admin Panel

---

## 🔮 Future Enhancements

* User Login & Authentication
* Email Notifications
* Event Search & Filters
* Event Capacity Management
* Online Payment Integration
* Mobile Responsive Design

---

## 👩‍💻 Author

**Gunjan H Murthy**

GitHub: https://github.com/GunjanHMurthy

---

## 📄 License

This project was developed for educational purposes as part of the **Full Stack Development** course at the **University of Mysore**.
