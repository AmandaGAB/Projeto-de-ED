class RecException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Recurso:
    def __init__(self, name = None, size = 0):
        self.__name = name
        self.__size = size
   
    @property
    def name(self):
        return self.__name
    @property
    def size(self):
        return self.__size
    @name.setter
    def name(self, newName):
        self.__name = newName
    @size.setter
    def size(self, newSize):
        self.__size = newSize

    def __str__(self):
        if self.__name == None or self.__size == 0:
            return 'Defina um nome e/ou tamanho para o recurso.'
        return f'Recurso: {self.__name} & Tamanho: {self.__size} Mb'


# def recursoCadastrado(lista, nome):
# 	for i in lista:
# 		if i.name == nome:
# 			return True
# 		False

# def criarRecurso(nome, tamanho):
# 	r = Recurso(nome, tamanho)
# 	return r


# r1 = Recurso('arquivo1', 100)
# recursos = [r1]
# r2 = Recurso('arquivo2', 200)
# r3 = Recurso('arquivo3', 300)
# r4 = Recurso('arquivo4', 400)