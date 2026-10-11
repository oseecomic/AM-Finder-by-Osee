🎀 AM Finder by Osee

Alight Motion Preset Finder for Termux

Tool Python sederhana untuk mencari link preset Alight Motion melalui link video TikTok menggunakan API Preset Finder.

✨ Fitur

- Mencari preset dari link TikTok
- Tampilan terminal berwarna
- Menu pencarian sederhana
- Berjalan di Termux dengan Python
- Tidak memerlukan website atau HTML

📱 Persyaratan

- Android
- Termux
- Koneksi internet
- Python 3
- API Preset Finder yang masih berfungsi

📥 Cara Instalasi

1. Instal Termux

Unduh Termux dari sumber resminya:

https://github.com/termux/termux-app

2. Perbarui paket Termux

pkg update && pkg upgrade -y

3. Instal Git dan Python

pkg install git python -y

4. Unduh repository

git clone https://github.com/oseecomic/AM-Finder-by-Osee.git

5. Masuk ke folder proyek

cd AM-Finder-by-Osee

6. Instal library yang diperlukan

pip install requests

🚀 Cara Menjalankan

Jalankan:

python amfinder.py

Pilih menu pencarian, masukkan link video TikTok yang valid, lalu tunggu hasil dari API.

🔄 Cara Menjalankan Lagi

Setiap kali membuka Termux:

cd AM-Finder-by-Osee
python amfinder.py

⚠️ Catatan

- Pastikan nama file program adalah "amfinder.py".
- Tool ini memerlukan koneksi internet.
- Hasil pencarian bergantung pada ketersediaan dan format respons API.
- Link preset belum tentu ditemukan untuk setiap video TikTok.
- Gunakan API sesuai ketentuan penyedianya.

👨‍💻 Developer

Osee

GitHub: https://github.com/oseecomic
