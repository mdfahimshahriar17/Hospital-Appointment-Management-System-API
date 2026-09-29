# Hospital Appointment Management System API

A REST API for managing patients, doctors, appointments, billing, and dashboard information using Django REST Framework.

## Features

- JWT Authentication
- Patient Registration & Login
- Forgot Password & Reset Password
- Profile Management
- Role-based User System
  - Admin
  - Doctor
  - Patient
- Doctor Management
- Appointment Management
- Billing Management
- Filtering
- Searching
- Ordering
- Pagination
- Dashboard Summary
- Custom Middleware
- API validation

---

## Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- Django Filter
- SQLite
- Postman
- Git & GitHub

---

## Project Structure

```text
Hospital Appointment Management System API/
│
├── accounts/
├── doctors/
├── appointments/
├── billing/
├── dashboard/
├── hospital/
├── manage.py
├── requirements.txt
└── README.md
````

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mdfahimshahriar17/Hospital-Appointment-Management-System-API.git
cd Hospital-Appointment-Management-System-API
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# API Endpoints

## Authentication

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| POST   | `/api/register/`        | Register a new patient       |
| POST   | `/api/login/`           | Login and receive JWT tokens |
| POST   | `/api/token/refresh/`   | Refresh access token         |
| POST   | `/api/forgot-password/` | Request password reset       |
| POST   | `/api/reset-password/`  | Reset password               |

---

## Profile

| Method | Endpoint        | Description                   |
| ------ | --------------- | ----------------------------- |
| GET    | `/api/profile/` | View logged-in user's profile |
| PUT    | `/api/profile/` | Update complete profile       |
| PATCH  | `/api/profile/` | Update profile partially      |

---

## Doctor Management

| Method | Endpoint             | Description             |
| ------ | -------------------- | ----------------------- |
| GET    | `/api/doctors/`      | View all doctors        |
| POST   | `/api/doctors/`      | Create doctor           |
| GET    | `/api/doctors/<id>/` | View single doctor      |
| PUT    | `/api/doctors/<id>/` | Update doctor           |
| PATCH  | `/api/doctors/<id>/` | Partially update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor           |

### Doctor Filtering

Filter doctors by department:

```text
GET /api/doctors/?department=Cardiology
```

### Doctor Searching

Search doctors by name:

```text
GET /api/doctors/?search=Rahman
```

### Doctor Ordering

Ascending:

```text
GET /api/doctors/?ordering=visiting_fee
```

Descending:

```text
GET /api/doctors/?ordering=-visiting_fee
```

### Doctor Pagination

```text
GET /api/doctors/?page=2
```

10 records are displayed per page.

---

# Appointment Management

| Method | Endpoint                  | Description                       |
| ------ | ------------------------- | --------------------------------- |
| GET    | `/api/appointments/`      | View appointments                 |
| POST   | `/api/appointments/`      | Book appointment                  |
| GET    | `/api/appointments/<id>/` | View appointment                  |
| PUT    | `/api/appointments/<id>/` | Update appointment                |
| PATCH  | `/api/appointments/<id>/` | Update appointment status/details |
| DELETE | `/api/appointments/<id>/` | Delete/cancel appointment         |

### Appointment Filtering

Filter by status:

```text
GET /api/appointments/?status=pending
```

Filter by doctor:

```text
GET /api/appointments/?doctor=2
```

### Appointment Searching

Search by patient or doctor name:

```text
GET /api/appointments/?search=John
```

### Appointment Ordering

Ascending:

```text
GET /api/appointments/?ordering=appointment_date
```

Descending:

```text
GET /api/appointments/?ordering=-appointment_date
```

### Appointment Pagination

```text
GET /api/appointments/?page=2
```

10 records are displayed per page.

---

# Billing Management

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/api/bills/`      | View bills            |
| POST   | `/api/bills/`      | Create bill           |
| GET    | `/api/bills/<id>/` | View single bill      |
| PUT    | `/api/bills/<id>/` | Update bill           |
| PATCH  | `/api/bills/<id>/` | Partially update bill |
| DELETE | `/api/bills/<id>/` | Delete bill           |

### Billing Calculation

When creating a bill:

```text
Consultation Fee = Doctor's Visiting Fee

Total Amount = Consultation Fee - Discount
```

A bill can be created only when the related appointment is completed.

---

# Dashboard

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | `/api/dashboard/` | View dashboard summary |

The dashboard provides:

* Total Patients
* Total Doctors
* Total Appointments
* Pending Appointments
* Completed Appointments

---

# Authentication

This project uses JWT authentication.

After login, include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

---

# User Roles

## Admin

* Full access
* Manage doctors
* Manage appointments
* View dashboard
* Manage bills

## Doctor

* View assigned appointments
* View related bills

## Patient

* Register and login
* Manage own profile
* Create appointments
* View own appointments
* View own bills

---

# Validation

The API includes the following validations:

* Email must be unique
* Phone number must be unique
* Visiting fee cannot be negative
* Appointment date cannot be in the past
* Discount cannot be greater than consultation fee
* Password confirmation during registration/reset

---

# Middleware

A custom middleware is included to log the HTTP method and request URL in the terminal.

Example:

```text
GET /api/doctors/
POST /api/appointments/
GET /api/dashboard/
```

---

# Testing

All APIs were tested using Postman.

The Postman collection covers:

* Authentication APIs
* Profile APIs
* Doctor APIs
* Appointment APIs
* Billing APIs
* Dashboard API

---

# Author

**Fahim Shahriar**
