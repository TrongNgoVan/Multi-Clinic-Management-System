# trọng test
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

#  trọngtrọng

class BacSi(Base):
    __tablename__ = "bacsi"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(100), nullable=False)
    sdt = Column(String(15), nullable=False)
    chucvu = Column(String(50), nullable=True)
    tendangnhap = Column(String(50), nullable=False)
    matkhau = Column(String(50), nullable=False)

    # Phòng chức năng
    phong_id = Column(Integer, ForeignKey("phongchucnang.id"))
    phong = relationship("PhongChucNang", back_populates="bacsi_list")

    # Liên kết với các bảng khác
    # - Lịch hẹn
    lichhen_list = relationship("LichHen", back_populates="bacsi")
    # - Phiếu khám
    phieukham_list = relationship("PhieuKham", back_populates="bacsi")
    # - Đơn thuốc
    donthuoc_list = relationship("DonThuoc", back_populates="bacsi")
