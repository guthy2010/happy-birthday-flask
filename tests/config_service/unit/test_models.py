from app.happy_birthday.models import Users

# Test database models
def test_user_model():
    user = Users(username='sally',dateOfBirth='1991-11-11T00:00:00')
    assert len(user.username) != 0
    assert len(user.dateOfBirth)!= 0

