class Lapangan:
    jumlah_lapangan = 0
    nama_gor = "GOR BADMINTON ALL ROUND"
    jam_operasional = "08.00 - 22.00 WITA"
    __kontak_pengelola = "0812-3456-7890"  

    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi):
        self.nama_customer = nama_customer
        self.jenis_lapangan = jenis_lapangan
        self.kode_lapangan = kode_lapangan
        self.lokasi = lokasi
        self._harga = 0  
        self.harga = harga
        Lapangan.jumlah_lapangan += 1

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            print(f"[ERROR] Gagal mengubah harga lapangan {self.kode_lapangan}! Harga sewa harus berupa angka positif.")
        else:
            self._harga = nilai_baru

    @staticmethod
    def validasi_durasi(durasi):
        if isinstance(durasi, int) and 1 <= durasi <= 8:
            return True
        return False

    @classmethod
    def get_kontak(cls):
        return cls.__kontak_pengelola

    @classmethod
    def ubah_jam_operasional(cls, jam_baru):
        if isinstance(jam_baru, str) and jam_baru.strip() != "":
            cls.jam_operasional = jam_baru
            print(f"[INFO] Jam operasional {cls.nama_gor} berhasil diubah menjadi: {cls.jam_operasional}")

    def hitung_total_sewa(self, durasi, sesi="pagi"):
        if not self.validasi_durasi(durasi):
            print(f"[ERROR] Durasi sewa {durasi} jam tidak valid (harus 1-8 jam).")
            return 0
        
        total = self.harga * durasi
        if sesi.lower() in ["sore", "malam"]:
            total += 10000 * durasi
        return total

    def tampilkan_info(self):
        print(f"| {self.kode_lapangan:<5} | {self.jenis_lapangan:<42} | {self.nama_customer:<10} | Rp {self.harga:>7,}/jam |")

class LapanganMatras(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, ketebalan_matras):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self.ketebalan_matras = ketebalan_matras 

    def hitung_total_sewa(self, durasi, sesi="pagi"):
        total = super().hitung_total_sewa(durasi, sesi)
        if durasi > 3:
            total -= 10000  
            print(f"[DISKON] Potongan Rp 10.000 diterapkan untuk lapangan matras {self.kode_lapangan}.")
        return total

    def tampilkan_info(self):
        detail_jenis = f"{self.jenis_lapangan} (Matras {self.ketebalan_matras})"
        print(f"| {self.kode_lapangan:<5} | {detail_jenis:<42} | {self.nama_customer:<10} | Rp {self.harga:>7,}/jam |")

class LapanganVinyl(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, jenis_karpet):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self.jenis_karpet = jenis_karpet 

    def hitung_total_sewa(self, durasi, sesi="pagi"):
        total = super().hitung_total_sewa(durasi, sesi)
        biaya_perawatan = 5000 * durasi
        total += biaya_perawatan
        return total

    def tampilkan_info(self):
        detail_jenis = f"{self.jenis_lapangan} (Vinyl {self.jenis_karpet})"
        print(f"| {self.kode_lapangan:<5} | {detail_jenis:<42} | {self.nama_customer:<10} | Rp {self.harga:>7,}/jam |")

class LapanganParquet(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, tipe_kayu):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self.tipe_kayu = tipe_kayu

    def hitung_total_sewa(self, durasi, sesi="pagi"):
        total = super().hitung_total_sewa(durasi, sesi)
        total += 15000 
        return total

    def tampilkan_info(self):
        detail_jenis = f"{self.jenis_lapangan} (Kayu {self.tipe_kayu})"
        print(f"| {self.kode_lapangan:<5} | {detail_jenis:<42} | {self.nama_customer:<10} | Rp {self.harga:>7,}/jam |")

