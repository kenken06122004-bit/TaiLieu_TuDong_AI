class TaiLieuAI:
    """Lớp đại diện cho một tài liệu AI được sinh tự động."""

    def __init__(self, ten_tai_lieu, noi_dung):
        self.ten_tai_lieu = ten_tai_lieu
        self.noi_dung = noi_dung

    def hien_thi(self):
        """In ra thông tin của tài liệu."""
        print(f"Tên tài liệu: {self.ten_tai_lieu}")
        print(f"Nội dung: {self.noi_dung}")