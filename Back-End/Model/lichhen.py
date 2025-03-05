from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from DB.db_connection import Base

class LichHen(Base):
    __tablename__ = "lichhen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bacsi_id = Column(Integer, ForeignKey("bacsi.id"))
    benhnhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    thoigianhen = Column(DateTime, nullable=False)

    bacsi = relationship("BacSi", back_populates="lichhen_list")
    benhnhan = relationship("BenhNhan", back_populates="lichhen_list")
