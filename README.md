# 🎓 Graduate Internship Program API

A secure, scalable **Django REST API** for managing graduate internship job postings, applications, and contact messages.
This backend powers internship portals by exposing clean, well-documented RESTful endpoints with authentication, validation, and file upload support.

---

## 📌 Features

### 🔹 Job Management

* Create, update, delete, and retrieve internship job postings
* Categorize jobs using reusable categories
* Optional job location type (`remote` or `hybrid`)
* Automatic job posting date
* Public read access with protected write operations

### 🔹 Job Applications

* Submit internship applications linked to jobs
* Resume upload with file type and size validation
* Applicant details (name, email, university, graduation year)
* Secure file handling

### 🔹 Messages

* Contact and enquiry message handling
* Full CRUD support for admin review

### 🔹 API Security

* HTTP **Basic Authentication**
* Role-based access using Django permissions
* Secure endpoints protected by authentication

### 🔹 API Documentation

* Auto-generated **Swagger (OpenAPI)** documentation
* Interactive API testing interface
* Supports authentication and file uploads

---

## 🏗️ Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework (DRF)**
* **drf-yasg (Swagger / OpenAPI)**
* SQLite (default, easily swappable)

---

## 📁 Project Structure

```
internship_api/
├── core/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── validators.py
│
├── internship_api/
│   ├── settings.py
│   ├── urls.py
│
├── media/
│   └── resumes/
│
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd internship_api
```

---

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create a superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Start the development server

```bash
python manage.py runserver
```

---

## 📖 API Documentation (Swagger)

Once the server is running, access:

| URL       | Description               |
| --------- | ------------------------- |
| `/`       | Swagger API Documentation |
| `/redoc/` | Redoc Documentation       |
| `/admin/` | Django Admin Panel        |

Swagger allows:

* Endpoint exploration
* Authenticated API testing
* Resume file uploads
* Request/response previews

---

## 🔐 Authentication

This API uses **Basic Authentication**.

### Example (curl)

```bash
curl -u username:password http://127.0.0.1:8000/api/jobs/
```

### Example (Postman / Swagger)

* Authorization Type: **Basic Auth**
* Provide Django user credentials

> ⚠️ Always use HTTPS in production.

---

## 📦 API Endpoints

### 🔹 Jobs

```
GET     /api/jobs/
POST    /api/jobs/
GET     /api/jobs/{id}/
PUT     /api/jobs/{id}/
PATCH   /api/jobs/{id}/
DELETE  /api/jobs/{id}/
```

### 🔹 Job Applications

```
GET     /api/applications/
POST    /api/applications/
GET     /api/applications/{id}/
PUT     /api/applications/{id}/
PATCH   /api/applications/{id}/
DELETE  /api/applications/{id}/
```

### 🔹 Categories

```
GET     /api/categories/
POST    /api/categories/
```

### 🔹 Messages

```
GET     /api/messages/
POST    /api/messages/
```

---

## 📄 Resume Upload Validation

Resumes are validated to ensure:

* Accepted formats: **PDF, DOC, DOCX**
* Maximum size: **2MB**

Validation is enforced at the **model level**, ensuring consistency across:

* API
* Django Admin
* Forms

---

## 🧠 Design Decisions

* **ModelViewSets** used for clean CRUD logic
* **Many-to-Many Categories** for scalability
* **Choices fields** to enforce valid job location types
* **Model-level validation** for strong data integrity
* **Swagger-first API documentation**

---

## 🔮 Future Enhancements

* JWT authentication
* Application status tracking
* Email notifications on application submission
* Job expiration and deadlines
* Admin analytics dashboard
* Cloud storage for resumes (AWS S3 / Cloudinary)

---

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

Developed as a **graduate internship backend system** for GradCell.
