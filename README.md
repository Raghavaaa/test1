# Weyou Internship Test System

Complete test assessment platform with admin dashboard and candidate portal.

## 📁 Repository Structure

```
test1/
├── index.html          # Frontend - Candidate test portal
├── script.js           # Frontend - Test logic
├── style.css           # Frontend - Styling
└── backend/            # Backend - Admin dashboard + API
    ├── app.py
    ├── requirements.txt
    └── static/
        └── admin.html
```

## 🚀 Deployment

### 1. Deploy Backend to Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect this GitHub repository
4. Configure:
   - **Name**: `weyou-backend`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free
5. Deploy and copy your backend URL

### 2. Update Frontend

1. Edit `script.js` line 3
2. Replace `REPLACE_WITH_YOUR_BACKEND_URL` with your backend URL
3. Example: `const BACKEND_URL = "https://your-backend.onrender.com/submit";`
4. Commit and push changes

### 3. Deploy Frontend to Render

1. Click **"New +"** → **"Static Site"**
2. Connect same GitHub repository
3. Configure:
   - **Name**: `weyou-frontend`
   - **Root Directory**: `.` (leave empty or use dot)
   - **Build Command**: (leave empty)
   - **Publish Directory**: `.`
   - **Plan**: Free
4. Deploy and copy your frontend URL

## 🎯 Result

- **Backend URL**: Admin dashboard for monitoring
- **Frontend URL**: Share with candidates for testing

## 💡 Features

### Frontend (Candidate Portal)
- 20-minute timed test
- 5 technical sections
- Auto-submit on timeout
- Mobile validation

### Backend (Admin Dashboard)
- Real-time monitoring
- Beautiful web interface
- Search & filter
- CSV export
- View full answers

## 📊 Test Sections

1. Code Reading
2. System Mapping
3. Data Brain
4. Logic Question
5. Micro Decision Case

---

Built with FastAPI + Vanilla JavaScript

