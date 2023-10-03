def get_discount(total, member):
    if total >= 200000 and member == "y":
        return 20
    elif total >= 200000 and member == "n":
        return 10
    else:
        return 0


def count_total(total, member):
    disc = get_discount(total, member) / 100 * total
    return total - disc


if __name__ == '__main__':
    total = int(input("Total belanja :"))
    member = str(input("Apakah member ? y/n"))
    print("Diskon : ", get_discount(total, member), "%")
    print("Bayar :", count_total(total, member))
