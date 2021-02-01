from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from src.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        if not name.strip():
            raise ValueError("Name can't be empty value")
        if len(name) > 100:
            raise ValueError("Name length is more than 100 characters")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be str")
        if len(description) > 255:
            raise ValueError("Description length is more than 100 characters")
        return description
