def ash_search(arr, s_num):
  """
  Mencari elemen target dalam larik data yang telah diurutkan menggunakan algoritma Ash Search.

  Args:
    arr: Larik data yang telah diurutkan (vector).
    s_num: Elemen target yang dicari.
    t_elem: Jumlah elemen dalam larik.

  Returns:
    Posisi elemen target dalam larik data, atau -1 jika elemen target tidak ditemukan.
  """
  t_elem = len(arr)
  start = 0
  end = t_elem - 1

  while start <= end:
    # Hitung perkiraan variasi
    if start == 0 and end == t_elem - 1:
      est_var = float("inf")
    else:
      est_var = (arr[end] - arr[start]) / (end - start)

    # Hitung perkiraan indeks
    est_idx = int(((s_num - arr[start]) / est_var) + start)

    # Periksa elemen target
    if arr[est_idx] == s_num:
      return est_idx
    elif s_num > arr[est_idx]:
      start = est_idx + 1
    else:
      end = est_idx - 1

    # Perbaikan pencarian biner
    mid = start + int((0.5) * (end - start))
    if arr[mid] <= s_num:
      start = mid
    else:
      end = mid

  # Elemen target tidak ditemukan
  return -1


def binary_search(data, target):
    """
  Mencari elemen target dalam larik data yang telah diurutkan menggunakan algoritma binary search.

  Args:
    data: Larik data yang telah diurutkan.
    target: Elemen yang dicari.

  Returns:
    Posisi elemen target dalam larik data, atau -1 jika elemen target tidak ditemukan.
  """

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    jumlah_elemen = 300000

    # Menghasilkan array acak dengan elemen float
    seq = range(0, jumlah_elemen)
    list_seq = list(seq)
    print(list_seq)

    # print(ash_search(list_seq, 125000))
    print(binary_search(list_seq, 125000))
