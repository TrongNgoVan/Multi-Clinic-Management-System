from sqlalchemy import Column, Integer, String, Text, Date, Float
from DB.db_connection import Base
from sqlalchemy.orm import relationship

class Thuoc(Base):
    __tablename__ = "thuoc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    mota = Column(Text, nullable=True)
    nsx = Column(Date, nullable=True)
    hsd = Column(Date, nullable=True)
    dongia = Column(Float, nullable=True)

    # Liên kết với Chi tiết đơn thuốc
    chitietdonthuoc_list = relationship("ChiTietDonThuoc", back_populates="thuoc")
