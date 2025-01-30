from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    comment_text: Mapped[str] = mapped_column(String(1000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.item_id'), nullable=False)

    user = relationship('User', back_populates='comments')
    item = relationship('Item', back_populates='comments')

    @classmethod
    def from_dict(cls, data):
        return cls(
            comment_text=data['comment_text'],
            user_id=data['user_id'],
            item_id=data['item_id']
        )

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'comment_text': self.comment_text,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': self.user_id,
            'item_id': self.item_id
        }