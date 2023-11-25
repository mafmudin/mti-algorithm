import random


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Mengembalikan -1 jika elemen tidak ditemukan


if __name__ == '__main__':
    jumlah_elemen = 300000

    # Menghasilkan array acak dengan elemen float
    seq = range(0, jumlah_elemen)
    list_seq = list(seq)
    print(list_seq)
    print(binary_search(list_seq, 198265))