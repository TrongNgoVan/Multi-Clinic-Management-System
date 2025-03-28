class PhongChucNang:
    def __init__(self, id, chucNang, moTa):
        self.id = id
        self.chucNang = chucNang
        self.moTa = moTa

    def to_dict(self):
        """Chuyển object thành dictionary để dễ dàng trả về JSON"""
        return {
            "id": self.id,
            "chucNang": self.chucNang,
            "moTa": self.moTa
        }
