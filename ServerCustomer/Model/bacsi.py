class BacSi:
    def __init__(self, id, ten, dob, chuyenmon, hocvan, kinhnghiem, img, phongID, username, password):
        self.id = id
        self.ten = ten
        self.dob = dob
        self.chuyenmon = chuyenmon
        self.hocvan = hocvan
        self.kinhnghiem = kinhnghiem
        self.img = img
        self.phongID = phongID
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
            "phongID": self.phongID,
            "username": self.username,
            "password": self.password
        }
