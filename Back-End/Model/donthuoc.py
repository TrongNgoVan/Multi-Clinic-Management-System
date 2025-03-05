from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class DonThuoc(Base):
    __tablename__ = "donthuoc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaymua = Column(DateTime, nullable=False)
    tonggia = Column(Float, nullable=True)

    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"))

    benhnhan = relationship("BenhNhan", back_populates="donthuoc_list")
    bacsi = relationship("BacSi", back_populates="donthuoc_list")

    chitiet_list = relationship("ChiTietDonThuoc", back_populates="donthuoc")
