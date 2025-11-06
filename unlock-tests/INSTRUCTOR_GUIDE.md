# Instructor Guide - Unlock-Style Tests

## 🎯 Test Concept

These are **"unlock"** style tests where candidates must fix broken code to reveal a secret answer code. Only when they fix ALL bugs and run the program successfully will they see the code they need to submit.

**Key Advantage:** You know they actually fixed and ran the code (not just guessed or got help without understanding).

---

## 📦 Two Tests Available

### 1. Frontend Test
- **File:** `broken_webpage.html`
- **Skills:** HTML, CSS, JavaScript debugging
- **Bugs:** 5 bugs to fix
- **Answer Code:** `WFR2025FE`
- **Magic Number:** 42 (they need to figure this out)
- **Time:** 30 minutes

### 2. Backend Test
- **File:** `broken_api.py`
- **Skills:** Python debugging, API logic
- **Bugs:** 5 bugs to fix
- **Answer Code:** `WBK2025BE`
- **Time:** 30 minutes

---

## 🚀 How to Administer

### Option 1: Individual Tests
Send one or both tests based on role:
- **Frontend position** → Frontend test only
- **Backend position** → Backend test only  
- **Full-stack position** → Both tests

### Option 2: Sequential Testing
```
Frontend Test (30 min) → Submit code
       ↓ (5 min break)
Backend Test (30 min) → Submit code
```

### Option 3: Choice Testing
Let candidate choose which test to take first, then optionally take the second.

---

## 📧 How to Send to Candidates

### For Frontend Test:
```
Subject: Weyou Frontend Debugging Challenge

Hi [Name],

Please complete the attached frontend debugging challenge.

Files attached:
- broken_webpage.html (to fix)
- README.md (instructions)

Steps:
1. Fix all bugs in the HTML file
2. Open in browser
3. Find the magic number and enter it
4. Copy the answer code that appears
5. Submit the answer code via reply

Time limit: 30 minutes
Due: [Date & Time]

Good luck!
```

### For Backend Test:
```
Subject: Weyou Backend Debugging Challenge

Hi [Name],

Please complete the attached backend debugging challenge.

Files attached:
- broken_api.py (to fix)
- README.md (instructions)

Steps:
1. Fix all bugs in the Python file
2. Run: python broken_api.py
3. Copy the answer code that appears
4. Submit the answer code via reply

Time limit: 30 minutes
Due: [Date & Time]

Good luck!
```

---

## ✅ Verifying Submissions

### Correct Answers:
- **Frontend Test:** `WFR2025FE`
- **Backend Test:** `WBK2025BE`

### If Candidate Submits Correct Code:
✅ They fixed all bugs  
✅ They ran the program successfully  
✅ **PASS** - Full credit (100 points)

### If Candidate Submits Wrong/No Code:
❌ Did not fix all bugs  
❌ Did not run successfully  
❌ **FAIL** - 0 points

### Partial Credit (Optional):
You can ask them to submit their fixed code for review if they couldn't get the answer code. Give partial credit based on bugs fixed.

---

## 🐛 Bug Summary

### Frontend Test (5 bugs):
1. CSS property typo: `dispaly` → `display`
2. Button class typo: `btn-submitt` → `btn-submit`
3. JS method typo: `getElementByID` → `getElementById`
4. Assignment instead of comparison: `=` → `==`
5. Magic number: Need to figure out it's 42

