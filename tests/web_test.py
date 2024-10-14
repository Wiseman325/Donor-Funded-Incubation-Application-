#import responses 
from website.models import User, Scholarship

def test_home(client):
    response = client.get("/")
    assert b"<title>Home</title>" in response.data

def test_registration(client, app):
    response = client.post("/sign-up", data={"email": "wisemanmlora@gmail.com", "first_name": "Mlondi"})

    with app.app_context():
        assert User.query.count() == 6
        assert User.query.first().email == "wisemanmlora@gmail.com"

def test_invalid_login(client):
    client.post("/login", data={"email": "wisemanmlora@gmail.com", "password": "testpassword"})

def test_scholarships(client, app):
    with app.app_context():
        assert Scholarship.query.count() == 7
        assert Scholarship.query.first().title == "wrcdbl;cqN"

def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200