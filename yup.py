nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


def insertionSort(anArray):
    for insertPos in range(1, len(anArray)):
        insertVal = anArray[insertPos]

        while anArray[insertPos - 1] > insertVal:
            

