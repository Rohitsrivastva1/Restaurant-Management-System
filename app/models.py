from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

class MenuSection(Base):
    __tablename__ = "MenuSections"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class MenuItem(Base):
    __tablename__ = "MenuItems"
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey("MenuSections.id"))
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(DECIMAL(10, 2), nullable=False)
    is_active = Column(Boolean, default=True)
    section = relationship("MenuSection", back_populates="items")

class Order(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=func.now())

class OrderItem(Base):
    __tablename__ = "OrderItems"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("Orders.id"))
    menu_item_id = Column(Integer, ForeignKey("MenuItems.id"))
    quantity = Column(Integer, nullable=False)
