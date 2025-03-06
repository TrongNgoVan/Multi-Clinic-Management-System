from sqlalchemy import Column, Integer, String, Text, Date, Float
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class Thuoc(Base):
    __tablename__ = "thuoc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=True)
    mota = Column(Text, nullable=True)
    nsx = Column(Date, nullable=True)
    hsd = Column(Date, nullable=True)
    dongia = Column(Float, nullable=True)

    # Quan hệ
    chitietdonthuoc_list = relationship("ChiTietDonThuoc", back_populates="thuoc")
