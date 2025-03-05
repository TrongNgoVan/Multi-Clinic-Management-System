from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class ChiTietDonThuoc(Base):
    __tablename__ = "chitietdonthuoc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    donthuoc_id = Column(Integer, ForeignKey("donthuoc.id"))
    thuoc_id = Column(Integer, ForeignKey("thuoc.id"))
    soluong = Column(Integer, nullable=False)
    gia = Column(Float, nullable=True)

    donthuoc = relationship("DonThuoc", back_populates="chitiet_list")
    thuoc = relationship("Thuoc", back_populates="chitietdonthuoc_list")
