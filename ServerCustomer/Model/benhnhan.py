class BenhNhan:
    def __init__(self, id, ten, sdt, quequan, cccd, dob, img, username, password):
        self.id = id
        self.ten = ten
        self.sdt = sdt
        self.quequan = quequan
        self.cccd = cccd
        self.dob = dob
        self.img = img
        self.username = username
        self.password = password

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "ten": self.ten,
            "sdt": self.sdt,
            "quequan": self.quequan,
            "cccd": self.cccd,
            "dob": str(self.dob),
            "img": self.img,
            "username": self.username,
            "password": self.password
        }

    
