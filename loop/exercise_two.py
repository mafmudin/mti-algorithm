def count_loop(n):
    result = 0
    for i in range(2, n+1):
        result += (1/i)
        print(str(1), "/", str(i))
    return result


if __name__ == '__main__':
    n = input("Masukkan nilai n: ")
    print(count_loop(int(n)))
