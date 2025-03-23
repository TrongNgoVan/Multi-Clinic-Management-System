class DonThuoc:
    def __init__(self, id, ngaymua, benhnhan_id, bacsi_id, tonggia, mota):
        self.id = id
        self.ngaymua = ngaymua
        self.benhnhan_id = benhnhan_id
        self.bacsi_id = bacsi_id
        self.tonggia = tonggia
        self.mota = mota

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "ngaymua": str(self.ngaymua),
            "benhnhan_id": self.benhnhan_id,
            "bacsi_id": self.bacsi_id,
            "tonggia": self.tonggia,
            "mota": self.mota
        }
