import subprocess

def run_pylint(code_file: str) -> str:
    """Run pylint on a Python file and return results."""
    result = subprocess.run(
        ["pylint", code_file, "--score=n"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def run_radon(code_file: str) -> str:
    """Run radon complexity analysis."""
    result = subprocess.run(
        ["radon", "cc", code_file],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def analyze_code(filepath: str) -> dict:
    """Run static analysis tools and return combined report."""
    pylint_report = run_pylint(filepath)
    radon_report = run_radon(filepath)

    feedback = "Code analysis completed."
    issues = [pylint_report, radon_report]

    return {"feedback": feedback, "issues": issues}
