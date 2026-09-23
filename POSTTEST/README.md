Program ini dibuat untuk membantu pengelola GOR Badminton All Round dalam mengurus persewaan lapangan. 
Lewat program ini, pengelola bisa mencatat data lapangan, mengatur harga sewa, memproses pesanan dari customer, 
sampai melihat rekap total pemasukan secara otomatis.

- Kelas Utama Lapangan
Bagian ini fungsinya sebagai cetakan utama untuk semua jenis lapangan yang ada di GOR. Di sini disimpan informasi 
dasar seperti nama GOR, jam operasional, dan nomor kontak pengelola. Kelas ini punya aturan dasar yang wajib diikuti 
oleh jenis lapangan lainnya, seperti cara menghitung harga dan menampilkan informasi lapangan. Selain itu, harga sewa 
di kelas ini dilindungi pakai fitur khusus (enkapsulasi) supaya nilainya nggak bisa diubah sembarangan dan harus bernilai 
positif. Ada juga fitur pengecekan otomatis untuk memastikan durasi sewa yang diinput customer berada di rentang 1 sampai 8 jam.

- Jenis Lapangan
Dua kelas ini adalah turunan dari kelas utama lapangan di atas. Masing-masing punya cara hitung harga yang beda sesuai 
dengan bahan lapangannya. Untuk lapangan matras, ada pilihan jenis bahan (seperti Interlock) dan ada biaya tambahan kalau 
disewa pada sesi sore atau malam. Sedangkan untuk lapangan vinyl, harganya dihitung berdasarkan ketebalan karpetnya (dalam mm) 
serta ada penyesuaian biaya sewa untuk sesi sore dan malam.

- Sistem Pemesanan
Kelas ini bertugas mengurus semua transaksi yang masuk. Setiap kali ada yang pesan, sistem bakal langsung mencatat 
nama pemesan, durasi sewa, pilihan sesi, serta opsi sewa alat tambahan seperti raket atau beli shuttlecock. 
Di bagian ini juga ada fitur untuk mengubah status pembayaran (Belum lunas, Lunas, atau Dibatalkan), 
cetak struk pembayaran yang rapi, rekap total uang masuk dari pesanan yang sudah lunas, dan pencarian riwayat transaksi 
berdasarkan ID pesanan.

- Cara Menjalankan dan Menguji Program
1. Pastikan komputer kamu sudah terinstall Python.
2. Buka terminal atau Command Prompt, lalu masuk ke folder tempat kamu menyimpan file kodenya.
3. Jalankan programnya dengan mengetik perintah `python main.py`.
4. Saat berjalan, program bakal menampilkan informasi GOR dan langsung mencoba membuat 4 pesanan contoh dengan pilihan 
lapangan serta opsi sewa raket/kok yang berbeda-beda.
5. Setelah itu, sistem bakal mengubah status pembayaran beberapa pesanan menjadi "Lunas", menampilkan rincian lapangan, 
dan mencetak struk belanjaan tiap customer.
6. Di bagian akhir, program bakal mencoba fitur ubah jam buka GOR, mengubah harga sewa lapangan, menampilkan total 
rekapitulasi uang masuk yang sudah lunas, dan mencari data transaksi lewat ID "B02".