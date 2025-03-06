class ChiTietDonThuoc:
    def __init__(self, id, donthuoc_id, thuoc_id, soluong, gia):
        self.id = id
        self.donthuoc_id = donthuoc_id
        self.thuoc_id = thuoc_id
        self.soluong = soluong
        self.gia = gia

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "donthuoc_id": self.donthuoc_id,
            "thuoc_id": self.thuoc_id,
            "soluong": self.soluong,
            "gia": self.gia
        }
