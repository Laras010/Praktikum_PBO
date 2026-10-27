from abc import ABC, abstractmethod

class Lapangan(ABC):
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
        return isinstance(durasi, int) and 1 <= durasi <= 8

    @classmethod
    def get_kontak(cls):
        return cls.__kontak_pengelola

    @classmethod
    def ubah_jam_operasional(cls, jam_baru):
        if isinstance(jam_baru, str) and jam_baru.strip() != "":
            cls.jam_operasional = jam_baru
            print(f"[INFO] Jam operasional {cls.nama_gor} berhasil diubah menjadi: {cls.jam_operasional}")

    @abstractmethod
    def hitung_biaya_tambahan(self, durasi):
        """Biaya/diskon khusus tiap jenis lapangan (bisa negatif jika diskon)."""
        pass

    @abstractmethod
    def deskripsi_jenis(self):
        """Teks deskripsi jenis lapangan beserta atribut uniknya."""
        pass

    def hitung_total_sewa(self, durasi, sesi="pagi"):
        """Alur hitung yang sama untuk semua lapangan (template method)."""
        if not self.validasi_durasi(durasi):
            print(f"[ERROR] Durasi sewa {durasi} jam tidak valid (harus 1-8 jam).")
            return 0

        total = self.harga * durasi
        if sesi.lower() in ["sore", "malam"]:
            total += 10000 * durasi
        total += self.hitung_biaya_tambahan(durasi)  
        return total

    def tampilkan_info(self):
        print(f"| {self.kode_lapangan:<5} | {self.deskripsi_jenis():<42} | {self.nama_customer:<10} | Rp {self.harga:>7,}/jam |")

    def __str__(self):
        return f"{self.kode_lapangan} - {self.deskripsi_jenis()} (Rp {self.harga:,}/jam)"

    def __lt__(self, other):
        return self.harga < other.harga

    def __eq__(self, other):
        return self.kode_lapangan == other.kode_lapangan

    def __hash__(self):
        return hash(self.kode_lapangan)

class LapanganMatras(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, ketebalan_matras):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self._ketebalan_matras = ketebalan_matras  

    def hitung_biaya_tambahan(self, durasi):
        return -10000 if durasi > 3 else 0

    def deskripsi_jenis(self):
        return f"{self.jenis_lapangan} (Matras {self._ketebalan_matras})"


class LapanganVinyl(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, jenis_karpet):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self._jenis_karpet = jenis_karpet  

    def hitung_biaya_tambahan(self, durasi):
        return 5000 * durasi

    def deskripsi_jenis(self):
        return f"{self.jenis_lapangan} (Vinyl {self._jenis_karpet})"


class LapanganParquet(Lapangan):
    def __init__(self, nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi, tipe_kayu):
        super().__init__(nama_customer, jenis_lapangan, kode_lapangan, harga, lokasi)
        self._tipe_kayu = tipe_kayu 

    def hitung_biaya_tambahan(self, durasi):
        return 15000

    def deskripsi_jenis(self):
        return f"{self.jenis_lapangan} (Kayu {self._tipe_kayu})"

class StrukPembayaran:
    def __init__(self, id_struk, total_bayar, status_pembayaran):
        self.id_struk = id_struk
        self.total_bayar = total_bayar
        self.status_pembayaran = status_pembayaran

    def cetak_detail(self, id_pesanan, nama_customer, detail_lapangan, sesi, durasi, sewa_raket, beli_cock):
        print("\n" + "=" * 45)
        print(f"| STRUK PEMESANAN - {Lapangan.nama_gor} |")
        print("=" * 45)
        print(f"No. Struk      : {self.id_struk}")
        print(f"ID Pesanan     : {id_pesanan}")
        print(f"Nama Customer  : {nama_customer}")
        print(f"Detail Lapangan: {detail_lapangan}")
        print(f"Sesi & Durasi  : {sesi.capitalize()} ({durasi} Jam)")
        print(f"Tambahan       : Raket ({'Ya' if sewa_raket else 'Tidak'}), Cock ({'Ya' if beli_cock else 'Tidak'})")
        print(f"Total Biaya    : Rp {self.total_bayar:,}")
        print(f"Status Bayar   : {self.status_pembayaran}")
        print("=" * 45 + "\n")


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
            self.beli_shuttlecock,
        )

    def __add__(self, other):
        return self.total_bayar + other.total_bayar

    def __str__(self):
        return f"Pesanan {self.id_pesanan} | {self.lapangan.kode_lapangan} | Rp {self.total_bayar:,} | {self.status_pembayaran}"

class NotifWhatsApp:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, pesan):
        print(f"  [WHATSAPP -> {self.nomor}] {pesan}")


class NotifSMS:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, pesan):
        print(f"  [SMS -> {self.nomor}] {pesan}")


class NotifEmail:
    def __init__(self, alamat):
        self.alamat = alamat

    def kirim(self, pesan):
        print(f"  [EMAIL -> {self.alamat}] {pesan}")


