from abc import ABC, abstractmethod


class Lapangan(ABC):
    jumlah_lapangan = 0
    nama_lapangan = "GOR BADMINTON ALL ROUND"
    jam_operasional = "08.00 - 00.00 WITA"
    kontak_pengelola = "0812-3456-7890"

    def __init__(self, nama_customer, nama_lapangan, kode_lapangan, harga, lokasi):
        self.nama_customer = nama_customer
        self.nama_lapangan = nama_lapangan
        self.kode_lapangan = kode_lapangan
        self.lokasi = lokasi
        self.__harga = 0
        self.harga = harga
        
        Lapangan.jumlah_lapangan += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru < 0:
            print("error: Gagal mengubah harga! Harga sewa harus berupa angka positif.")
        else:
            self.__harga = nilai_baru

    @staticmethod
    def validasi_durasi(durasi):
        if isinstance(durasi, int) and 1 <= durasi <= 8:
            return True
        return False
    
    @classmethod
    def ubah_jam_operasional(cls, jam_baru):
        if isinstance(jam_baru, str) and jam_baru.strip() != "":
            cls.jam_operasional = jam_baru
            print(f"Jam operasional lapangan telah diubah menjadi: {cls.jam_operasional}")
        else:
            print("error: Jam operasional harus berupa string yang valid.")

    @classmethod
    def tampilkan_info_gor(cls):
        print("=" * 43)
        print(f"          INFORMASI GOR: {cls.nama_lapangan}")
        print("=" * 43)
        print(f"Jam Operasional : {cls.jam_operasional}")
        print(f"Kontak CS       : {cls.kontak_pengelola}")
        print(f"Total Lapangan  : {cls.jumlah_lapangan} Lapangan")
        print("=" * 43 + "\n")

    @abstractmethod
    def hitung_biaya_sewa(self, durasi, sesi="pagi"):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass 

class LapanganMatras(Lapangan):
    def __init__(self, nama_customer, nama_lapangan, kode_lapangan, harga, lokasi="Gedung All Round", jenis_matras="Interlock"):
        super().__init__(nama_customer, nama_lapangan, kode_lapangan, harga, lokasi)
        self.jenis_matras = jenis_matras

    def hitung_biaya_sewa(self, durasi, sesi="pagi"):
        biaya = self.harga * durasi
        if sesi.lower() == "sore":
            biaya += 35000 * durasi
        elif sesi.lower() == "malam":
            biaya += 35000 * durasi
        return biaya

    def tampilkan_info(self):
        print(f"[{self.nama_lapangan}] {self.nama_lapangan} (matras {self.jenis_matras}) | lokasi: {self.lokasi} | Harga/Jam: Rp{self.harga:,}")

class LapanganVinyl(Lapangan):
    def __init__(self, nama_customer, nama_lapangan, kode_lapangan, harga, lokasi="Gedung All Round", ketebalan_mm=5):
        super().__init__(nama_customer, nama_lapangan, kode_lapangan, harga, lokasi)
        self.ketebalan_mm = ketebalan_mm

    def hitung_biaya_sewa(self, durasi, sesi="pagi"):
        biaya = (self.harga + 25000) * durasi
        if sesi.lower() == "sore":
            biaya += 25000 * durasi
        elif sesi.lower() == "malam":
            biaya += 25000 * durasi
        return biaya
    
    def tampilkan_info(self):
        print(f"[{self.kode_lapangan}] {self.nama_lapangan} (Vinyl {self.ketebalan_mm}mm) | Lokasi: {self.lokasi} | Harga/Jam: Rp{self.harga:,}")

