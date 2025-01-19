from leia import leiaInt
dicio = {}
f = '\033[m' #Fim
vd = '\033[1;32m' #Verde
am = '\033[1;33m' #Amarelo
az = '\033[1;34m' #Azul

def menu():
	print(f'''{am}1{f} - {az}Ver pessoas registadas
{am}2{f} - {az}Registar nova Pessoa
{am}3{f} - {az}Sair do Sistema {f}
''' + '-' *67)


def titulo(txt):
	print('-' * 67)
	print(f"{txt:^67}")
	print('-' * 67)
	
while True:	
	titulo('MENU PRINCIPAL')
	menu()
	while True:
		opc = leiaInt(f"{vd}Sua opção: {f}")
		if opc <= 0 or opc >= 4:
			print('\033[1;31mERRO! Digite uma opção válida.\033[m')
		else:
			break
			
	if opc == 1:
		with open('D115.py', 'r') as arquivo:
			conteudo = arquivo.read()
		titulo('Pessoas Registadas')
		print(conteudo)
			
	elif opc == 2:
		print()
		with open('D115.py', 'a') as arquivo:
			dicio['Nome'] = input('Nome: ').strip().capitalize()
			dicio['Idade'] = leiaInt('Idade: ')
			arquivo.write(f"{dicio['Nome']}{dicio['Idade']:>40} anos\n")
	
	else:
		titulo('Saindo do Sistema...')
		break