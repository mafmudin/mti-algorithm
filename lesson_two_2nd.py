def get_score_grade(score):
    if score >= 80:
        return "A", 4
    elif score >= 65:
        return "B", 3
    elif score >= 45:
        return "C", 2
    elif score >= 20:
        return "D", 1
    else:
        return "E", 0


if __name__ == '__main__':
    score = int(input("Masukkan nilai : "))
    sks = int(input("Masukkan SKS : "))
    print("Nilai anda: ", get_score_grade(score)[0])
    print("Total Score: ", get_score_grade(score)[1] * sks)
