class LichHen:
    def __init__(self, id, bacsi_id, benhnhan_id, thoigianhen):
        self.id = id
        self.bacsi_id = bacsi_id
        self.benhnhan_id = benhnhan_id
        self.thoigianhen = thoigianhen

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "bacsi_id": self.bacsi_id,
            "benhnhan_id": self.benhnhan_id,
            "thoigianhen": str(self.thoigianhen) if self.thoigianhen else None
        }
