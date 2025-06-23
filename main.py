from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from zoneinfo import ZoneInfo
import os

app = Flask(__name__)
folder_exe = os.path.dirname(os.path.abspath(__file__))
folder_hasil = os.path.join(folder_exe, "hasil")

# Buat folder hasil jika belum ada
if not os.path.exists(folder_hasil):
    os.makedirs(folder_hasil)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nomer1 = request.form["nomer1"]
        nomer2 = request.form["nomer2"]

        path_gambar = os.path.join(folder_exe, "gambar.jpeg")
        font_path = os.path.join(folder_exe, "calibri.ttf")

        font = ImageFont.truetype(font_path, 70)
        font1 = ImageFont.truetype(font_path, 50)

        gambar = Image.open(path_gambar)
        draw = ImageDraw.Draw(gambar)

        warna_teks = (0, 0, 0)
        waktu = datetime.now(ZoneInfo("Asia/Makassar"))  # GMT+9
        timestamp = waktu.strftime("%H:%M")
        tanggal = waktu.strftime("%d-%m-%Y")

        draw.text((365, 140), tanggal, font=font1, fill=warna_teks)
        draw.text((415, 210), timestamp, font=font1, fill=warna_teks)
        draw.text((670, 240), nomer1, font=font, fill=warna_teks)
        draw.text((755, 340), nomer2, font=font, fill=warna_teks)

        # Simpan ke folder hasil/
        nama_file = f"{nomer1}.{nomer2}.jpg"
        output_path = os.path.join(folder_hasil, nama_file)
        gambar.save(output_path)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")


# Untuk Replit
app.run(host='0.0.0.0', port=81)
