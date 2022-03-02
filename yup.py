nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]


#Initialize a function that will sort the array using the bubble sort alg
def bubbleSort(anArray):
    for x in range(len(anArray)-1): 
        for i in range(x+1):
            if anArray[i] > anArray[i + 1]:
                temp = anArray[i]
                anArray[i] = anArray[i + 1]
                anArray[i + 1] = temp

# #Initialize a function that will sort the array using the bubble sort alg
# def bubbleSort(anArray):
#     for x in range(len(anArray)-1): 
#         count = 1
#         for i in range(len(anArray)-count):
#             if anArray[i] > anArray[i + 1]:
#                 temp = anArray[i]
#                 temp2 = anArray[i + 1]
#                 anArray[i] = temp2
#                 anArray[i + 1] = temp
#                 count+=1

 #invoke functions
bubbleSort(nums)
bubbleSort(words)


#print results
print(nums)
print(words)
