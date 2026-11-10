from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Float, Integer, Column, CheckConstraint

Base = declarative_base()

class Product(Base):

    __tablename__ = 'product'
    __table_args__ = (
        CheckConstraint('id >= 1', name='check_product_id'),
        CheckConstraint('price >= 1', name='check_product_price'),
        CheckConstraint('quantity >= 1',name='check_product_quantity')
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)