# the following was copied from https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def sort(elements):
	swapped = False
	# Looping from size of array from last index[-1] to index [0]
	for n in range(len(elements)-1, 0, -1):
		for i in range(n):
			if elements[i] > elements[i + 1]:
				swapped = True
				# swapping data if the element is less than next element in the array
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
		if not swapped:
			# exiting the function if we didn't make a single swap
			# meaning that the array is already sorted.
			return elements
