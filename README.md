# 🚚 Moving Company Management System

A comprehensive web application built with Django for managing a moving company's operations including customer quotes, move scheduling, inventory tracking, and insurance claims.

## ✨ Features

- **Customer Management**: Store and manage customer information
- **Quote Generation**: Create quotes with automatic cost calculation
- **Inventory Tracking**: Track items for each move
- **Move Scheduling**: Schedule moves with driver and vehicle information (Admin Only)
- **Insurance Claims**: Users can submit claims, Admins can approve them
- **User Authentication**: Login/Signup system with role-based access
- **Admin Panel**: Full Django admin interface for data management

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 5.2.7
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5.3
- **Database**: SQLite (development), PostgreSQL (production)
- **Additional Packages**: 
  - Pillow (image handling)
  - django-crispy-forms (form rendering)
  - reportlab (PDF generation)
  - gunicorn (production server)
  - whitenoise (static files)

## 📁 Project Structure

```
pro1/
│
├── backend/
│   ├── manage.py
│   ├── backend/                 
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── company/                 
│       ├── models.py            
│       ├── views.py             
│       ├── urls.py              
│       └── admin.py             
│
├── templates/                   
│   ├── base.html
│   ├── home.html
│   ├── quote_form.html
│   ├── quote_detail.html
│   ├── inventory.html
│   ├── schedule.html
│   ├── insurance.html
│   ├── login.html
│   └── signup.html
│
├── static/                      
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
└── DEPLOYMENT.md
```

## 🚀 Local Setup Instructions

### Step 1: Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 3: Navigate to Backend

```powershell
cd backend
```

### Step 4: Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User

```powershell
python manage.py createsuperuser
```

### Step 6: Run Development Server

```powershell
python manage.py runserver
```

### Step 7: Access Application

- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 👥 User Roles & Permissions

### 👤 Regular User
- ✅ Create new quotes
- ✅ View quote details
- ✅ Add items to inventory
- ✅ Submit insurance claims
- ❌ Cannot schedule moves
- ❌ Cannot approve insurance claims
- ❌ Cannot update quote status

### ⚙️ Admin User
- ✅ All regular user permissions
- ✅ Schedule moves
- ✅ Approve/reject insurance claims
- ✅ Update quote status (Pending/Approved/Completed/Cancelled)
- ✅ Full access to Django admin panel

## 💰 Cost Calculation Formula

```
Total Cost = Base Rate + (Distance × Per Km Rate) + (Items × Per Item Rate)
```

Where:
- Base Rate = ₹500
- Per Km Rate = ₹15
- Per Item Rate = ₹50

**Example:**
- 20 items, 50 km distance
- Cost = 500 + (50 × 15) + (20 × 50) = ₹2,250

## 🌐 Deployment

This project is ready for deployment on various platforms. See `DEPLOYMENT.md` for detailed instructions on:

- Railway
- Render
- Heroku
- PythonAnywhere

Quick deployment steps are in `DEPLOYMENT.md`.

## 📝 Available URLs

- `/` - Homepage (Dashboard)
- `/login/` - User Login
- `/signup/` - User Registration
- `/quote/` - Create New Quote
- `/quote/<id>/` - View Quote Details
- `/inventory/` - Manage Inventory
- `/inventory/<id>/` - Inventory for Specific Quote
- `/schedule/` - Schedule Moves (Admin Only)
- `/insurance/` - Insurance Claims
- `/admin/` - Django Admin Panel

## 🔐 Security Notes

- Secret key should be changed in production
- Use environment variables for sensitive data
- Set `DEBUG=False` in production
- Configure `ALLOWED_HOSTS` properly
- Use HTTPS in production

## 📄 License

This project is created for educational purposes.

---

**Built with ❤️ using Django**
