from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class BenhNhan(Base):
    __tablename__ = "benhnhan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    sdt = Column(String(15), nullable=False)
    quequan = Column(String(255), nullable=False)
    cccd = Column(String(20), unique=True, nullable=False)
    dob = Column(Date, nullable=False)
    img = Column(String(100), nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    # Quan hệ ngược với các bảng khác
    donthuoc_list = relationship("DonThuoc", back_populates="benhnhan")
    lichhen_list = relationship("LichHen", back_populates="benhnhan")
    phieukham_list = relationship("PhieuKham", back_populates="benhnhan")
