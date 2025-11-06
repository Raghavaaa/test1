# Backend Unlock Challenge - Complete System

## 🎯 What This Is

A complete web-based system where candidates:
1. **Register** with their details (name, mobile, email, branch, CGPA, interests, availability)
2. **Download** the broken Python file from the website
3. **Fix** all 5 bugs locally
4. **Run** the fixed code to get answer code
5. **Submit** the answer code on the website

## 📦 Structure

```
unlock-backend-full/
├── frontend/
│   ├── index.html          (Registration page + test download)
│   └── broken_api.py       (The broken file to fix)
└── backend/
    ├── app.py              (FastAPI server)
    └── requirements.txt    (Dependencies)
```

## 🚀 Deployment

### Step 1: Deploy Backend
1. Upload `backend/` to Render/Railway
2. Configure:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`
3. Get backend URL: `https://backend-unlock.onrender.com`

### Step 2: Update Frontend
1. Edit `frontend/index.html` line 263:
   ```javascript
   const BACKEND_URL = "https://your-backend-url.onrender.com";
   ```
2. Save the file

### Step 3: Deploy Frontend
1. Upload `frontend/` to Netlify/Vercel
2. Deploy as static site
3. Get frontend URL: `https://backend-unlock-test.netlify.app`

## 📊 Candidate Experience

1. **Visit your frontend URL**
2. **Fill registration form:**
   - Full Name
   - Mobile Number (10 digits)
   - Email ID
   - Branch/Stream
   - CGPA (0-10)
   - Interests/Tech Stack
   - Availability in Next 15 Days

3. **Click "Register & Access Test"**
4. **Download** `broken_api.py` (or copy code from page)
5. **Fix all 5 bugs** in their editor
6. **Run:** `python broken_api.py`
7. **See answer code:** `WBK2025BE`
8. **Submit code** on the website

## 🔑 Bugs in File (5 total)

1. Variable typo: `SECRET_ANSER_CODE` → `SECRET_ANSWER_CODE`
2. Wrong operator: `num_documents + 2` → `num_documents * 2`
3. Missing colon: `def generate_report(case_type, num_documents)` → add `:`
4. Missing argument: `calculate_complexity(case_type)` → `calculate_complexity(case_type, num_documents)`
5. Wrong variable: `SECRET_ANSER_CODE` → `SECRET_ANSWER_CODE`

## ✅ Answer Code

**Correct:** `WBK2025BE`

Backend automatically checks and marks as PASS/FAIL.

## 📈 Admin Endpoints

- `GET /results` - All submissions with PASS/FAIL status
- `GET /registrations` - All candidate registrations

## 📊 Data Stored

### registrations.csv
- Name, Mobile, Email
- Branch, CGPA
- Interests, Availability
- Registration timestamp

### submissions.csv
- All registration data
- Answer code submitted
- PASS or FAIL
- Submission timestamp

---

**Complete system ready to deploy!**

