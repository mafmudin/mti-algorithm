class Bunga:
    def __init__(self, nama, jumlah_kelopak, harga):
        self.nama = nama
        self.jumlah_kelopak = jumlah_kelopak
        self.harga = harga

    def set_nama(self, nama):
        self.nama = nama

    def set_jumlah_kelopak(self, jumlah_kelopak):
        self.jumlah_kelopak = jumlah_kelopak

    def set_harga(self, harga):
        self.harga = harga

    def get_nama(self):
        return self.nama

    def get_jumlah_kelopak(self):
        return self.jumlah_kelopak

    def get_harga(self):
        return self.harga


if __name__ == '__main__':
    bunga = Bunga("Mlati", 5, 30000)
    print(bunga.get_nama())
    bunga.set_nama("Mawar")
    print(bunga.get_nama())

