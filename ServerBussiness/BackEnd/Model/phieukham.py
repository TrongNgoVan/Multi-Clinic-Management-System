from BackEnd.Model.bacsi import BacSi
from BackEnd.Model.benhnhan import BenhNhan

class PhieuKham:
    def __init__(self, id, trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, tienkham, BenhNhan, BacSi):
        # Fix lại thuộc tính chuandoan ==> chandoan. Lỡ để thuộc tính chandoan trong database rồi :v
        self.id = id
        self.trieuchung = trieuchung
        self.chandoan = chandoan
        self.thongsoxetnghiem = thongsoxetnghiem
        self.anhxetnghiem = anhxetnghiem
        self.ngaykham = ngaykham
        self.BenhNhan = BenhNhan
        self.BacSi = BacSi
        self.tienkham = tienkham

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "trieuchung": self.trieuchung,
            "chandoan": self.chandoan,
            "thongsoxetnghiem": self.thongsoxetnghiem,
            "anhxetnghiem": self.anhxetnghiem,
            "ngaykham": str(self.ngaykham) if self.ngaykham else None,
            "benhnhan": self.BenhNhan.to_dict() if self.BenhNhan else None,
            "bacsi": self.BacSi.to_dict() if self.BacSi else None,
            "tienkham": self.tienkham
        }
