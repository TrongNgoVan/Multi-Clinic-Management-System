from Model.bacsi import BacSi
from Model.benhnhan import BenhNhan

class LichHen:
    def __init__(self, id,  Bacsi, BenhNhan, ghichu, thoigianhen, trangthai):
        self.id = id
        self.Bacsi = Bacsi
        self.BenhNhan = BenhNhan
        self.ghichu = ghichu
        self.thoigianhen = thoigianhen
        self.trangthai = trangthai
    
    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "bacsi": self.Bacsi.to_dict() if self.Bacsi else None,
            "benhnhan": self.BenhNhan.to_dict() if self.BenhNhan else None,
            "ghichu": str(self.ghichu) if self.ghichu else None,
            "thoigianhen": str(self.thoigianhen) if self.thoigianhen else None,
            "trangthai": str(self.trangthai) if self.trangthai else None
        }