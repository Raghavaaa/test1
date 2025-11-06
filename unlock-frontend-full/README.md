# Frontend Unlock Challenge - Complete System

## 🎯 What This Is

A complete web-based system where candidates:
1. Register with their details
2. Download the broken HTML file
3. Fix all bugs locally
4. Submit the answer code they discover

## 📦 Contains

```
unlock-frontend-full/
├── frontend/
│   ├── index.html             (Registration & test access page)
│   └── broken_webpage.html    (The broken file to download)
└── backend/
    ├── app.py                 (FastAPI server)
    └── requirements.txt       (Dependencies)
```

## 🚀 Deployment

### Backend (Render/Railway):
1. Deploy `backend/` folder
2. Get your backend URL: `https://your-backend.onrender.com`

### Frontend (Netlify/Vercel):
1. Edit `frontend/index.html` line 263:
   ```javascript
   const BACKEND_URL = "https://your-backend.onrender.com";
   ```
2. Deploy `frontend/` folder
3. Get your frontend URL: `https://your-frontend.netlify.app`

## 📊 Candidate Flow

1. Visit frontend URL
2. Fill registration form:
   - Name
   - Mobile
   - Email
   - Branch
   - CGPA
   - Interests
   - Availability
3. Click "Register & Access Test"
4. Download `broken_webpage.html`
5. Fix all 5 bugs locally
6. Open fixed file in browser
7. Enter magic number (42)
8. Copy answer code (WFR2025FE)
9. Submit answer code on the website

## ✅ Data Collected

**Registration:**
- Name, Mobile, Email
- Branch, CGPA
- Interests/Tech Stack
- Availability

**Submission:**
- All registration data
- Answer code submitted
- PASS/FAIL status
- Timestamps

## 📈 Admin Endpoints

- `/results` - View all submissions with pass/fail
- `/registrations` - View all registrations

## 🔑 Answer Code

**Correct Answer:** `WFR2025FE`

System automatically marks as PASS or FAIL.

---

**Complete, professional system ready to deploy!**

