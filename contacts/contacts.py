class Contact:

	def __init__(self, name, phone, email):
		self._name = name
		self._phone = phone
		self._email = email

class ContactBook:

	def __init__(self):
		self._contacts = []

	def add(self, name, phone, email):
		print('name: {}, phone: {}, email: {}'.format(name, phone, email))

def run():

	contact_book = ContactBook()

	while(True):
		command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
			'''))

		if command == 'a':
			name = str(input('Nombre: '))
			phone = str(input('Teléfono: '))
			email = str(input('Email: '))

			contact_book.add(name, phone, email)

		elif command == 'ac':
			print('actuaizar contacto')

		elif command == 'b':
			print('buscar contacto')

		elif command == 'e':
			print('eliminar contacto')

		elif command == 'l':
			print('listar contactos')

		else:
			print('salir')

if __name__ == '__main__':
	print('B I E N V E N I D O  A  L A  A G E N D A')
	run()