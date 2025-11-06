from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict
import csv
import os
from datetime import datetime
import json

app = FastAPI(title="Weyou Internship Test Backend")

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define data model
class TestSubmission(BaseModel):
    name: str
    mobile: str
    cgpa: str
    branch: str
    tech_stack: str
    answers: Dict[str, str]
    submission_time: str
    time_taken_seconds: int = 0

# CSV file path
CSV_FILE = "results.csv"
CSV_HEADERS = ["name", "mobile", "cgpa", "branch", "tech_stack", "submission_time", "time_taken_seconds", "Q1", "Q2", "Q3", "Q4", "Q5"]

# Initialize CSV file if it doesn't exist
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

init_csv()

@app.get("/")
def read_root():
    """
    Serve the admin dashboard
    """
    admin_html = os.path.join(os.path.dirname(__file__), "static", "admin.html")
    if os.path.exists(admin_html):
        return FileResponse(admin_html)
    return {
        "message": "Weyou Internship Test Backend",
        "status": "running",
        "endpoints": {
            "dashboard": "/ (GET) - Admin dashboard",
            "submit": "/submit (POST) - Submit test answers",
            "results": "/results (GET) - View all submissions"
        }
    }

@app.get("/api")
def api_info():
    """
    API information endpoint
    """
    return {
        "message": "Weyou Internship Test Backend",
        "status": "running",
        "endpoints": {
            "dashboard": "/ (GET) - Admin dashboard",
            "submit": "/submit (POST) - Submit test answers",
            "results": "/results (GET) - View all submissions",
            "download": "/results/download (GET) - Download CSV"
        }
    }

@app.post("/submit")
async def submit_test(submission: TestSubmission):
    """
    Submit test answers
    """
    try:
        # Validate mobile number (10 digits)
        if not submission.mobile.isdigit() or len(submission.mobile) != 10:
            raise HTTPException(status_code=400, detail="Invalid mobile number")
        
        # Check for duplicate mobile number
        existing_submissions = []
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                existing_submissions = list(reader)
                
            for row in existing_submissions:
                if row['mobile'] == submission.mobile:
                    raise HTTPException(
                        status_code=400,
                        detail="This mobile number has already been used for a submission"
                    )
        
        # Append to CSV
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                submission.name,
                submission.mobile,
                submission.cgpa,
                submission.branch,
                submission.tech_stack,
                submission.submission_time,
                submission.time_taken_seconds,
                submission.answers.get("Q1", ""),
                submission.answers.get("Q2", ""),
                submission.answers.get("Q3", ""),
                submission.answers.get("Q4", ""),
                submission.answers.get("Q5", "")
            ])
        
        return {
            "status": "success",
            "message": "Submission recorded successfully",
            "data": {
                "name": submission.name,
                "mobile": submission.mobile,
                "timestamp": submission.submission_time
            }
        }
    
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/results")
async def get_results():
    """
    Get all test submissions
    """
    try:
        results = []
        
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                results = list(reader)
        
        # Sort by submission time (most recent first)
        results.sort(key=lambda x: x.get('submission_time', ''), reverse=True)
        
        return {
            "status": "success",
            "count": len(results),
            "results": results
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading results: {str(e)}")

@app.get("/results/download")
async def download_results():
    """
    Get raw CSV data for download
    """
    try:
        if not os.path.exists(CSV_FILE):
            return {"status": "success", "data": "No results yet"}
        
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            csv_content = f.read()
        
        return {
            "status": "success",
            "csv_data": csv_content
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

