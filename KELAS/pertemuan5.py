class akunbank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def hitung_bunga(self):
        return 0

class tabungan(akunbank):

    def hitung_bunga(self):
        return self.saldo * 0.02
    
class doposito(akunbank):
    def hitung_bunga(self):
        return self.saldo * 0.06

    def tariku_uang(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
        else:
            print('saldo  tidak cukup')

class rekening_giro:
    def __init__(self, saldo):
        self.saldo = saldo

    def tarik_uang(self, saldo):
        if saldo <= self.saldo:
            self.saldo -= saldo
        else:
            print('saldo tidak cukup')

    