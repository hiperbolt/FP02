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
        return str((self.x, self.y))

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
        devolve um tuplo com as posiç~oes adjacentes à posição
        p, começando pela posição acima de p e seguindo no sentido horário.
    '''
    ### POR IMPLEMENTAR!!!

def ordenar_posicoes(t: tuple) -> tuple:
    '''
        devolve um tuplo contendo as mesmas posições do tuplo fornecido
        como argumento, ordenadas de acordo com a ordem de leitura do prado.
    '''
    #### POR IMPLEMENTAR!!!

###
#   TAD animal
#
#   O TAD animal é usado para representar os animais do simulador de ecossistemas que
#    habitam o prado, existindo de dois tipos: predadores e presas. Os predadores s~ao caracterizados
#    pela espécie, idade, frequ^encia de reprodução, fome e frequ^encia de alimentação.
#    As presas s~ao apenas caracterizadas pela espécie, idade e frequ^encia de reprodução.
#
#   Representação interna: posicao = (x,y) -> Lista de dois ints
###

class animal:
    def __init__(self, tipo, especie=None, idade=None, freq_reprod=None, fome=None, freq_alim=None) -> None:
        self.tipo = tipo
        self.especie = especie
        self.idade = idade
        self.freq_reprod = freq_reprod
        self.fome = fome
        self.freq_alim = freq_alim
   
    def __repr__(self) -> str:
        return str(
            {
            "especie" : self.especie,
            "idade": self.idade,
            "freq_reprod" : self.freq_reprod,
            "fome" : self.fome,
            "freq_alim" : self.freq_alim
            }
        )
    
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

    

###
#   Construtor
###
def cria_animal(s: str, r:int, a:int) -> animal:
    '''
        cria_animal(s, r, a) recebe uma string não vazia s
        s = espécie
        r = freq reprod
        a = freq alim

        TODO
    '''
    if isinstance(s, str) and s:
        if isinstance(r, int) and r > 0:
            if isinstance(a, int) and a >= 0:
                if a > 0:
                    return animal("predador", especie=s, freq_reprod=r, freq_alim=a)
                return animal("presa", especie=s, freq_reprod=r, freq_alim=0)

    raise ValueError("cria_animal: argumentos invalidos")

def cria_copia_animal(a: animal) -> animal:
    '''
        TODO : Descrição
        Garantimos que estamos a criar deep copy do objeto
    '''
    res = animal(a.tipo)
    res.tipo = a.tipo
    res.especie = a.especie
    res.idade = a.idade
    res.freq_reprod = a.freq_reprod
    res.fome = a.fome
    res.freq_alim = a.freq_alim
    return(res)
    

###
#   Seletores
###
def obter_especie(a: animal) -> str:
    '''
        TODO : descrição
    '''
    return str(a.especie)

def obter_freq_reprod(a: animal) -> int:
    '''
        obter_freq_reprod(a) devolve a freq_reprod do animal a.
    '''
    return int(a.freq_reprod)

def obter_freq_aliment(a: animal) -> int:
    '''
        obter_freq_aliment(a) devolve a freq_aliment do animal a.
    '''
    return int(a.freq_aliment)

def obter_idade(a: animal) -> int:
    '''
        obter_idade(a) devolve a idade do animal a.
    '''
    return int(a.idade)
 
def obter_fome(a: animal) -> int:
    '''
        obter_fome(a) devolve a fome do animal a.
    '''
    return int(a.fome)

    
###
#   Modificadores
###
def aumenta_idade(a: animal) -> animal:
    '''
        TODO
    '''
    a.idade += 1
    return a

def reset_idade(a: animal) -> animal:
    '''
        TODO
    '''
    a.idade = 0
    return a

def aumenta_fome(a: animal) -> animal:
    '''
        TODO
    '''
    a.fome += 1
    return a

def reset_fome(a: animal) -> animal:
    '''
        TODO
    '''
    a.fome = 0
    return a


###
#   Reconhecedor
###
def eh_animal(arg) -> bool:
    '''
        TODO : FIX ME!!!!
    '''
    pass

def eh_predador(arg) -> bool:
    if eh_animal(arg):
        if arg.tipo == "predador":
            return True
    
    return False

def eh_presa(arg) -> bool:
    if eh_animal(arg):
        if arg.tipo == "presa":
            return True

    return False


###
#   Teste
###
def animais_iguais(a1: animal, a2: animal) -> bool:
    '''
        TODO : DESCRIÇÃO
    ''' 
    if a1 == a2:
        return True
    return False


###
#   Transformadores
###
def animal_para_char(a: animal) -> str:
    '''
        TODO : descrição
    '''
    res = str(a.especie)[0]

    if a.tipo == "predador":
        return res.upper()
    else:
        return res.lower()
    
def animal_para_str(a: animal) -> str:
    '''
        TODO : DESCRIÇÃO
    '''
    return f"{a.especie} [{a.freq_reprod}/20;{a.freq_alim}/10]"
    
