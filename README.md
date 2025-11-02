# 🚚 Moving Company Management System

A comprehensive web application built with Django for managing a moving company's operations including customer quotes, move scheduling, inventory tracking, and insurance claims.

## ✨ Features

- **Customer Management**: Store and manage customer information
- **Quote Generation**: Create quotes with automatic cost calculation
- **Inventory Tracking**: Track items for each move
- **Move Scheduling**: Schedule moves with driver and vehicle information
- **Insurance Claims**: Manage insurance claims for moves
- **Admin Panel**: Full Django admin interface for data management

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 5.2.7
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5.3
- **Database**: SQLite
- **Additional Packages**: 
  - Pillow (image handling)
  - django-crispy-forms (form rendering)
  - reportlab (PDF generation - ready for future use)

## 📁 Project Structure

```
moving_company_management/
│
├── backend/
│   ├── manage.py
│   ├── backend/                 # Main project folder (settings, URLs)
│   └── company/                 # Django app (main logic)
│       ├── models.py            # Database models
│       ├── views.py             # View functions
│       ├── urls.py              # URL routing
│       └── admin.py             # Admin configuration
│
├── templates/                   # All HTML templates
│   ├── base.html
│   ├── home.html
│   ├── quote_form.html
│   ├── quote_detail.html
│   ├── inventory.html
│   ├── schedule.html
│   └── insurance.html
│
├── static/                      # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── venv/                        # Virtual environment
└── README.md
```

## 🚀 Setup Instructions

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

All dependencies should already be installed. If not, run:
```bash
pip install django pillow django-crispy-forms reportlab
```

### 3. Run Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

Admin Panel: **http://127.0.0.1:8000/admin/**

## 💰 Cost Calculation Formula

The system automatically calculates moving costs using:

```
Total Cost = Base Rate + (Distance × Per Km Rate) + (Items × Per Item Rate)
```

Where:
- Base Rate = ₹500
- Per Km Rate = ₹15
- Per Item Rate = ₹50

Example:
- 20 items, 50 km distance
- Cost = 500 + (50 × 15) + (20 × 50) = 500 + 750 + 1000 = ₹2,250

## 📝 Usage Guide

### Creating a Quote

1. Navigate to "New Quote" from the navigation menu
2. Fill in customer information
3. Enter move details (date, items, distance)
4. The system automatically calculates the estimated cost
5. Submit to create the quote

### Managing Inventory

1. Go to "Inventory" page
2. Select a quote
3. Add items with quantities and fragility status

### Scheduling Moves

1. Go to "Schedule" page
2. Select a quote
3. Choose date, time, driver, and vehicle
4. Save the schedule

### Insurance Claims

1. Go to "Insurance" page
2. Select a quote
3. Enter claim details and status
4. Submit to create the claim

## 🔐 Admin Panel

Access the Django admin panel at `/admin/` to:
- View and edit all database records
- Manage customers, quotes, inventory, schedules, and insurance claims
- Perform bulk operations
- Export data

## 🎨 Customization

### Modifying Cost Calculation

Edit the `calculate_cost()` function in `backend/company/views.py`:

```python
def calculate_cost(items, distance):
    base_rate = 500  # Change this
    per_km_rate = 15  # Change this
    per_item_rate = 50  # Change this
    return base_rate + (per_km_rate * distance) + (per_item_rate * items)
```

### Styling

Modify `static/css/style.css` to customize the appearance.

## 🚧 Future Enhancements

- Customer authentication system
- Email notifications
- PDF invoice generation
- Image uploads for inventory items
- Advanced reporting and analytics
- Mobile app integration

## 📄 License

This project is created for educational purposes.

## 👤 Author

Moving Company Management System - 2025

---

**Happy Moving! 🚚**

