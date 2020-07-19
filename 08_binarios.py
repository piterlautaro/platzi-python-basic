def binary_search(numbers, number_to_find, low, high):
	if low > high:
		return False

	mid = (low + high) // 2

	if numbers[mid] == number_to_find:
		return True
	elif numbers[mid] > number_to_find:
		return binary_search(numbers, number_to_find, low, mid - 1)
	else:
		return binary_search(numbers, number_to_find, mid + 1, high)

if __name__ == '__main__':
	
	numbers = [1,3,4,5,6,8,9,10,13,15,17,20,23,45,67,78,89,99]

	number_to_find = int(input('Ingresa un número:'))

	result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

	if result:
		print('El número si está en la lista')
	else:
		print('El número no está en la lista')