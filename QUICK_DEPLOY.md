# ⚡ Quick Deployment Guide

## 🚀 Fastest Way to Deploy (Railway - Recommended)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Deploy on Railway
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Django
5. Add environment variables:
   - `SECRET_KEY` (generate with command below)
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app-name.railway.app`
6. Deploy! Your app is live

### 3. Create Admin User
In Railway dashboard → Deployments → View Logs → Run:
```bash
railway run python backend/manage.py createsuperuser
```

**Generate Secret Key:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📦 All Deployment Files Included

✅ **requirements.txt** - All dependencies
✅ **Procfile** - Heroku/Railway deployment
✅ **runtime.txt** - Python version
✅ **.gitignore** - Ignore unnecessary files
✅ **DEPLOYMENT.md** - Detailed deployment guide
✅ **render.yaml** - Render platform config
✅ **railway.json** - Railway platform config

---

## 🔧 Environment Variables Needed

Set these in your deployment platform:

```
SECRET_KEY=<generate-a-long-random-key>
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

For PostgreSQL (optional):
```
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

---

## ✅ After Deployment

1. Run migrations: `python backend/manage.py migrate`
2. Create admin: `python backend/manage.py createsuperuser`
3. Test all features
4. Your app is live! 🎉

See `DEPLOYMENT.md` for platform-specific instructions.

