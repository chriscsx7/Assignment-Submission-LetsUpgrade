# Write a program to implement insertion sort.
def insertion_sort(list2):
    for i in range(1, len(list2)):
        value = list2[i]
        j = i-1
        while j >= 0 and value < list2[j]:
            list2[j+1] = list2[j]
            j = j-1
        list2[j+1] = value


list1 = [76, 34, 18, 7, 90]
print("Unsorted list:")
for i in range(len(list1)):
    print(list1[i])

insertion_sort(list1)
print("Sorted list:")
for i in range(len(list1)):
    print(list1[i])
