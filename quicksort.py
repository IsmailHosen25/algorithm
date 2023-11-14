def quicksort(arr, lowrange, highrange):
	if lowrange < highrange:
		temp = part(arr, lowrange, highrange)
		quicksort(arr, lowrange, temp - 1)
		quicksort(arr, temp + 1, highrange)

def part(arr, lowrange, highrange):
	pivot = arr[highrange]
	i = lowrange - 1
	for j in range(lowrange, highrange):
		if arr[j] <= pivot:
			i = i + 1
			(arr[i], arr[j]) = (arr[j], arr[i])
	(arr[i + 1], arr[highrange]) = (arr[highrange], arr[i + 1])
	return i + 1

arr = [34, 78, 1, 19,79, 101, 0,67]
highrange= len(arr)-1
print("Not Sorted array -",arr)
quicksort(arr, 0, highrange)
print("Sorted Array - ",arr)

