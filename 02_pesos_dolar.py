def foreign_exchange_calculator(ammount):
	dolar_val = 787.87
	return dolar_val * ammount

def run():
	print('C A L C U L A D O R A  D E  P E S O S  C H I L E N O S  A  D O L A R')
	print('')
	ammount = float(input('¿Cuántos pesos chilenos desea convertir?: '))

	result = foreign_exchange_calculator(ammount)

	print('${} dólares son ${} pesos chilenos'.format(ammount,result))

if(__name__ == '__main__'):
	run()