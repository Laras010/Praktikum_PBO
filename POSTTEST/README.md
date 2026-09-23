Program ini dirancang khusus untuk mengelola operasional persewaan lapangan di GOR Badminton All Round, mencakup pendataan lapangan, 
pembuatan pesanan, penambahan fasilitas, hingga pencetakan struk dan rekapitulasi pemasukan.

- Class & Object
   -`Lapangan` Kelas yang merepresentasikan data fisik lapangan dan pemesan.
   -`PemesananJadwal` Kelas yang menangani alur transaksi pemesanan jadwal sewa beserta fasilitas tambahan.
   -`PengelolaGOR` Kelas manajerial yang berfungsi menyimpan dan mengorganisasi koleksi objek lapangan serta pesanan.
   -Instansiasi Objek Pembuatan berbagai objek seperti `lap1`, `lap2`, `p1`, dan `p2` dalam bagian driver code

- Atribut & Method
   -Atribut Kelas itu Atribut bersama yang dimiliki seluruh kelas, meliputi `jumlah_lapangan`, `nama_gor`, `jam_operasional`, dan `kontak_pengelola`.
   -Instance Method Fungsi yang beroperasi pada tingkat objek, seperti `hitung_total_sewa()`, `tampilkan_info()`, `tambah_fasilitas()`, `cetak_struk()`, dan `rekap_pemasukan()`.
   - Static Method Method `validasi_durasi()` untuk mengecek apakah durasi sewa yang diinput berada dalam rentang valid (1–8 jam).
   -Class Method adalah Method `ubah_jam_operasional()` untuk memperbarui atribut kelas `jam_operasional`.

- Encapsulation & Property
   -Private Attribute ini adalah Atribut `__harga` pada kelas `Lapangan` diubah menjadi *private* agar tidak dapat diakses atau diubah langsung secara tidak sah.
   -Getter (`@property`) untuk membaca nilai atribut `__harga` secara aman.
   -lalu Getter (`@property`) ini memperbarui nilai `__harga` dengan menyertakan kontrol validasi agar input harga harus berupa angka positif.

-Cara Menjalankan Program
    -Buka terminal atau Command Prompt di folder tempat file program disimpan.
    -Jalankan perintah berikut:
   ```bash
   python PT1_2509106010_ZihniLarasati.py