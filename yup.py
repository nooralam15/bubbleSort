nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


def selectionSort(anArray):
    for fillSlot in range(len(anArray)-1, 0, -1):
        #Search for minimum
        minPosition = fillSlot
        for i in range(fillSlot):
            if anArray[i] > anArray[minPosition]:
                minPosition = i
        
        temp = anArray[fillSlot]
        anArray[fillSlot] = anArray[minPosition]
        anArray[minPosition] = temp


#invoke functions
selectionSort(nums)

#print results
print(nums)
print(words)