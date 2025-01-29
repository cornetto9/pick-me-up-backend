from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf8')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username':self.username
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(
            email=data['email'],
            username=data['username']
        )
        user.password = data['password']
        return user
            