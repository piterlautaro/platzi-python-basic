import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''','''

    +---+
    |   |
    O	|
   /|   |
        |
        |
        =========''','''

    +---+
    |   |
    O	|
   /|\  |
        |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''']

WORDS = [
	'lavadora',
	'secadora',
	'sofa',
	'diputado',
	'gobierno',
	'piñera',
	'computador',
	'notebook',
	'teclado',
	'fiona',
	'hola',
	'harry',
	'potter'
]

def display_board(hidden_word,tries):
	print(IMAGES[tries])
	print('')
	print(hidden_word)
	print('--- * --- * --- * --- * ---')

def random_word():
	return WORDS[random.randint(0, len(WORDS) - 1)]

def run():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word,tries)
		current_letter = str(input('Escoge una letra: '))

		letter_indexes = []

		for i in range(len(word)):
			if word[i] == current_letter:
				letter_indexes.append(i)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 7:
				display_board(hidden_word,tries)
				print('')
				print('Has matado a tu amigo :(')
				print('La palabra correcta era {}'.format(word))
				break
		else:
			for i in letter_indexes:
				hidden_word[i] = current_letter

			letter_indexes = []

			try:
				print(hidden_word.index('-'))
			except ValueError:
				print('')
				print('¡Tu amigo se ha salvado!')
				print('Has adivinado la palabra {}'.format(word))
				break

if __name__ == '__main__':
	print(' B I E N V E N I D O S   A L   A H O R C A D O ')
	run()