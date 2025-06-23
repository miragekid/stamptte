from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

app = Flask(__name__)

# Tentukan folder kerja
folder = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nomer1 = request.form['nomer1']
        nomer2 = request.form['nomer2']

        path_gambar = os.path.join(folder, 'gambar.jpeg')
        font_path = os.path.join(folder, 'calibri.ttf')
        font_size = 70
        font_size1 = 50

        font = ImageFont.truetype(font_path, font_size)
        font1 = ImageFont.truetype(font_path, font_size1)

        gambar = Image.open(path_gambar)
        draw = ImageDraw.Draw(gambar)

        warna_teks = (0, 0, 0)
        timestamp = datetime.now().strftime("%H:%M")
        tanggal = datetime.now().strftime("%d-%m-%Y")

        # Tulis teks ke gambar
        draw.text((365, 140), tanggal, font=font1, fill=warna_teks)
        draw.text((415, 210), timestamp, font=font1, fill=warna_teks)
        draw.text((670, 240), nomer1, font=font, fill=warna_teks)
        draw.text((755, 340), nomer2, font=font, fill=warna_teks)

        # Simpan hasil ke file temporer
        hasil_path = os.path.join(folder, f"{nomer1}.{nomer2}.jpg")
        gambar.save(hasil_path)

        return send_file(hasil_path, as_attachment=True)

    return render_template('index.html')
