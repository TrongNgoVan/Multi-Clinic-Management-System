from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class PhongChucNang(Base):
    __tablename__ = "phongchucnang"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chucNang = Column(String(255), nullable=True)
    moTa = Column(Text, nullable=True)

    # Quan hệ ngược với BacSi
    bacsi_list = relationship("BacSi", back_populates="phong")
