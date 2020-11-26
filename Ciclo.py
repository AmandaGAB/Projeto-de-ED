class CicloException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


'''
Classe que representa um nó na memória
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def insertNext(self, data):
        if self.next == None:
            self.next = Node(data)	

    def getNext(self):
        return self.next

    def setData(self,newValue):
        self.data = newValue

    def getData(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        return self.next != None


class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class ValorInexistenteException(Exception):
    def __init__(self,msg):
        super().__init__(msg)         
	    
'''
Esta classe implementa uma estrutura Lista Simplesmente Encadeada
'''
class Ciclo:
    # constructor initializes an empty ListaEncadeada of integers
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        return True if self.__tamanho ==0 else False

    def tamanho(self):
        return self.__tamanho

    def elemento(self, posicao):

        try:
            assert posicao > 0

            if (self.estaVazia()):
                raise PosicaoInvalidaException(f'Lista vazia')

            cursor = self.__head
            contador = 1
            while( (cursor != None) and (contador < posicao) ):
                cursor = cursor.next
                contador += 1

            if ( cursor != None ):
                return cursor.data
        
            raise PosicaoInvalidaException(f'A lista não contém {posicao} elementos. O máximo é {self.__tamanho}')

        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser 0 (zero) ou um número negativo')
        except:
            raise


    def modificar(self, posicao, valor):
 
        try:
            assert posicao > 0

            if (self.estaVazia()):
                raise PosicaoInvalidaException(f'Lista vazia')

            cursor = self.__head
            contador = 1
            while( (cursor != None) and (contador < posicao) ):
                cursor = cursor.next
                contador += 1

            if ( cursor != None ):
                cursor.data = valor
                return
        
            raise PosicaoInvalidaException(f'A lista não contém {posicao} elementos. O máximo é {self.__tamanho}')


        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser 0 (zero) ou um número negativo')
        except:
            raise      
    
    def busca(self, valor):
        if (self.estaVazia()):
            raise PosicaoInvalidaException(f'Lista vazia')

        cursor = self.__head
        contador = 1

        while( cursor != None ):
            if( cursor.data == valor):
                return contador
            cursor = cursor.next
            contador += 1
            
        raise ValorInexistenteException(f'O valor {valor} não está armazenado na lista')

    def inserir(self, posicao, valor):

        try:
            assert posicao > 0

            
            # CONDICAO 1: insercao se a lista estiver vazia
            
            if (self.estaVazia()):
                if ( posicao != 1):
                    print('Entrei no posicao = 1')
                    raise PosicaoInvalidaException(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = Node(valor)
                self.__head.next = self.__head
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia

            if posicao == 1:
                novo = Node(valor)
                if self.__tamanho <=0:
                    self.__head = novo
                    novo.next = self.__head
                else:
                    no = self.__head
                    while no.next!=self.__head:
                        no = no.next
                    no.next = novo
                    novo.next = self.__head
                    self.__head = novo
                self.__tamanho += 1
                return


            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            if posicao > self.__tamanho+1:
                raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')
            cursor = self.__head
            contador = 1

            while (contador < posicao-1):
                cursor = cursor.next
                contador += 1

                
            novo = Node(valor)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo ou 0 (zero)')
        except:
            raise


    def remover(self, posicao):
 
        try:
            assert posicao > 0

            if posicao == 1 and self.__tamanho ==1:
                self.__head = None
                self.__tamanho-=1
                return
               

            if( self.estaVazia() ):
                raise PosicaoInvalidaException(f'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            if ( posicao > self.__tamanho ):
                raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')

            anterior = self.__head

            while anterior.next!=self.__head:
                anterior = anterior.next

            while(contador <= posicao-1):
                anterior = cursor
                cursor = cursor.next
                contador+=1

            data = cursor.data

            anterior.next = cursor.next

            if( posicao == 1):
                self.__head = anterior.next 

            self.__tamanho -= 1

            return data
        
        except TypeError:
            raise PosicaoInvalidaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise


    def imprimir(self):
        
        print(f'----------JOBS INSERIDOS----------\n')
       
        cont=1
        cursor = self.__head
    
        while( cursor.next != self.__head ):
            
            print(f'{cont}', f' - {cursor.data}', end='')
            cursor = cursor.next
            cont+=1
            print('\n', end='')
        print(f'{cont}', f' - {cursor.data}', end='')
        print('\n')
      
        
        
        

        
    def __str__(self):

        str = 'Lista: [ '

        cursor = self.__head

        while( cursor != None ):
            str += f'{cursor.data}'
            cursor = cursor.next
            if (cursor != None):
                str += ', '
        str += ']'
        return str
