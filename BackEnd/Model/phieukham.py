class PhieuKham:
    def __init__(self, id, trieuchung, chuandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhan_id, bacsi_id, tienkham):
        self.id = id
        self.trieuchung = trieuchung
        self.chuandoan = chuandoan
        self.thongsoxetnghiem = thongsoxetnghiem
        self.anhxetnghiem = anhxetnghiem
        self.ngaykham = ngaykham
        self.benhnhan_id = benhnhan_id
        self.bacsi_id = bacsi_id
        self.tienkham = tienkham

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "trieuchung": self.trieuchung,
            "chuandoan": self.chuandoan,
            "thongsoxetnghiem": self.thongsoxetnghiem,
            "anhxetnghiem": self.anhxetnghiem,
            "ngaykham": str(self.ngaykham) if self.ngaykham else None,
            "benhnhan_id": self.benhnhan_id,
            "bacsi_id": self.bacsi_id,
            "tienkham": self.tienkham
        }
