def interpolation_search(arr, search_target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= search_target <= arr[high]:
        if low == high:
            if arr[low] == search_target:
                return low
            else:
                return -1

        pos = low + ((search_target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == search_target:
            return pos
        elif arr[pos] < search_target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == '__main__':
    total_element = 3496
    target = input("Enter the data to be looked for :")
    seq = range(0, total_element)
    list_seq = list(seq)
    print(list_seq)
    print(interpolation_search(list_seq, int(target)))
