def moveTower(n, start, finish, temp):
	if n == 1:
		print(start + " -> " + finish)
	else:
		moveTower(n-1, start, temp, finish)
		print(start + " -> " + finish)
		moveTower(n-1, temp, finish, start)





moveTower(3, "A", "B", "C")