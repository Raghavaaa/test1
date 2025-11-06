from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import csv
import os
from datetime import datetime

app = FastAPI(title="Frontend Unlock Challenge Backend")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class CandidateRegistration(BaseModel):
    name: str
    mobile: str
    email: str
    branch: str
    cgpa: str
    interests: str
    availability: str
    registration_time: str

class AnswerSubmission(BaseModel):
    name: str
    mobile: str
    email: str
    branch: str
    cgpa: str
    interests: str
    availability: str
    registration_time: str
    answer_code: str
    submission_time: str

# CSV files
REGISTRATIONS_FILE = "registrations.csv"
SUBMISSIONS_FILE = "submissions.csv"
CORRECT_ANSWER = "WFR2025FE"

# CSV headers
REGISTRATION_HEADERS = ["name", "mobile", "email", "branch", "cgpa", "interests", "availability", "registration_time"]
SUBMISSION_HEADERS = ["name", "mobile", "email", "branch", "cgpa", "interests", "availability", "registration_time", "answer_code", "submission_time", "is_correct"]

# Initialize CSV files
def init_csv():
    if not os.path.exists(REGISTRATIONS_FILE):
        with open(REGISTRATIONS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(REGISTRATION_HEADERS)
    
    if not os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(SUBMISSION_HEADERS)

init_csv()

@app.get("/")
def read_root():
    return {
        "message": "Frontend Unlock Challenge Backend",
        "status": "running",
        "endpoints": {
            "register": "/register (POST)",
            "submit": "/submit (POST)",
            "results": "/results (GET)"
        }
    }

@app.post("/register")
async def register_candidate(registration: CandidateRegistration):
    """
    Register a new candidate
    """
    try:
        # Check for duplicate mobile
        existing = []
        with open(REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing = list(reader)
        
        for row in existing:
            if row['mobile'] == registration.mobile:
                raise HTTPException(
                    status_code=400,
                    detail="This mobile number is already registered"
                )
        
        # Save registration
        with open(REGISTRATIONS_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                registration.name,
                registration.mobile,
                registration.email,
                registration.branch,
                registration.cgpa,
                registration.interests,
                registration.availability,
                registration.registration_time
            ])
        
        return {
            "status": "success",
            "message": "Registration successful",
            "data": {
                "name": registration.name,
                "mobile": registration.mobile
            }
        }
    
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.post("/submit")
async def submit_answer(submission: AnswerSubmission):
    """
    Submit answer code
    """
    try:
        # Check if answer is correct
        is_correct = submission.answer_code.upper() == CORRECT_ANSWER
        
        # Save submission
        with open(SUBMISSIONS_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                submission.name,
                submission.mobile,
                submission.email,
                submission.branch,
                submission.cgpa,
                submission.interests,
                submission.availability,
                submission.registration_time,
                submission.answer_code,
                submission.submission_time,
                "PASS" if is_correct else "FAIL"
            ])
        
        return {
            "status": "success",
            "message": "Answer submitted successfully",
            "is_correct": is_correct,
            "data": {
                "name": submission.name,
                "answer_code": submission.answer_code,
                "result": "PASS" if is_correct else "FAIL"
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/results")
async def get_results():
    """
    Get all submissions with time taken calculations
    """
    try:
        results = []
        
        if os.path.exists(SUBMISSIONS_FILE):
            with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                results = list(reader)
        
        # Calculate time taken for each submission
        for result in results:
            try:
                reg_time = datetime.fromisoformat(result['registration_time'].replace('Z', '+00:00'))
                sub_time = datetime.fromisoformat(result['submission_time'].replace('Z', '+00:00'))
                time_diff = (sub_time - reg_time).total_seconds()
                
                # Format time
                minutes = int(time_diff // 60)
                seconds = int(time_diff % 60)
                result['time_taken'] = f"{minutes}m {seconds}s"
                result['time_taken_seconds'] = int(time_diff)
            except Exception:
                result['time_taken'] = "Unknown"
                result['time_taken_seconds'] = 0
        
        # Sort by submission time
        results.sort(key=lambda x: x.get('submission_time', ''), reverse=True)
        
        # Count stats
        total = len(results)
        passed = len([r for r in results if r.get('is_correct') == 'PASS'])
        failed = total - passed
        
        # Calculate average time for passed candidates
        passed_times = [r['time_taken_seconds'] for r in results if r.get('is_correct') == 'PASS' and r.get('time_taken_seconds', 0) > 0]
        avg_time_seconds = sum(passed_times) / len(passed_times) if passed_times else 0
        avg_minutes = int(avg_time_seconds // 60)
        avg_seconds = int(avg_time_seconds % 60)
        
        # Find fastest
        fastest_time = min(passed_times) if passed_times else 0
        fastest_minutes = int(fastest_time // 60)
        fastest_seconds = int(fastest_time % 60)
        
        return {
            "status": "success",
            "stats": {
                "total_submissions": total,
                "passed": passed,
                "failed": failed,
                "pass_rate": f"{(passed/total*100):.1f}%" if total > 0 else "0%",
                "avg_time": f"{avg_minutes}m {avg_seconds}s",
                "fastest_time": f"{fastest_minutes}m {fastest_seconds}s"
            },
            "results": results
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading results: {str(e)}")

@app.get("/registrations")
async def get_registrations():
    """
    Get all registrations
    """
    try:
        registrations = []
        
        if os.path.exists(REGISTRATIONS_FILE):
            with open(REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                registrations = list(reader)
        
        return {
            "status": "success",
            "count": len(registrations),
            "registrations": registrations
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading registrations: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