def kirim_notifikasi(daftar_kanal, pesan):
    """Tidak peduli tipe kanalnya, asal punya method kirim()."""
    for kanal in daftar_kanal:
        kanal.kirim(pesan)


class PengelolaGOR:
    def __init__(self, nama_pengelola, daftar_kanal=None):
        self.nama_pengelola = nama_pengelola
        self.daftar_lapangan = []   
        self.daftar_pesanan = []
        self._daftar_kanal = daftar_kanal if daftar_kanal is not None else []

    def tambah_lapangan(self, lapangan_obj):
        self.daftar_lapangan.append(lapangan_obj)
        print(f"[BERHASIL] Lapangan {lapangan_obj.kode_lapangan} berhasil ditambahkan.")

    def tampilkan_semua_lapangan(self):
        garis = "=" * 85
        print(garis)
        print(f"|DAFTAR LAPANGAN TERSEDIA (DIKELOLA OLEH {self.nama_pengelola.upper()}):".ljust(84) + "|")
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

    def cari_pesanan(self, id_pesanan):
        for pesanan in self.daftar_pesanan:
            if pesanan.id_pesanan == id_pesanan:
                return pesanan
        return None

    def buat_pesanan(self, id_pesanan, kode_lapangan, durasi, sesi="pagi"):
        lapangan = self.cari_lapangan(kode_lapangan)
        if lapangan:
            pesanan_baru = PemesananJadwal(id_pesanan, lapangan, durasi, sesi)
            self.daftar_pesanan.append(pesanan_baru)
            print(f"[BERHASIL] Pesanan {id_pesanan} berhasil dibuat!")
            return pesanan_baru
        print(f"[ERROR] Lapangan dengan kode {kode_lapangan} tidak ditemukan!")
        return None

    def konfirmasi_pembayaran(self, id_pesanan):
        pesanan = self.cari_pesanan(id_pesanan)
        if pesanan is None:
            print(f"[ERROR] Pesanan {id_pesanan} tidak ditemukan!")
            return
        pesanan.update_status("Lunas")
        kirim_notifikasi(
            self._daftar_kanal,
            f"Pesanan {id_pesanan} sebesar Rp {pesanan.total_bayar:,} telah LUNAS. Terima kasih!",
        )

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

    print("=======================================")
    print("| BUKTI: ABSTRACT CLASS TIDAK BISA    |")
    print("| DIINSTANSIASI                       |")
    print("=======================================")
    try:
        lapangan_abstrak = Lapangan("Test", "Abstrak", "L-XX", 10000, "Sektor X")
    except TypeError as e:
        print(f"[TypeError] {e}\n")

    kanal_notifikasi = [
        NotifWhatsApp("0812-1111-2222"),
        NotifSMS("0813-3333-4444"),
        NotifEmail("customer@mail.com"),
    ]
    gor_system = PengelolaGOR("Larasati", kanal_notifikasi)

    lap1 = LapanganMatras("Yayas", "Matras Interlock Standard", "L-01", 50000, "Sektor A", "10mm")
    lap2 = LapanganVinyl("Zihni", "Vinyl Karpet Pro 5mm", "L-02", 65000, "Sektor B", "Standard BWF")
    lap3 = LapanganParquet("Laras", "Parquet Kayu Premium", "L-03", 80000, "VIP Sektor", "Jati Mahoni")

    gor_system.tambah_lapangan(lap1)
    gor_system.tambah_lapangan(lap2)
    gor_system.tambah_lapangan(lap3)
    print()
    gor_system.tampilkan_semua_lapangan()

    print("=====================================================")
    print("| POLIMORFISME PEWARISAN: 1 LOOP, PERILAKU BEDA     |")
    print("| (sewa 4 jam, sesi sore)                           |")
    print("=====================================================")
    for lap in [lap1, lap2, lap3]:
        print(f"{lap.kode_lapangan} {type(lap).__name__:<16} -> Rp {lap.hitung_total_sewa(4, 'sore'):,}")
    print()

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

    print("===========================================")
    print("| PEMBAYARAN, REKAP & DUCK TYPING NOTIFIKASI |")
    print("===========================================")
    gor_system.konfirmasi_pembayaran("ORD-001")
    gor_system.konfirmasi_pembayaran("ORD-003")
    print()
    gor_system.rekap_pemasukan()

    print("===============================")
    print("| PENGUJIAN OPERATOR OVERLOADING |")
    print("===============================")
    print(f"__str__ : {lap1}")
    print(f"__lt__  : lap1 < lap2 -> {lap1 < lap2}")
    print(f"__eq__  : lap1 == lap2 -> {lap1 == lap2}")
    print(f"__add__ : p1 + p3 -> Rp {p1 + p3:,}")
    print("sorted() otomatis memakai __lt__ (harga termurah ke termahal):")
    for lap in sorted([lap3, lap1, lap2]):
        print(f"  {lap}")
    print(f"max() -> {max([lap1, lap2, lap3])}")
    print()

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