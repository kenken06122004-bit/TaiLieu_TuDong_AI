import os

def kiem_tra_tai_lieu():
    """Kiểm tra các file trong thư mục 'tai_lieu' có lỗi hay không."""
    loi = 0
    thu_muc = "tai_lieu"

    for tep in os.listdir(thu_muc):
        if tep.endswith(".md"):
            duong_dan = os.path.join(thu_muc, tep)
            with open(duong_dan, "r", encoding="utf-8") as f:
                data = f.read()
                if len(data.strip()) < 50:  # File quá ngắn thì báo lỗi
                    print(f"⚠️ File {tep} có thể bị thiếu nội dung.")
                    loi += 1

    if loi == 0:
        print("KHÔNG PHÁT HIỆN LỖI TRONG TÀI LIỆU.")
    else:
        print(f"PHÁT HIỆN {loi} FILE CẦN KIỂM TRA LẠI.")

if __name__ == "__main__":
    kiem_tra_tai_lieu()