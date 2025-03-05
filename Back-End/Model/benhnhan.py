# trọng test

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class BenhNhan(Base):
    __tablename__ = "benhnhan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    sdt = Column(String(15), nullable=True)
    quequan = Column(String(255), nullable=True)
    cccd = Column(String(20), unique=True, nullable=True)

    # Liên kết với Lịch hẹn
    lichhen_list = relationship("LichHen", back_populates="benhnhan")
    # Liên kết với Phiếu khám
    phieukham_list = relationship("PhieuKham", back_populates="benhnhan")
    # Liên kết với Đơn thuốc
    donthuoc_list = relationship("DonThuoc", back_populates="benhnhan")
