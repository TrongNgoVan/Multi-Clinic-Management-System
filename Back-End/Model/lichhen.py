from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class LichHen(Base):
    __tablename__ = "lichhen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"), nullable=True)
    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"), nullable=True)
    thoigianhen = Column(DateTime, nullable=True)  # tuỳ chỉnh theo nhu cầu (NOT NULL hoặc DEFAULT NULL)

    # Quan hệ
    bacsi = relationship("BacSi", back_populates="lichhen_list")
    benhnhan = relationship("BenhNhan", back_populates="lichhen_list")
