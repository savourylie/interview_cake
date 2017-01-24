def get_max_profit(stock_prices):
	# Boundary conditions
	if len(stock_prices) < 2:
		return 0

	min_price = stock_prices[0]
	candidate = max(0, stock_prices[1] - stock_prices[0])

	for x in stock_prices:
		if x < min_price:
			min_price = x

		candidate = max(candidate, x - min_price)
			
	return candidate

def test_get_max_profit():
	stock_prices_yesterday1 = [10, 7, 5, 8, 11, 9]
	stock_prices_yesterday2 = [10, 7, 5, 2, 8, 11, 20, 1, 9]

	assert get_max_profit(stock_prices_yesterday1) == 6
	assert get_max_profit(stock_prices_yesterday2) == 18

	print("All tests passed.")


if __name__ == '__main__':
	test_get_max_profit()