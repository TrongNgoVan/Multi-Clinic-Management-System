from sqlalchemy import Column, Integer, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class DonThuoc(Base):
    __tablename__ = "donthuoc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaymua = Column(DateTime, nullable=True)
    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"), nullable=True)
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"), nullable=True)
    tonggia = Column(Float, nullable=True)
    mota = Column(String(100), nullable=True)

    # Quan hệ
    benhnhan = relationship("BenhNhan", back_populates="donthuoc_list")
    bacsi = relationship("BacSi", back_populates="donthuoc_list")
    chitietdonthuoc_list = relationship("ChiTietDonThuoc", back_populates="donthuoc")
