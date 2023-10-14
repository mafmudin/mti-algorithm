if __name__ == '__main__':
    ulang = ""
    for i in range(10, -11, -1):
        ulang += str(i)
        if i != -10:
            ulang += " , "
    print(ulang)