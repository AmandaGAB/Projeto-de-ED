from Gerenciador import *
import pickle

def menu():

	print(
		f'-----------------MENU-----------------\n',
		f'Opção 1 - Configurar banda\n',
		f'Opção 2 - Cadastrar computadores\n',
		f'Opção 3 - Cadastrar recursos\n',
		f'Opção 4 - Importar/Exportar\n',
		f'Opção 5 - Listar Jobs\n',
		f'Opção 6 - Inserir jobs para processamento (download)\n',
		f'Opção 7 - Remover Job')


op = ''
while op!=0:
	try:
		menu()
		op = int(input('Digite uma opção: '))

	#CONFIGURAR BANDA
		if op == 1:
			banda = int(input('Qual é a banda da sua internet (Mbps)? '))
			gerenciador.setBanda(banda)
			print(f'A banda da sua internet é {gerenciador.banda} Mbps')

	#CADASTRAR COMPUTADORES

		if op == 2:
			ip = str(input('Digite o ip:'))
			if gerenciador.computadorCadastrado(ip): #verifica se está cadastrado e se não estiver:
				print('O computador já está cadastrado')
			else:
				prioridade = 's' #determina prioridade e
				gerenciador.criarCadastroPC(ip, prioridade)      #cria objeto Computador

	#CADASCTRAR RECURSOS

		if op == 3:
			nome = str(input('Digite o nome:'))
			if gerenciador.recursoCadastrado(nome): #verifica se está cadastrado e se não estiver:
				print('O recurso já está cadastrado')
			else:
				tamanho = int(input('Digite o tamanho (KB):')) #determina tamanho
				gerenciador.criarCadastroRec(nome, tamanho) #cria objeto Recurso


		#IMPORTAR / EXPORTAR COMPUTADORES

		if op == 4:
			op = str(input('Digite (r) para carregar ou (w) para gravar computadores e recursos cadastrados: ')).lower()
			if op == 'r':
				gerenciador.importarComputador()
				gerenciador.importarRecursos()
				print('As listas foram carregadas!')
			if op == 'w':
				gerenciador.exportarComputador()
				gerenciador.exportarRecursos()
				print('As listas foram gravadas no disco!')

		if op == 5:

			gerenciador.imprimirJobs()


		#INSERIR JOBS PARA PROCESSAMENTO (DOWNLOAD)
		if op == 6:
			gerenciador.imprimirComputadores()
			gerenciador.imprimirRecursos()
			ip = str(input('Digite o ip:'))
			nome = str(input('Digite o nome:'))
			if gerenciador.computadorCadastrado(ip) and gerenciador.recursoCadastrado(nome):
				pc = gerenciador.getComputador(ip)
				re = gerenciador.getRecurso(nome)
				job = Job(pc, re) #Cria objeto job com computador e  recurso
				gerenciador.inserirJob(1, job) #insere o job na lista circular encadeada
				print(f'Um job foi adicionado para processamento (download)')
			else:
				raise GerenciadorException('Computador ou recurso não está cadastrado!')
		
		if op == 7:
			posicao = int(input('Digite a posição que deseja remover o job:'))
			gerenciador.removerJob(1)
			
		if op == 8:
			print(gerenciador.jobs.tamanho())
			# print(gerenciador.jobs)
			gerenciador.jobs.imprimir()

	except GerenciadorException as a: 
		print(a)
	except Exception as e:
		print('Nossos engenheiros irão analisar esse problema')
		print(e.__class__.__name__)