class StrukPembayaran:
    def __init__(self, id_struk, total_bayar, status_pembayaran):
        self.id_struk = id_struk
        self.total_bayar = total_bayar
        self.status_pembayaran = status_pembayaran

    def cetak_detail(self, id_pesanan, nama_customer, detail_lapangan, sesi, durasi, sewa_raket, beli_cock):
        print("\n" + "="*45)
        print(f"| STRUK PEMESANAN - {Lapangan.nama_gor} |")
        print("="*45)
        print(f"No. Struk      : {self.id_struk}")
        print(f"ID Pesanan     : {id_pesanan}")
        print(f"Nama Customer  : {nama_customer}")
        print(f"Detail Lapangan: {detail_lapangan}")
        print(f"Sesi & Durasi  : {sesi.capitalize()} ({durasi} Jam)")
        print(f"Tambahan       : Raket ({'Ya' if sewa_raket else 'Tidak'}), Cock ({'Ya' if beli_cock else 'Tidak'})")
        print(f"Total Biaya    : Rp {self.total_bayar:,}")
        print(f"Status Bayar   : {self.status_pembayaran}")
        print("="*45 + "\n")

class PemesananJadwal:
    def __init__(self, id_pesanan, obyek_lapangan, durasi, sesi="pagi"):
        self.id_pesanan = id_pesanan
        self.lapangan = obyek_lapangan
        self.durasi = durasi
        self.sesi = sesi
        self.sewa_raket = False
        self.beli_shuttlecock = False
        self.status_pembayaran = "Belum Lunas"
        self.total_bayar = self.hitung_total_transaksi()
        self.struk = StrukPembayaran(f"STR-{id_pesanan}", self.total_bayar, self.status_pembayaran)

    def tambah_fasilitas(self, raket=False, shuttlecock=False):
        self.sewa_raket = raket
        self.beli_shuttlecock = shuttlecock
        self.total_bayar = self.hitung_total_transaksi()
        self.struk.total_bayar = self.total_bayar

    def hitung_total_transaksi(self):
        total = self.lapangan.hitung_total_sewa(self.durasi, self.sesi)
        if self.sewa_raket:
            total += 25000 * self.durasi
        if self.beli_shuttlecock:
            total += 20000
        return total

    def update_status(self, status):
        status_valid = ["Belum Lunas", "Lunas", "Dibatalkan"]
        if status in status_valid:
            self.status_pembayaran = status
            self.struk.status_pembayaran = status
            print(f"[INFO] Status pesanan {self.id_pesanan} berhasil diubah menjadi: {self.status_pembayaran}")
        else:
            print("[ERROR] Status pembayaran tidak valid!")

    def cetak_struk(self):
        detail_lap = f"{self.lapangan.jenis_lapangan} ({self.lapangan.kode_lapangan})"
        self.struk.cetak_detail(
            self.id_pesanan, 
            self.lapangan.nama_customer, 
            detail_lap, 
            self.sesi, 
            self.durasi, 
            self.sewa_raket, 
            self.beli_shuttlecock
        )

