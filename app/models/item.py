from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, ForeignKey

class Item(db.Model):
    __tablename__ = 'items'

    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    details: Mapped[str] = mapped_column(String(1000), nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    is_general: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    availability: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    user = relationship('User', back_populates='items')
    comments = relationship('Comment', back_populates='item')

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            details=data.get('details'),
            image_url=data.get('image_url'),
            latitude=data['latitude'],
            longitude=data['longitude'],
            is_general=data.get('is_general', True),
            availability=data.get('availability', True),
            user_id=data['user_id']
        )

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'title': self.title,
            'details': self.details,
            'image_url': self.image_url,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'is_general': self.is_general,
            'availability': self.availability,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': self.user_id
        }