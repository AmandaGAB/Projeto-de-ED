from Recurso import *


class CompException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Computador:
    id = 1
    def __init__(self, ip): 
        self.__id = Computador.id      
        self.__ip = ip   
        self.__temPrioridade = False
        self.__nome = f'IFPB0{self.__id}'
        Computador.id += 1
  
    @property
    def ip(self):
        return self.__ip
    @property
    def nome(self):
        return self.__nome
    @property
    def temPrioridade(self):
        return self.__temPrioridade

    def setIp(self, ip):
        self.__ip = ip

    def setPriority(self):
        self.__temPrioridade = True
    
    def request(self, Recurso = None):
        if self.__ip == '0.0.0.0' or type(self.__ip) != str:
            raise CompException('Você deve setar um ip válido.')
        if Recurso == None or Recurso.name == None or Recurso.size == 0:
            raise CompException('Defina um Recurso válido.')
        try:
            return f'[{self.__nome}; {self.__ip}; {Recurso.name}; {Recurso.size}]'
        except:
            raise CompException('Faltam argumentos.')


    def __str__(self):
        if self.__ip == '0.0.0.0':
            raise CompException('Você deve setar um ip válido')
        return f'{self.__nome} tem ip {self.__ip} | Prioridade: {self.__temPrioridade}'



# pc1 = Computador('1')
# pc2 = Computador('2')
# pc3 = Computador('3')