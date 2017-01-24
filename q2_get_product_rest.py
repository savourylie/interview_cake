def get_products_of_all_ints_except_at_index(lst):
	return [x[0] * x[1] for x in zip(get_products_of_all_ints_before_index(lst), get_products_of_all_ints_after_index(lst))]

def get_products_of_all_ints_before_index(lst):
	prod = 1
	result_list = [None] * len(lst)
	result_list[0] = 1

	for i, x in enumerate(lst):
		if i == len(lst) - 1:
			break
		prod = prod * x
		result_list[i + 1] = prod

	return result_list

def get_products_of_all_ints_after_index(lst):
	prod = 1
	result_list = [None] * len(lst)
	result_list[0] = 1

	for i, x in enumerate(lst[::-1]):
		if i == len(lst) - 1:
			break
		prod = prod * x
		result_list[i + 1] = prod

	return result_list[::-1]

def test_get_products_of_all_ints_except_at_index():
	lst = [1, 7, 3, 4]

	assert get_products_of_all_ints_except_at_index(lst) == [84, 12, 28, 21]
	print("All tests passed.")

if __name__ == '__main__':
	test_get_products_of_all_ints_except_at_index()