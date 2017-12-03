def fib(n):
	if n == 0:
		return 0
		
	fibs = [0, 1]

	while len(fibs) - 1 < n:
		fibs.append(fibs[-1] + fibs[-2])

	return fibs[-1]


if __name__ == '__main__':
	assert fib(0) == 0
	assert fib(1) == 1
	assert fib(2) == 1
	assert fib(3) == 2
	assert fib(4) == 3
	assert fib(5) == 5
	assert fib(6) == 8
	assert fib(7) == 13
	assert fib(8) == 21
	assert fib(9) == 34

	print("Tests passed.")