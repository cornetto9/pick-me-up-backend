from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str]
    name: Mapped[str]



    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name':self.name
        }
    
    @classmethod
    def from_dict(cls, data):
        return User(email=data['email'], name=data['name'])
            