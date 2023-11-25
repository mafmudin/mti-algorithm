def bubble_sort(val):
    for number in range(len(val) - 1, 0, -1):
        # range dari akhir daftar sampai awal, step -1 (turun)
        for i in range(len(val) - number, 0, -1):
            if val[i] < val[i - 1]:
                temp = val[i]
                val[i] = val[i - 1]
                val[i - 1] = temp


if __name__ == '__main__':
    array = [512, 12, 345, 678, 9]
    bubble_sort(array)
    print(array)
