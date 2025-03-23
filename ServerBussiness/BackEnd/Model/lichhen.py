from BackEnd.Model.bacsi import BacSi
from BackEnd.Model.benhnhan import BenhNhan

class LichHen:
    def __init__(self, id, thoigianhen, Bacsi, BenhNhan):
        self.id = id
        self.Bacsi = Bacsi
        self.BenhNhan = BenhNhan
        self.thoigianhen = thoigianhen
    
    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "bacsi": self.Bacsi.to_dict() if self.Bacsi else None,
            "benhnhan": self.BenhNhan.to_dict() if self.BenhNhan else None,
            "thoigianhen": str(self.thoigianhen) if self.thoigianhen else None
        }