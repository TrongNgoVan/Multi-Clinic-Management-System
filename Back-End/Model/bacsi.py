from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class BacSi(Base):
    __tablename__ = "bacsi"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    dob = Column(Date, nullable=False)
    chuyenmon = Column(String(255), nullable=False)
    hocvan = Column(String(100), nullable=False)
    kinhnghiem = Column(String(100), nullable=False)
    img = Column(String(100), nullable=False)
    phong_id = Column(Integer, ForeignKey("phongchucnang.id"), nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    # Quan hệ ngược với các bảng khác
    phong = relationship("PhongChucNang", back_populates="bacsi_list")
    donthuoc_list = relationship("DonThuoc", back_populates="bacsi")
    lichhen_list = relationship("LichHen", back_populates="bacsi")
    phieukham_list = relationship("PhieuKham", back_populates="bacsi")
