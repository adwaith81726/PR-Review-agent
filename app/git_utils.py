import tempfile
import shutil
import git
import os
from app.utils import analyze_code

def clone_and_analyze(repo_url: str, branch: str = "main") -> dict:
    """
    Clone the repo from any git server and analyze its Python files.
    """
    temp_dir = tempfile.mkdtemp()

    try:
        # Clone repo
        repo = git.Repo.clone_from(repo_url, temp_dir, branch=branch)

        results = {}
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            code = f.read()
                        feedback = analyze_code(code)
                        results[file_path] = feedback
                    except Exception as e:
                        results[file_path] = {"error": str(e)}

        return {"status": "success", "analysis": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        # Clean up temporary folder
        shutil.rmtree(temp_dir, ignore_errors=True)
