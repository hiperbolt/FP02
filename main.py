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

    def __str__(self):
        return f"({self.x}, {self.y})"


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
