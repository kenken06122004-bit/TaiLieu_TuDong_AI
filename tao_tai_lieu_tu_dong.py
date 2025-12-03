import os  # Dùng để thao tác với thư mục, file

def tao_tai_lieu_tu_dong():
    """Hàm sinh tài liệu tự động từ mã nguồn trong thư mục 'ma_nguon'."""
    thu_muc_nguon = "ma_nguon"                      # Đường dẫn mã nguồn
    noi_dung = "# TÀI LIỆU TỰ ĐỘNG SINH BỞI AI\n\n"

    # Duyệt toàn bộ file trong thư mục ma_nguon
    for goc, thu_muc, tep_tin in os.walk(thu_muc_nguon):
        for ten_tep in tep_tin:
            if ten_tep.endswith(".py"):              # Chỉ lấy file .py
                duong_dan_tap_tin = os.path.join(goc, ten_tep)
                with open(duong_dan_tap_tin, 'r', encoding='utf-8') as f:
                    code = f.read()                  # Đọc nội dung file
                # Ghi nội dung vào tài liệu Markdown
                noi_dung += f"## File: {ten_tep}\n```python\n{code}\n```\n\n"

    # Tạo thư mục tai_lieu nếu chưa có
    os.makedirs("tai_lieu", exist_ok=True)
    # Ghi nội dung vào file tài liệu
    with open("tai_lieu/tai_lieu_tu_dong.md", "w", encoding="utf-8") as file:
        file.write(noi_dung)

    print("ĐÃ TẠO TÀI LIỆU TỰ ĐỘNG TRONG THƯ MỤC 'tai_lieu/'")

if __name__ == "__main__":
    tao_tai_lieu_tu_dong()