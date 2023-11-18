class Pembaca:
    def __init__(self):
        self.koleksi = []
        self.dibaca = []

    def membeli(self, judul_buku):
        self.koleksi.append(judul_buku)
        print("Membeli", judul_buku)

    def membaca(self, judul_buku):
        if judul_buku in self.koleksi:
            self.dibaca.append(judul_buku)
            print("Membaca", judul_buku)
        else:
            print(f"Buku {judul_buku} Belum di beli")

    def get_buku_dibeli(self):
        return self.koleksi

    def get_buku_dibaca(self):
        return self.dibaca


if __name__ == '__main__':
    pembaca = Pembaca()
    pembaca.membeli("Pinokio")
    pembaca.membeli("Cinderela")
    pembaca.membaca("Ande-ande lumut")
    pembaca.membaca("Pinokio")

    print(pembaca.get_buku_dibaca())
    print(pembaca.get_buku_dibeli())
