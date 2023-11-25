import random


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Mengembalikan -1 jika elemen tidak ditemukan


if __name__ == '__main__':
    jumlah_elemen = 300000

    # Menghasilkan array acak dengan elemen float
    arr = [random.randint(2, 300000) for _ in range(jumlah_elemen)]
    print(arr)
    print(linear_search(arr, 185692))
