# Langkah 1: Instal pustaka qrcode jika belum terinstal
# pip install qrcode[pil]

# Langkah 2: Impor pustaka yang diperlukan
import qrcode

# Langkah 3: Minta pengguna untuk memasukkan data yang ingin disimpan dalam QR Code
link = input("Masukkan data yang ingin disimpan dalam QR Code : ")

# Langkah 4: Buat objek QRCode
qr = qrcode.QRCode(
    version=1,  # Ukuran QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan
    box_size=10,  # Ukuran setiap kotak
    border=4,  # Lebar border
)

# Langkah 5: Tambahkan data ke QR Code
qr.add_data(link)
qr.make(fit=True)

# Langkah 6: Buat gambar QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Langkah 7: Simpan gambar QR Code ke file
img.save("qr_code_example.png")