class BacSi:
    def __init__(self, id, ten, dob, chuyenmon, hocvan, kinhnghiem, img, phong_id, username, password):
        self.id = id
        self.ten = ten
        self.dob = dob
        self.chuyenmon = chuyenmon
        self.hocvan = hocvan
        self.kinhnghiem = kinhnghiem
        self.img = img
        self.phong_id = phong_id
        self.username = username
        self.password = password

    def to_dict(self):
        """Chuyển object thành dictionary (dễ dàng trả về JSON nếu cần)"""
        return {
            "id": self.id,
            "ten": self.ten,
            "dob": str(self.dob),
            "chuyenmon": self.chuyenmon,
            "hocvan": self.hocvan,
            "kinhnghiem": self.kinhnghiem,
            "img": self.img,
            "phong_id": self.phong_id,
            "username": self.username,
            "password": self.password
        }
