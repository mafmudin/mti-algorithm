import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


if __name__ == '__main__':
    jumlah_elemen = 100000000

    # Menghasilkan array acak dengan elemen float
    arr = [random.randint(2, 100000) for _ in range(jumlah_elemen)]

    print(quick_sort(arr))
