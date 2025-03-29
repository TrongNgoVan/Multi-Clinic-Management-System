class Thuoc:
    def __init__(self, id, ten, mota, nsx, hsd, dongia, img):
        self.id = id
        self.ten = ten
        self.mota = mota
        self.nsx = nsx
        self.hsd = hsd
        self.dongia = dongia
        self.img = img

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "ten": self.ten,
            "mota": self.mota,
            "nsx": str(self.nsx) if self.nsx else None,
            "hsd": str(self.hsd) if self.hsd else None,
            "dongia": self.dongia,
            "img": str(self.img) if self.img else None
        }
