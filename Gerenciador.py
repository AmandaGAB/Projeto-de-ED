from Computador import *
from Recurso import *
from Job import *
from Ciclo import *
import pickle

# PARA TRATAMENTO DE EXCESSÕES DO GERENCIADOR
class GerenciadorException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Gerenciador:
    def __init__(self, computadores = [], recursos = []):
        self.__computadores = computadores # lista criada para inserir computadores que são/serão cadastrados
        self.__recursos = recursos #lista criada para inserir recursos que são/serão cadastrados
        self.__jobs = Ciclo() # Ciclo() 
        self.__banda = 0
        
    
    #MÉTODOS ACESSADORES
    @property
    def banda(self):
        return self.__banda

    @property
    def computadores(self):
        return self.__computadores

    @property
    def recursos(self):
        return self.__recursos

    @property
    def jobs(self):
        return self.__jobs


    #Métodos modificadores
    def setBanda(self, novaBanda):
        self.__banda = novaBanda
    #------------------------------------------------------------------------------#

    #Verifica se a lista de computadores cadastrados está vazia e verifica se o pc desejado está cadastrado (compara ip)

    def computadorCadastrado(self, ip):
        if len(self.__computadores) == -1: 
            raise CompException('Não há computadores cadastrados')
        for i in self.__computadores:
            if ip == i.ip:
                return True
        return False
    
    #Se o pc estiver cadastrado ele exibe mensagem, se não = cria objeto, seta prioridade e insere na lista de computadores cadastrados
    def criarCadastroPC(self, ip, prioridade):
        if self.computadorCadastrado(ip):
            print('O computador já está cadastrado!')
        else:   
            pc = Computador(ip)
            if prioridade == 's':
                pc.setPriority()
            self.__computadores.append(pc)

    #Verifica se a lista de recursos cadastrados está vazia e verifica se o recurso desejado está cadastrado (compara nome)   
    def recursoCadastrado(self, nome):
        if len(self.__recursos) == -1:
            raise CompException('Não há computadores cadastrados')
        for i in self.recursos:
            if i.name == nome:
                return True
        return False

    #Verifica se o recurso está cadastrado, se não, cria objeto recurso com o nome e tamanho desejado e add na lista de recursos cadastrados
    def criarCadastroRec(self, nome, tamanho):
        if self.recursoCadastrado(nome):
            print('O recurso já está cadastrado')
        else:
            r = Recurso(nome, tamanho)
            self.__recursos.append(r)
    
    #Cria arquivo com módulo pickle e grava a lista de computadores cadastrados na sessão
    def exportarComputador(self):
        abrir = open('lista_computadores.pkl', 'wb')
        pickle.dump(self.__computadores, abrir)   
        abrir.close()

    #Abre arquivo anterior e carrega os computadores para a lista de cadastrados
    def importarComputador(self):
        abrir = open('lista_computadores.pkl', 'rb')
        self.__computadores = pickle.load(abrir) 
        abrir.close()

        
    #Cria arquivo com módulo pickle e grava a lista de recursos cadastrados na sessão
    def exportarRecursos(self):
        abrir = open('lista_recursos.pkl', 'wb')
        pickle.dump(self.recursos, abrir) #close
        abrir.close()

    #Abre arquivo anterior e carrega os recursos para a lista de cadastrados
    def importarRecursos(self):
        abrir = open('lista_recursos.pkl', 'rb')
        self.__recursos = pickle.load(abrir)
        abrir.close()
            

    #Retorna pc com ip desejado que está na lista de computadores cadastrados
    def getComputador(self, ip):
        for i in self.__computadores:
            if i.ip == ip:
                return i

    #Retorna recurso com nome desejado que está na lista de recursos cadastrados
    def getRecurso(self, nome):
        for i in self.__recursos:
            if i.name == nome:
                return i

    #Inseri o job na lista circular encadeada 
    def inserirJob(self, posicao, job):
        try:
            self.__jobs.inserir(posicao, job)   
        except:
            raise GerenciadorException('Não é possível inserir um job!')
                  

    def imprimirJobs(self):
        # if self.__jobs.estaVazia():
        #     print('A lista está vazia')
        # else:
        try:
            self.__jobs.imprimir()
        except:
            raise GerenciadorException('A lista está vazia')

    def removerJob(self, posicao):
        try:
            self.__jobs.remover(posicao)
        except:
            raise GerenciadorException('Agora não é possível remover um job.')

    def imprimirComputadores(self):
        print('------Computadores cadastrados------')
        cont = 0
        for i in self.__computadores:
            cont+=1
            print(f'{cont}', f' - {i}', end='')
            print(f'\n')

    def imprimirRecursos(self):
        print('------Recursos cadastrados------')
        cont = 0
        for i in self.__recursos:
            cont+=1
            print(f'{cont}', f' - {i}', end='')
            print(f'\n')
               
gerenciador = Gerenciador()

   


#USAR RECURSIVIDADE
# a = float(input('Qual a banda da internet? '))
# b = float(input('Quantos computadores deseja executar? '))
# #c = float(input('Qual o tamanho do recurso? '))

# divisao = a / b
# acrescimo = divisao * a / 100
# print(f'Cada máquina vai ficar com: {divisao:.2f}') #PC sem prioridade quando n tem pc com prioridade

# if pc.temPrioridade == True:
#     prioridade = divisao + acrescimo
#     print(acrescimo) #PC com prioridade

# #recalculo da banda
# o = divisao - prioridade/b #pc sem prioridade 


