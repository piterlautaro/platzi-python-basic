def run():
	counter = 0
	with open('genesis01.txt') as f:
		for line in f:
			counter += line.count('Dios')
	print('Dios se encuentra {} veces en el texto'.format(counter))

if __name__ == '__main__':
	run()