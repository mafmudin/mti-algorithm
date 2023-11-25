import random


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr


if __name__ == '__main__':
    jumlah_elemen = 100000

    # Menghasilkan array acak dengan elemen float
    arr = [random.randint(2, 100000) for _ in range(jumlah_elemen)]
    print(selection_sort(arr))
