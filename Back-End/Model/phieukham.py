from sqlalchemy import Column, Integer, Text, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class PhieuKham(Base):
    __tablename__ = "phieukham"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trieuchung = Column(Text, nullable=True)
    chuandoan = Column(Text, nullable=False)
    thongsoxetnghiem = Column(Text, nullable=True)
    anhxetnghiem = Column(String(255), nullable=True)
    ngaykham = Column(DateTime, nullable=False)
    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"), nullable=False)
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"), nullable=False)
    tienkham = Column(Float, nullable=False)

    # Quan hệ
    benhnhan = relationship("BenhNhan", back_populates="phieukham_list")
    bacsi = relationship("BacSi", back_populates="phieukham_list")
