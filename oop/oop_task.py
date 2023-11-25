# polimorfisme
# contoh overriding

class Animal:
    def make_noise(self):
        print("Animal is making noise")


class Wolf(Animal):
    def make_noise(self):
        print("Woof!")

class Fish(Animal):
    def make_noise(self):
        print("krucuk-krucuk")


# ============================
# contoh enkapsulasi
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


if __name__ == '__main__':
    # implementasi overriding
    # Membuat objek
    wolf = Wolf()

    # Memanggil metode make_noise()
    wolf.make_noise()
    # Output: Woof!

    # ===================================

    #implementasi enkapsulasi
    # Membuat objek
    person = Person("John Doe", 30)

    # Mengakses properti name
    print(person.get_name())
    # Output: John Doe

    # Mengubah properti name
    person.set_name("Jane Doe")

    # Mengakses properti name lagi
    print(person.get_name())

    # ===================================

    # implementasi inheritance
    fish = Fish()

    fish.make_noise()
