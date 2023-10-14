if __name__ == '__main__':
    text = "UNIVERSITAS TEKNOLOGI DIGITAL INDONESIA"
    a = 0
    t = 0
    for i in text:
        if i == "A":
            a += 1
        if i == "T":
            t += 1

    print("Total A :", a)
    print("Total T :", t)

