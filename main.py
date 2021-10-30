###
#    Projeto 2 de Fundamentos da Programação
#    Tomás Simões ist1102416
###

from functools import reduce


###
#   TAD posicao
#
#   O TAD posicao é usado para representar uma posição (x; y) de um prado arbitrariamente
#   grande, sendo x e y dois valores inteiros não negativos.
#
#   Representação interna: posicao = (x,y) -> Lista de dois ints
###

class posicao:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__


###
#    Construtores
###

def cria_posicao(x: int, y: int) -> posicao:
    '''
        Recebe os valores correspondentes às coordenadas de uma
        posição e devolve a posição correspondente. O construtor verifica a validade
        dos seus argumentos, gerando um ValueError.
    '''
    if isinstance(x, int) and isinstance(y, int):
        if x > 0 and y > 0:
            return posicao(x, y)
    
    raise ValueError("cria_posicao: argumentos invalidos")

def cria_copia_posicao(p: posicao) -> posicao:
    '''
        Recebe uma posição p e devolve uma cópia nova da posição.
    '''
    return posicao(p.x, p.y)


###
#   Seletores
###

def obter_pos_x(p: posicao) -> int:
    '''
        Devolve a componente x da posição p
    '''
    return p.x

def obter_pos_y(p: posicao) -> int:
    '''
        Devolve a componente y da posição p
    '''
    return p.y


###
#   Reconhecedor
###

def eh_posicao(arg) -> bool:
    '''
        Devolve True caso o seu argumento seja um TAD posicao e
        False caso contrário.
    '''
    ## POR IMPLEMENTAR!!!!


###
#   Teste
###

def posicoes_iguais(p1: posicao, p2: posicao) -> bool:
    '''
        devolve True apenas se p1 e p2 são posições e são
        iguais.
    '''
    if p1 == p2:
        return True
    return False


###
#   Transformador
###
def posicao_para_str(p: posicao) -> str:
    '''
        Devolve a cadeia de caracteres `(x, y)' que representa o
        seu argumento, sendo os valores x e y as coordenadas de p.
    '''

    return str(p)

###
#   Funções de alto nível
###

def obter_posicoes_adjacentes(p: posicao) -> tuple:
    '''
        devolve um tuplo com as posic~oes adjacentes a posic~ao
        p, comecando pela posic~ao acima de p e seguindo no sentido horario.
    '''
    ### POR IMPLEMENTAR!!!

def ordenar_posicoes(t: tuple) -> tuple:
    '''
        devolve um tuplo contendo as mesmas posic~oes do tuplo fornecido
        como argumento, ordenadas de acordo com a ordem de leitura do prado.
    '''
    #### POR IMPLEMENTAR!!!

###
#   TAD animal
#
#   O TAD animal e usado para representar os animais do simulador de ecossistemas que
#    habitam o prado, existindo de dois tipos: predadores e presas. Os predadores s~ao caracterizados
#    pela especie, idade, frequ^encia de reproduc~ao, fome e frequ^encia de alimentac~ao.
#    As presas s~ao apenas caracterizadas pela especie, idade e frequ^encia de reproduc~ao.
#
#   Representação interna: posicao = (x,y) -> Lista de dois ints
###

class animal:
    def __init__(self) -> None:
        pass