class pemesananjadwal:
    total_transaksi = 0
    daftar_transaksi = []

    def __init__(self, id_pemesanan, no_lapangan, durasi, sesi="pagi", sewa_raket=False, jumlah_kok=0):
        self.id_pemesanan = id_pemesanan
        self.lapangan = no_lapangan
        self.durasi = durasi
        self.sesi = sesi.lower()
        self.sewa_raket = sewa_raket
        self.jumlah_kok = jumlah_kok
        self.__status_pelunasan = "Belum lunas"
        self.__biaya_tambahan = self.__hitung_tambahan()
        self.__total_pembayaran = self.lapangan.hitung_biaya_sewa(durasi, sesi=self.sesi) + self.__biaya_tambahan
        pemesananjadwal.total_transaksi += 1
        pemesananjadwal.daftar_transaksi.append(self)

    def __hitung_tambahan(self):
        total_ekstra = 0
        if self.sewa_raket:
            total_ekstra += 20000 * self.durasi
        if self.jumlah_kok > 0:
            total_ekstra += 15000 * self.jumlah_kok
        return total_ekstra 

    @property
    def status_pelunasan(self):
        return self.__status_pelunasan

    @status_pelunasan.setter
    def status_pelunasan(self, status_baru):
        status_valid = ["Belum lunas", "Lunas", "Dibatalkan"]
        if status_baru in status_valid:
            self.__status_pelunasan = status_baru
            print(f" SUCCESS {self.id_pemesanan} diperbarui menjadi: {self.__status_pelunasan}")
        else:
            print(f"error: Status '{status_baru}' tidak valid. Pilih dari {status_valid}.")

    @property 
    def total_pembayaran(self):
        return self.__total_pembayaran

    @classmethod
    def rekap_pendapatan_lunas(cls):
        total = sum(order.total_pembayaran for order in cls.daftar_transaksi if order.status_pelunasan == "Lunas")
        print(f"Total Pendapatan (Status Lunas): Rp{total:,}")
        return total

    @staticmethod
    def cari_transaksi_by_id(id_search):
        for order in pemesananjadwal.daftar_transaksi:
            if order.id_pemesanan.upper() == id_search.upper():
                return order
        return None


    def cetak_struk(self):
        print("="*42)
        print(f"STRUK PEMESANAN - {Lapangan.nama_lapangan}")
        print(f"    Kontak CS: {Lapangan.kontak_pengelola}")
        print("="*42)
        print(f"ID Pemesanan   : {self.id_pemesanan}")
        print(f"Nama Customer  : {self.lapangan.nama_customer}")
        print(f"Lapangan       : {self.lapangan.nama_lapangan} ({self.lapangan.kode_lapangan})")
        print(f"Lokasi         : {self.lapangan.lokasi}")
        print(f"Durasi Sewa    : {self.durasi} Jam (sesi {self.sesi.capitalize()})")

        if self.sewa_raket or self.jumlah_kok > 0:
            print("-" * 42)
            print("Fasilitas Tambahan:")
            if self.sewa_raket:
                print(f" - Sewa Raket  : Rp20,000 x {self.durasi} jam")
            if self.jumlah_kok > 0:
                print(f" - Shuttlecock : Rp15,000 x {self.jumlah_kok} pcs")
            print("-" * 42)

        print(f"Total Biaya    : Rp{self.__total_pembayaran:,}")
        print(f"Status         : {self.__status_pelunasan}")
        print("="*42 + "\n")


if __name__ == "__main__":
    Lapangan.tampilkan_info_gor()

    lap_matras1 = LapanganMatras("Andi", "Lapangan A", "L01", 40000, "Lantai 1", "Interlock")
    lap_matras2 = LapanganMatras("yayas", "Lapangan B", "L02", 45000, "Lantai 1", "Rubber")
    lap_vinyl1 = LapanganVinyl("Laras", "Lapangan C", "L03", 60000, "Lantai 1", 5)
    lap_vinyl2 = LapanganVinyl("zihni", "Lapangan D", "L04", 75000, "Lantai 1", 7)

    order1 = pemesananjadwal("A01", lap_matras1, durasi=2, sesi="pagi")
    order2 = pemesananjadwal("B02", lap_vinyl1, durasi=3, sesi="sore")
    order3 = pemesananjadwal("C03", lap_matras2, durasi=2, sesi="malam")
    order4 = pemesananjadwal("D04", lap_vinyl2, durasi=3, sesi="malam")

    order1.status_pelunasan = "Lunas"
    order3.status_pelunasan = "Lunas" 

    lap_matras1.tampilkan_info()
    lap_matras2.tampilkan_info()
    lap_vinyl1.tampilkan_info()
    lap_vinyl2.tampilkan_info()
    print()
    order1.cetak_struk()
    order2.cetak_struk()
    order3.cetak_struk()
    order4.cetak_struk()


    Lapangan.ubah_jam_operasional("07.30 - 23.00 WITA")
    print(f"Kontak Pengelola: {Lapangan.kontak_pengelola}")
    print(f"Total Lapangan Terdaftar: {Lapangan.jumlah_lapangan}")
    print(f"Total Transaksi Terdaftar: {pemesananjadwal.total_transaksi}\n")
    print(f"Validasi durasi 3 jam : {Lapangan.validasi_durasi(3)}")
    print(f"Validasi durasi 10 jam: {Lapangan.validasi_durasi(10)}\n")

    print(f"Harga awal {lap_matras2.nama_lapangan}: Rp{lap_matras2.harga:,}")
    lap_matras2.harga = 50000
    print(f"Harga baru {lap_matras2.nama_lapangan}: Rp{lap_matras2.harga:,}\n")

    pemesananjadwal.rekap_pendapatan_lunas()

    id_cari = "B02"
    hasil_cari = pemesananjadwal.cari_transaksi_by_id(id_cari)
    if hasil_cari:
        print(f"\nTransaksi dengan ID {id_cari} ditemukan atas nama {hasil_cari.lapangan.nama_customer}.")
    else:
        print(f"\nTransaksi {id_cari} tidak ditemukan.")