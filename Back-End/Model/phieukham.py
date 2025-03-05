from sqlalchemy import Column, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class PhieuKham(Base):
    __tablename__ = "phieukham"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trieuchung = Column(Text, nullable=True)
    chuandoan = Column(Text, nullable=True)
    thongsoxetnghiem = Column(Text, nullable=True)
    ngaykham = Column(DateTime, nullable=False)
    sothutu = Column(Integer, nullable=True)
    tienkham = Column(Float, nullable=True)

    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"))

    benhnhan = relationship("BenhNhan", back_populates="phieukham_list")
    bacsi = relationship("BacSi", back_populates="phieukham_list")
