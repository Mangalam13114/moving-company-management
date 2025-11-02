# 🚀 Deployment Guide - Moving Company Management System

This guide explains how to deploy the Moving Company Management System to various platforms.

## 📋 Pre-Deployment Checklist

- [x] All dependencies listed in `requirements.txt`
- [x] Static files configuration
- [x] Environment variables setup
- [x] Database migration ready
- [x] Security settings configured

---

## 🌐 Deployment Platforms

### Option 1: Railway (Recommended - Easy & Free)

#### Steps:

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository

3. **Configure Environment Variables**
   - Go to Variables tab
   - Add:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.railway.app
     ```

4. **Set Build Command** (if needed)
   - Railway will auto-detect Django
   - No additional commands needed

5. **Deploy**
   - Railway will automatically deploy
   - Your app will be live at: `https://your-app-name.railway.app`

#### Create Admin User:
```bash
railway run python backend/manage.py createsuperuser
```

---

### Option 2: Render (Free Tier Available)

#### Steps:

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your repository

3. **Configure Service**
   - **Name:** moving-company-app
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && cd backend && python manage.py collectstatic --noinput`
   - **Start Command:** `cd backend && gunicorn backend.wsgi:application`

4. **Add Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.onrender.com
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment

#### Create Admin User:
Use Render Shell:
```bash
cd backend
python manage.py createsuperuser
```

---

### Option 3: Heroku

#### Steps:

1. **Install Heroku CLI**
   - Download from https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Run Migrations**
   ```bash
   heroku run python backend/manage.py migrate
   ```

7. **Create Admin User**
   ```bash
   heroku run python backend/manage.py createsuperuser
   ```

---

### Option 4: PythonAnywhere

#### Steps:

1. **Create Account**
   - Go to https://www.pythonanywhere.com
   - Sign up for free account

2. **Open Bash Console**
   - Upload project files via Files tab
   - Open Bash console

3. **Setup Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab
   - Click "Add a new web app"
   - Select "Manual configuration"
   - Select Python 3.10
   - Set source code path

5. **Edit WSGI Configuration**
   ```python
   import os
   import sys
   
   path = '/home/yourusername/yourproject'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.backend.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. **Run Migrations**
   ```bash
   python backend/manage.py migrate
   python backend/manage.py collectstatic
   ```

---

## 🔐 Environment Variables

Create a `.env` file (for local) or set in platform:

```env
SECRET_KEY=your-super-secret-key-here-min-50-characters
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### Generate Secret Key:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📦 Post-Deployment Steps

### 1. Run Migrations
```bash
python backend/manage.py migrate
```

### 2. Collect Static Files
```bash
python backend/manage.py collectstatic --noinput
```

### 3. Create Admin User
```bash
python backend/manage.py createsuperuser
```

### 4. Test the Application
- Visit your deployed URL
- Test login/signup
- Create a test quote
- Verify all features work

---

## 🗄️ Database Setup

### For SQLite (Default):
- Works out of the box
- Data persists in `backend/db.sqlite3`

### For PostgreSQL (Production Recommended):
1. Create database on your platform
2. Get DATABASE_URL
3. Set environment variable:
   ```
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```
4. Run migrations

---

## 🔧 Troubleshooting

### Static Files Not Loading:
```bash
python backend/manage.py collectstatic --noinput
```

### Migration Errors:
```bash
python backend/manage.py migrate --run-syncdb
```

### Permission Errors:
- Check file permissions
- Ensure staticfiles directory is writable

### 500 Internal Server Error:
- Check DEBUG=False in production
- Review server logs
- Verify ALLOWED_HOSTS includes your domain

---

## 📝 Platform-Specific Notes

### Railway:
- Auto-detects Django
- Handles static files automatically
- Free tier available

### Render:
- Free tier: 750 hours/month
- Sleeps after inactivity
- Static files served automatically

### Heroku:
- Free tier discontinued
- Requires credit card for some features
- Good for production

### PythonAnywhere:
- Free tier available
- Great for beginners
- Easy database setup

---

## ✅ Verification Checklist

After deployment, verify:
- [ ] Homepage loads
- [ ] Login/Signup works
- [ ] Can create quotes
- [ ] Can manage inventory
- [ ] Insurance claims work
- [ ] Admin panel accessible (for admins)
- [ ] Schedule page works (for admins)
- [ ] Static files (CSS/JS) load correctly
- [ ] Images/forms display properly

---

**Your app is now live! 🎉**

