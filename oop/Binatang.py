class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def lompat(self):
        pass

    def susu(self):
        pass

    def bersuara(self):
        pass

    def makan(self):
        pass

    def lari(self):
        pass


class Kambing(Binatang):

    def __init__(self, ekor):
        self.ekor = ekor

    def lompat(self):
        print("Kambing melompat")

    def susu(self):
        print("Susu kambing")


class Gajah(Binatang):

    def __init__(self, hidung):
        self.hidung = hidung

    def makan(self, makanan):
        print("Memakan ", makanan)

    def bersuara(self):
        print("Gajah bersuara")


class Kuda(Binatang):

    def __init__(self, tinggi, warna):
        self.tinggi = tinggi
        self.warna = warna

    def lari(self):
        print("Kuda lari")

    def lompat(self):
        print("Kuda lompat")


class Pembalap(Kuda):
    def balapan(self):
        print("Kuda balapan")


class Berkuda(Kuda):
    def __init__(self, bobot):
        self.bobot = bobot

    def berlari(self):
        print("Kuda Berlari")

    def berlatih(self):
        print("Kuda Berlatih")


if __name__ == '__main__':
    berkuda = Berkuda(100)
    berkuda.berlari()

