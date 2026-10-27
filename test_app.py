
from app import app

def test_student_information():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Information" in response.data
    assert b"Arun Kumar" in response.data
    assert b"24MIS1001" in response.data
    assert b"Software Engineering" in response.data
