from fastapi import APIRouter, UploadFile, File, Form
from app.utils import analyze_code
from app.git_utils import clone_and_analyze

router = APIRouter()

@router.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    """Analyze an uploaded file (existing feature)."""
    code = await file.read()
    feedback = analyze_code(code.decode("utf-8"))
    return {"filename": file.filename, "feedback": feedback}


@router.post("/analyze-repo")
async def analyze_repo(repo_url: str = Form(...), branch: str = Form("main")):
    """Clone and analyze a repo from GitHub/GitLab/Bitbucket."""
    result = clone_and_analyze(repo_url, branch)
    return result
