PR Review Agent

An AI-powered code review agent written in *Python (FastAPI)* that works with *multiple Git servers (GitHub, GitLab, Bitbucket, or any Git URL)*.  
The system analyzes Pull Requests (or full repos) for:
- Code structure & complexity  
- Coding standards & style  
- Possible bugs or issues  

---

Project Structure

PR Review agent/ │── app/ │   ├── init.py │   ├── main.py │   ├── routes.py │   ├── utils.py │   ├── git_utils.py │── requirements.txt │── README.md │── venv/

---

 Features
- Upload and analyze individual *files*  
- Clone and analyze a *full repository* from any Git server  
- Feedback provided using:
  - *Pylint* → style, warnings, errors  
  - *Radon* → cyclomatic complexity  
- Modular, extensible architecture  
- REST API with Swagger UI (/docs)  

---

Setup Instructions

### 1. Install Python
Download Python (3.10 or above) from [python.org](https://www.python.org/downloads/).  
Verify installation:
```bash
python --version

2. Clone Project

git clone <your_repo_url>
cd "PR Review agent"

3. Create Virtual Environment

python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate


4. Install Dependencies

pip install -r requirements.txt

If requirements.txt is missing, create it with:

fastapi
uvicorn
pylint
radon
gitpython


---

 Run the Project

From the root folder:

uvicorn app.main:app --reload

Server will be live at:
👉 http://127.0.0.1:8000
👉 http://127.0.0.1:8000/docs


---

📡 API Endpoints

1. Analyze Single File

POST /analyze

Form-data:

file → Python file


Response:

{
  "filename": "example.py",
  "feedback": {
    "pylint": "...",
    "complexity": "..."
  }
}


---

2. Analyze Git Repository

POST /analyze-repo

Form-data:

repo_url → Git repo URL (GitHub/GitLab/Bitbucket/other)

branch → Branch name (default = main)


Example:

curl -X POST "http://127.0.0.1:8000/analyze-repo" \
     -F "repo_url=https://github.com/psf/requests.git" \
     -F "branch=main"

Response:

{
  "status": "success",
  "analysis": {
    "path/to/file1.py": { "pylint": "...", "complexity": "..." },
    "path/to/file2.py": { "pylint": "...", "complexity": "..." }
  }
}




Test Cases

File Upload

Upload a valid Python file → returns pylint + radon feedback

Upload empty file → error message

Upload non-Python file → rejected


Repo Analysis

Valid public repo → cloned + analyzed

Invalid URL → error

Private repo without access → error

Large repo → only Python files analyzed



Future Enhancements

Webhook integration for PR events

Database storage of reports

More analyzers (Bandit, Black, etc.)

Frontend dashboard for results
