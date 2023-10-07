```python
# src/app/services/auth_service.py

from flask_login import login_user, logout_user, current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from ..models.user import User
from ..config import Config

class AuthService:
    def __init__(self):
        self.s = Serializer(Config.OAUTH2_CLIENT_SECRET)

    def register_user(self, username, email, password):
        user = User.query.filter_by(username=username).first()

        if user:
            return False, 'Username already exists'

        user = User.query.filter_by(email=email).first()

        if user:
            return False, 'Email already exists'

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return True, 'User created'

    def login_user(self, username, password):
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            token = self.s.dumps({'id': user.id}).decode('utf-8')
            return True, token

        return False, 'Invalid username or password'

    def logout_user(self):
        logout_user()

    def get_current_user(self):
        return current_user

    def verify_token(self, token):
        try:
            data = self.s.loads(token)
        except:
            return None

        return User.query.get(data['id'])
```
