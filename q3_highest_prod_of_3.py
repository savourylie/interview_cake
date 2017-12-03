from itertools import islice

def highest_of_3(lst):
	highest = max(lst[0], lst[1])
	lowest = min(lst[0], lst[1])

	highest_prod_of_2 = lst[0] * lst[1]
	lowest_prod_of_2 =  lst[0] * lst[1]

	highest_prod_of_3 = lst[0] * lst[1] * lst[2]

	for current in islice(lst, 2, None):
		# Update highest_prod_of_3
		highest_prod_of_3 = max(highest_prod_of_3, highest_prod_of_2 * current, lowest_prod_of_2 * current)

		# Update highest_prod_of_2
		highest_prod_of_2 = max(highest_prod_of_2, highest * current, lowest * current)
		# Update lowest_prod_of_2
		lowest_prod_of_2 = min(lowest_prod_of_2, highest * current, lowest * current)

		# Update highest
		highest = max(highest, current)
		# Update lowest
		lowest = min(lowest, current)

	return highest_prod_of_3


if __name__ == '__main__':
	test_list = [-10, -10, 1, 3, 2]
	print(highest_of_3(test_list))
	assert highest_of_3(test_list) == 300
	print("Tests passed.")