class PengelolaGOR:
    def __init__(self, nama_pengelola):
        self.nama_pengelola = nama_pengelola
        self.daftar_lapangan = []
        self.daftar_pesanan = []

    def tambah_lapangan(self, lapangan_obj):
        self.daftar_lapangan.append(lapangan_obj)
        print(f"[BERHASIL] Lapangan {lapangan_obj.kode_lapangan} berhasil ditambahkan.")

    def tampilkan_semua_lapangan(self):
        garis = "=" * 85
        print(garis)
        print(f"|DAFTAR LAPANGAN TERSEDIA (DIKELOLA OLEH {self.nama_pengelola.upper()}):".ljust(84) +"|")
        print(garis)
        print(f"| {'Kode':<5} | {'Jenis Lapangan':<42} | {'Pemesan':<10} | {'Harga Sewa':<14} |")
        print(garis)
        if not self.daftar_lapangan:
            print("| Belum ada data lapangan.".ljust(84) + "|")
        else:
            for lap in self.daftar_lapangan:
                lap.tampilkan_info()
        print(garis + "\n")

    def cari_lapangan(self, kode):
        for lap in self.daftar_lapangan:
            if lap.kode_lapangan.lower() == kode.lower():
                return lap
        return None

    def buat_pesanan(self, id_pesanan, kode_lapangan, durasi, sesi="pagi"):
        lapangan = self.cari_lapangan(kode_lapangan)
        if lapangan:
            pesanan_baru = PemesananJadwal(id_pesanan, lapangan, durasi, sesi)
            self.daftar_pesanan.append(pesanan_baru)
            print(f"[BERHASIL] Pesanan {id_pesanan} berhasil dibuat!")
            return pesanan_baru
        else:
            print(f"[ERROR] Lapangan dengan kode {kode_lapangan} tidak ditemukan!")
            return None

    def rekap_pemasukan(self):
        total_pemasukan = 0
        print("=============================")
        print("| REKAP PEMASUKAN SEMENTARA |")
        print("=============================")
        for pesanan in self.daftar_pesanan:
            if pesanan.status_pembayaran == "Lunas":
                total_pemasukan += pesanan.total_bayar
                print(f"- {pesanan.id_pesanan} ({pesanan.lapangan.nama_customer}): Rp {pesanan.total_bayar:,}")
        print(f"TOTAL PEMASUKAN LUNAS: Rp {total_pemasukan:,}\n")

if __name__ == "__main__":
    print(f"=== SYSTEM {Lapangan.nama_gor} ===")
    print(f"Jam Operasional : {Lapangan.jam_operasional}")
    print(f"Kontak Admin    : {Lapangan.get_kontak()}\n")

    gor_system = PengelolaGOR("Larasati")

    lap1 = LapanganMatras("Yayas", "Matras Interlock Standard", "L-01", 50000, "Sektor A", "10mm")
    lap2 = LapanganVinyl("Zihni", "Vinyl Karpet Pro 5mm", "L-02", 65000, "Sektor B", "Standard BWF")
    lap3 = LapanganParquet("Laras", "Parquet Kayu Premium", "L-03", 80000, "VIP Sektor", "Jati Mahoni")

    gor_system.tambah_lapangan(lap1)
    gor_system.tambah_lapangan(lap2)
    gor_system.tambah_lapangan(lap3)
    gor_system.tampilkan_semua_lapangan()

    print("=======================")
    print("| MEMPROSES PEMESANAN |")
    print("=======================")

    p1 = gor_system.buat_pesanan("ORD-001", "L-01", durasi=4, sesi="sore")
    if p1:
        p1.tambah_fasilitas(raket=True, shuttlecock=True)
        p1.cetak_struk()

    p2 = gor_system.buat_pesanan("ORD-002", "L-02", durasi=3, sesi="malam")
    if p2:
        p2.cetak_struk()

    p3 = gor_system.buat_pesanan("ORD-003", "L-03", durasi=2, sesi="pagi")
    if p3:
        p3.tambah_fasilitas(raket=False, shuttlecock=True)
        p3.cetak_struk()

    print("===========================")
    print("| PROSES PEMBAYARAN & REKAP |")
    print("===========================")
    if p1:
        p1.update_status("Lunas")
    if p3:
        p3.update_status("Lunas")
    gor_system.rekap_pemasukan()

    print("====================================")
    print("|PENGUJIAN ENCAPSULATION & PROPERTY|")
    print("====================================")
    print(f"Harga awal L-01: Rp {lap1.harga:,}")
    lap1.harga = 55000
    print(f"Harga baru L-01: Rp {lap1.harga:,}")
    lap1.harga = -20000

    print("===================================")
    print("| PENGUJIAN CLASS & STATIC METHOD |")
    print("===================================")
    print(f"Validasi durasi 5 jam : {Lapangan.validasi_durasi(5)}")
    print(f"Validasi durasi 10 jam: {Lapangan.validasi_durasi(10)}")
    Lapangan.ubah_jam_operasional("07.00 - 23.00 WITA")