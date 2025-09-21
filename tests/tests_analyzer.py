from app.analyzer import analyze_code
import os

def test_analyze_code(tmp_path):
    test_file = tmp_path / "test.py"
    test_file.write_text("print('Hello World')")
    result = analyze_code(str(test_file))
    assert "feedback" in result
    assert "issues" in result
