POSTTEST 2

- Menambahkan relasi Association antara kelas PemesananJadwal dan Lapangan, relasi Aggregation pada kelas PengelolaGOR yang menampung daftar objek Lapangan, serta relasi Composition di mana objek StrukPembayaran dibuat dan terikat langsung di dalam kelas PemesananJadwal.

- Membuat superclass Lapangan beserta tiga subclass yaitu LapanganMatras, LapanganVinyl, dan LapanganParquet, di mana setiap subclass memanggil konstruktor induk menggunakan super().__init__().

- Menambahkan atribut unik pada tiap subclass (seperti jenis_interlock pada matras, ketebalan pada vinyl, dan tipe_kayu pada parquet) serta meng-override metode hitung_total_sewa() dan tampilkan_info() untuk menyesuaikan kalkulasi harga dan rincian tampilan.

- Menggunakan atribut protected (_harga) pada superclass agar bisa diakses langsung oleh subclass, serta atribut private (__kontak_pengelola) untuk data eksklusif superclass.

- Memperbarui metode cetak_detail() pada kelas StrukPembayaran dengan format :^51 untuk meratakan judul tepat di tengah border, serta format :<16 dan :<32 agar posisi titik dua dan garis border kanan tersusun rapi.