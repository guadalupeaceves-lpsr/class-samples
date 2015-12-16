for avocado_num in range(1,26):
	avocado_cost = float( avocado_num * 1.25)
	avocado_cost_str = str(avocado_cost)
	print(str(avocado_num) + " avocados will cost you $" + avocado_cost_str)
	if avocado_num == 5 or avocado_num == 10 or avocado_num == 15 or avocado_num == 20 or avocado_num == 25:
		avocado_extra = avocado_num / 5
		print("And you've earned " + str(avocado_extra) + " bonus avocado!")
