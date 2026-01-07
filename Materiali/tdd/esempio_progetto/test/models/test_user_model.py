# tests/models/test_user_model.py - test per il modello User

from models import User

def test_create_user():
    user = User('Alice', 25)
    assert user.name == 'Alice'
    assert user.age == 25