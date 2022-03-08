nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


def selectionSort(anArray):
    for fillSlot in range(0, len(anArray)-2):
        #Search for minimum
        minPosition = fillSlot
        for i in range(fillSlot + 1, len(anArray)-1):
            if anArray[i] < anArray[minPosition]:
                minPosition = i
        
        temp = anArray[fillSlot]
        anArray[fillSlot] = anArray[minPosition]
        anArray[minPosition] = temp


#invoke functions
selectionSort(nums)
selectionSort(words)


#print results
print(nums)
print(words)