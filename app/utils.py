import subprocess

def analyze_code(code: str) -> dict:
    """Analyze Python code using pylint + radon."""
    results = {}

    try:
        # Save code to temp file
        with open("temp_code.py", "w", encoding="utf-8") as f:
            f.write(code)

        # Run pylint
        pylint_output = subprocess.getoutput("pylint temp_code.py --disable=all --enable=errors,warnings")
        results["pylint"] = pylint_output

        # Run radon for complexity
        radon_output = subprocess.getoutput("radon cc temp_code.py -s")
        results["complexity"] = radon_output

    except Exception as e:
        results["error"] = str(e)

    return results
