from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import validates
from back.models.base_model import BaseModel
from back.utils.validators import validate_type, validate_not_empty, validate_lenght, validate_greater_than


class Product(BaseModel):
    __tablename__ = 'PRODUCT11'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    price = Column('price', Float, nullable=False)
    amount = Column('amount', Integer, nullable=False)

    def __init__(self, name: str, description: str, price: float, amount: int = 0) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
    
    @validates('name')
    def validate_name(self, key, name):
        validate_type(name, str, key)
        validate_not_empty(name, key)
        validate_lenght(name, 100, key)
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not description:
            return description
        validate_type(description, str, key)
        validate_lenght(description, 255, key)
        return description

    @validates('price')
    def validate_price(self, key, price):
        validate_type(price, float, key)
        validate_greater_than(price, key, 1)
        return price

    @validates('amount')
    def validate_amount(self, key, amount):
        validate_type(amount, int, key)
        validate_greater_than(amount, key, 0)
        return amount