### Backend Test (5 bugs):
1. Variable typo: `SECRET_ANSER_CODE` → `SECRET_ANSWER_CODE`
2. Wrong operator: `+` → `*`
3. Missing colon after function definition
4. Missing argument in function call
5. Wrong variable name (same as bug #1)

---

## 🎓 Skills Assessed

### Frontend Test:
- HTML debugging
- CSS syntax knowledge
- JavaScript debugging
- DOM manipulation understanding
- Problem-solving
- Browser DevTools usage

### Backend Test:
- Python syntax knowledge
- Debugging skills
- API logic understanding
- Testing mindset
- Error handling
- Code reading comprehension

---

## ⏱️ Time Expectations

| Skill Level | Frontend | Backend |
|-------------|----------|---------|
| Beginner | 40-50 min | 40-50 min |
| Intermediate | 25-35 min | 25-35 min |
| Advanced | 15-25 min | 15-25 min |

---

## 💡 Hints (If Candidates Are Stuck)

### Frontend Hints:
1. "Check your CSS property spellings"
2. "HTML IDs and classes must match exactly"
3. "JavaScript methods are case-sensitive"
4. "Compare vs assign: = vs =="
5. "The magic number is famous in sci-fi"

### Backend Hints:
1. "Check variable names for typos"
2. "Look at mathematical operators carefully"
3. "Python functions need colons"
4. "Count function parameters vs arguments"
5. "Variable names must be consistent"

---

## 📊 Grading Options

### Option 1: Binary (Pass/Fail)
- Correct code = 100 points (Pass)
- Wrong/no code = 0 points (Fail)

### Option 2: Tiered
- Correct code = 100 points
- Submitted code + 4-5 bugs fixed = 70 points
- Submitted code + 3 bugs fixed = 50 points
- Submitted code + 1-2 bugs fixed = 30 points
- No submission = 0 points

### Option 3: Detailed Rubric
- Each bug fixed = 15 points (×5 = 75 points)
- Correct submission = 25 points
- **Total = 100 points**

---

## 🔐 Answer Code Security

The answer codes are embedded in the files:
- Frontend: `WFR2025FE` (in JavaScript variable)
- Backend: `WBK2025BE` (in Python constant)

**Security measures:**
✅ Codes only revealed when program runs successfully  
✅ Can't be found by just searching the file (need to understand code)  
✅ Unique codes per test  
✅ Easy to verify  

**To change codes:**
- Edit `SECRET_CODE` in broken_webpage.html
- Edit `SECRET_ANSWER_CODE` in broken_api.py
- Update ANSWER_KEY.md

---

## 📁 File Structure

```
unlock-tests/
├── frontend-test/
│   ├── broken_webpage.html    (broken code - send to candidates)
│   └── README.md              (instructions - send to candidates)
├── backend-test/
│   ├── broken_api.py          (broken code - send to candidates)
│   └── README.md              (instructions - send to candidates)
├── ANSWER_KEY.md              (solutions - KEEP CONFIDENTIAL)
└── INSTRUCTOR_GUIDE.md        (this file)
```

---

## 🚫 Common Issues

### Frontend Test:
**Issue:** Candidate can't see the result  
**Cause:** CSS `display` bug not fixed  
**Hint:** "Check DevTools console for errors"

**Issue:** Button click doesn't work  
**Cause:** Class name mismatch  
**Hint:** "Check HTML class matches CSS selector"

### Backend Test:
**Issue:** Syntax errors when running  
**Cause:** Missing colon or other syntax issues  
**Hint:** "Python will tell you the line number"

**Issue:** Logic errors after fixing syntax  
**Cause:** Missing arguments or wrong operators  
**Hint:** "Check function calls have all required parameters"

---

## 🎯 Integration with Other Tests

These can be used:
1. **Standalone** - Send as the only test
2. **After online test** - As a follow-up to the 20-min online test
3. **Interview stage** - During technical interview
4. **Take-home** - As homework assignment
5. **Combined** - Both frontend + backend together

---

## 📈 Success Metrics

**Target pass rate:** 40-60%
- Too high (>80%) → Tests are too easy
- Too low (<20%) → Tests might be too hard or unclear

**Average time to complete:**
- Should be around 25-30 minutes for intermediate level
- Adjust difficulty if consistently taking much longer or shorter

---

## ✅ Checklist for Administering

Before sending:
- [ ] Prepare candidate email
- [ ] Attach correct files (broken code + README)
- [ ] Set clear deadline
- [ ] Note answer code in your records
- [ ] Prepare hint strategy if needed

After receiving submission:
- [ ] Check if code matches exactly
- [ ] If correct → Mark as passed
- [ ] If incorrect → Review their code (optional)
- [ ] Provide feedback (optional)

---

## 🎓 Educational Value

These tests teach:
- **Real debugging workflow** - How professionals actually debug
- **Attention to detail** - Small typos matter
- **Testing mindset** - Run and verify your fixes
- **Problem-solving** - Work through errors systematically
- **Tools usage** - Browser DevTools, Python error messages

---

**Keep ANSWER_KEY.md confidential!** 🔒

Only share broken files and README with candidates.

