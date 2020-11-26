from Computador import *
from Recurso import *


class JobException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Job:
    def __init__(self, Computador = None, Recurso = None):
        self.__Computador = Computador
        self.__Recurso = Recurso

    @property
    def Computador(self):
        return self.__Computador
    @property
    def Recurso(self):
        return self.__Recurso
    @Computador.setter
    def Computador(self, newComputador):
        self.__Computador = newComputador
    @Recurso.setter
    def Recurso(self, newRecurso):
        self.__Recurso = newRecurso

    def __str__(self):        
        if self.__Computador == None or self.__Recurso == None:
            raise JobException('Faltando argumentos: Computador e/ou Recurso.')
        elif self.__Recurso.name == None or self.__Recurso.size == 0:
            return 'Faltando atributos para o Recurso.'
        return f'{self.__Computador} | {self.__Recurso}'

# job = Job(Computador(1), Recurso('a', 1))

