if __name__ == '__main__':
    fruitArray: list[str] = ["apple", "semangka", "pisang", "jambu", "durian", "nangka", "duku", "sirsak"]

    # add item to array
    fruitArray[4] = "Gomu gomuno"
    fruitArray.insert(100, "Tomat")

    # remove item
    fruitArray.pop(2)
    fruitArray.remove("jambu")

    # convert to set
    fruitArray = list(fruitArray)

    # print array length
    print("Panjang array :", len(fruitArray), "\n")

    # print array items
    print(fruitArray[1], "\n")
    for fruit in fruitArray:
        print(fruit)

    # access item with :
    print(fruitArray)
    print(fruitArray[4:])
    print(fruitArray[:5])

    # reverse array
    reversedArray = list(reversed(fruitArray))
    print(reversedArray)

    # copy array
    copyFruit = fruitArray.copy()
    if "Tomat" in fruitArray:
        print("Exist")

    copyFruit.pop()
    print(copyFruit)

    drinkArray = ["teh", "kopi", "susu", "latte", "juice"]

    # 2 dimension array
    combinedArray = [fruitArray, drinkArray]

    print(combinedArray)
    print(combinedArray[0][0])
    print(combinedArray[1][0])

    # dictionary from existing array
    combinedDictionary = {
        "buah": fruitArray,
        "minuman": drinkArray
    }

    print(combinedDictionary)
    print(combinedDictionary.get("buah"))

    # use item
    print(combinedDictionary.items())

    # use value
    print(combinedDictionary.values())

    # print dictionary
    for i in combinedDictionary:
        print("\t", i)
        for dictItem in combinedDictionary[i]:
            print(dictItem)

    # add data to dictionary
    combinedDictionary["makanan"] = ["bebek goreng", "ayam bakar"]

    del combinedDictionary["buah"]
    combinedDictionary["makanan"].sort()
    print(combinedDictionary)

    # make a tuple
    fruitTuple = tuple(fruitArray)
    print(fruitTuple)

    # update tuple value
    tempList = list(fruitTuple)
    tempList[1] = "durian"
    fruitTuple = tuple(tempList)
    print(fruitTuple)

    fruitSet = set(fruitArray)

    if "mangga" in fruitSet:
        print("Ada mangga")
    else:
        print("Tidak ada mangga")
