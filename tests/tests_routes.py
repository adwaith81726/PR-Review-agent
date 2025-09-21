from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "PR Review Agent" in response.json()["message"]

def test_analyze_endpoint(tmp_path):
    test_file = tmp_path / "dummy.py"
    test_file.write_text("print('Hello')")
    with open(test_file, "rb") as f:
        response = client.post("/analyze", files={"file": ("dummy.py", f, "text/x-python")})
    assert response.status_code == 200
    assert "feedback" in response.json()
