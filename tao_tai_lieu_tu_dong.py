import os

def tao_tai_lieu_tu_dong():
    thu_muc_nguon = "ma_nguon"
    noi_dung = "# TÀI LIỆU TỰ ĐỘNG SINH BỞI AI\n\n"

    for goc, thu_muc, tep_tin in os.walk(thu_muc_nguon):
        for ten_tep in tep_tin:
            if ten_tep.endswith(".py"):
                duong_dan_tap_tin = os.path.join(goc, ten_tep)
                with open(duong_dan_tap_tin, 'r', encoding='utf-8') as f:
                    code = f.read()
                noi_dung += f"## File: {ten_tep}\n<pre>{code}</pre>\n\n"

    os.makedirs("tai_lieu", exist_ok=True)

    # Tạo file index.html trực tiếp ở root để GitHub Pages hiển thị
    html = f"""
    <html>
    <head><meta charset="utf-8"><title>Tài liệu AI</title></head>
    <body>
    <h1>TÀI LIỆU TỰ ĐỘNG SINH BỞI AI</h1>
    {noi_dung}
    </body>
    </html>
    """

    with open("tai_lieu/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("ĐÃ TẠO TÀI LIỆU index.html trong thư mục 'tai_lieu/'")

if __name__ == "__main__":
    tao_tai_lieu_tu_dong()
