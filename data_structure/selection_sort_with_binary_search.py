def binary_search(data, search_target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == search_target:
            return mid
        elif search_target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def selection_sort_with_binary_search(data):
    sorted_array = []
    while data:
        smallest_element_index = binary_search(data, min(data))
        sorted_array.append(data[smallest_element_index])
        data.pop(smallest_element_index)
    return sorted_array


if __name__ == '__main__':
    array = [5, 3, 2, 1, 4]
    # target = input("masukkan yang di cari :")
    # index = binary_search(array, int(target))
    #
    # if index == -1:
    #     print("The target element is not in the array.")
    # else:
    #     print("The target element is at index {}.".format(index))

    print(selection_sort_with_binary_search(array))
