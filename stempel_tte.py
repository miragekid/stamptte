import sys
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import tkinter as tk
import tkinter.messagebox as messagebox

# Tentukan folder kerja sesuai environment (exe atau script)
if getattr(sys, 'frozen', False):
    folder_exe = os.path.dirname(sys.executable)
else:
    folder_exe = os.path.dirname(os.path.abspath(__file__))

path_gambar = os.path.join(folder_exe, "gambar.jpg")

# Load font sekali saja
font_path = os.path.join(folder_exe, "arial.ttf")  # Pastikan font ada di folder exe juga
font_size = 70
font_size1 = 50
font = ImageFont.truetype(font_path, font_size)
font1 = ImageFont.truetype(font_path, font_size1)

def ambil_data():
    nomer1 = entry_nomer1.get()
    nomer2 = entry_nomer2.get()
    
    gambar = Image.open(path_gambar)
    draw = ImageDraw.Draw(gambar)
    
    warna_teks = (0, 0, 0)  # Hitam

    timestamp = datetime.now().strftime("%H:%M")
    tanggal = datetime.now().strftime("%d-%m-%Y")

    # Cetak nomer1
    draw.text((670, 230), nomer1, font=font, fill=warna_teks)
    # Cetak nomer2
    draw.text((755, 330), nomer2, font=font, fill=warna_teks)
    # Cetak Waktu
    draw.text((400, 135), timestamp, font=font1, fill=warna_teks)
    # Cetak Tanggal
    draw.text((340, 205), tanggal, font=font1, fill=warna_teks)
    
    # Buat folder hasil jika belum ada
    folder_hasil = os.path.join(folder_exe, "hasil")
    if not os.path.exists(folder_hasil):
        os.makedirs(folder_hasil)
    
    # Simpan file di folder hasil
    nama_file = f"{nomer1}.{nomer2}.jpg"
    path_simpan = os.path.join(folder_hasil, nama_file)
    gambar.save(path_simpan)
    
    messagebox.showinfo("Sukses", f"Gambar {nama_file} berhasil disimpan di folder 'hasil'!")

def clear_input():
    entry_nomer1.delete(0, tk.END)
    entry_nomer2.delete(0, tk.END)
    entry_nomer1.focus_set()  # Fokus ke entry_nomer1

root = tk.Tk()
root.title("Stempel TTE")

lebar_layar = root.winfo_screenwidth()
tinggi_layar = root.winfo_screenheight()

lebar_form = 500
tinggi_form = 150 

x = (lebar_layar // 2) - (lebar_form // 2)
y = (tinggi_layar // 2) - (tinggi_form // 2)

root.geometry(f"{lebar_form}x{tinggi_form}+{x}+{y}")

# Frame untuk Nomor 1
frame_nomer1 = tk.Frame(root)
frame_nomer1.pack(pady=(20,5), fill='x', padx=10)

label_nomer1 = tk.Label(frame_nomer1, text="Nomor 1:", width=5, anchor='w', padx=20)
label_nomer1.pack(side=tk.LEFT)

entry_nomer1 = tk.Entry(frame_nomer1)
entry_nomer1.pack(side=tk.LEFT, fill='x', expand=True, padx=20)
entry_nomer1.focus_set()

# Frame untuk Nomor 2
frame_nomer2 = tk.Frame(root)
frame_nomer2.pack(pady=5, fill='x', padx=10)

label_nomer2 = tk.Label(frame_nomer2, text="Nomor 2:", width=5, anchor='w', padx=20)
label_nomer2.pack(side=tk.LEFT)

entry_nomer2 = tk.Entry(frame_nomer2)
entry_nomer2.pack(side=tk.LEFT, fill='x', expand=True, padx=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Cetak", width=10, command=ambil_data)
submit_button.pack(side=tk.LEFT, padx=(0, 5))

clear_button = tk.Button(button_frame, text="Clear", width=10, command=clear_input)
clear_button.pack(side=tk.LEFT, padx=(5, 0))

root.mainloop()