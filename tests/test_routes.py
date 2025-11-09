import requests

BASE_URL = "http://127.0.0.1:5000"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert "ok" in r.text.lower()

def test_academic_chat():
    payload = {"user_id": "stu_01", "message": "Explain recursion"}
    r = requests.post(f"{BASE_URL}/chat", json=payload)
    assert r.status_code == 200
    assert "academic" in r.text.lower()

def test_productivity_chat():
    payload = {"user_id": "stu_01", "message": "Plan my study schedule"}
    r = requests.post(f"{BASE_URL}/chat", json=payload)
    assert r.status_code == 200

def test_mental_health_chat():
    payload = {"user_id": "stu_01", "message": "I'm anxious about exams"}
    r = requests.post(f"{BASE_URL}/chat", json=payload)
    assert r.status_code == 200

def test_admin_chat():
    payload = {"user_id": "stu_01", "message": "Find scholarships for CS students"}
    r = requests.post(f"{BASE_URL}/chat", json=payload)
    assert r.status_code == 200

def test_clear_memory():
    payload = {"user_id": "stu_01"}
    r = requests.post(f"{BASE_URL}/clear", json=payload)
    assert r.status_code == 200
