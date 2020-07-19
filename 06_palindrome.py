def palin2(word):
	return word == word[::-1]

def palin(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0,letter)

	reversed_word = ''.join(reversed_letters)

	return reversed_word == word

if __name__ == '__main__':
	word = str(input('Escribe una palabra: '))

	if palin2(word):
		print('{} si es un palíndromo.'.format(word))
	else:
		print('{} no es un palíndromo.'.format(word))