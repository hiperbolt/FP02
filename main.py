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
    def __init__(self, tipo, especie, freq_reprod, freq_alim, idade=0, fome=0) -> None:
        self.tipo = tipo
        self.especie = especie
        self.idade = idade
        self.freq_reprod = freq_reprod
        self.fome = fome
        self.freq_alim = freq_alim
   
    def __repr__(self) -> str:
        return str(
            {
            "tipo" : self.tipo,
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
    return f"{a.especie} [{a.idade}/{a.freq_reprod};{a.fome}/{a.freq_alim}]"
    
###
#   Transformadores
###
def eh_animal_fertil(a: animal) -> bool:
    '''
        TODO : Descrição
    '''
    if a.idade >= a.freq_reprod:
        return True
    return False

def eh_animal_faminto(a: animal) -> bool:
    '''
        TODO
    '''
    if a.fome >= a.freq_alim:
        return True
    return False

def reproduz_animal(a: animal) -> animal:
    '''
        TODO
    '''
    a.idade = 0
    return animal(a.tipo, a.especie)


###
#   TAD posicao
#
#   O TAD posicao é usado para representar uma posição (x; y) de um prado arbitrariamente
#   grande, sendo x e y dois valores inteiros não negativos.
#
#   Representação interna: posicao = (x,y) -> Lista de dois ints
###

class prado:
    '''
        TODO
    '''
    def __init__(self, cantInfDirPos, obs, animais, posAnimais) -> None:
        '''
         x,y = n colunas, n linhas do prado. (x,y) representa a pos do canto
               inferior direito do prado

        e.g:
            P = (11,4)
            +----------+
            |..........|
            |..........|
            |.........P|
            +----------+

            A representação interna do prado ignora a moldura.

        '''
        # Conservamos o input original no caso de ser útil
        self.input_cantInfDirPos = cantInfDirPos
        self.input_obs = obs
        self.input_animais = animais
        self.input_posAnimais = posAnimais

        # Representação interna
        # A rep. int. ignora a moldura pelo que tem valores x,y ligeiramente diferentes
        # Isto é tido em conta sempre que o TAD é acedido exteriormente.
        self.x = cantInfDirPos.x - 2
        self.y = cantInfDirPos.y - 2
        self.obs = list(map(lambda x: (x.x-1,x.y-1), obs))
        
        posAnimaisTransf = list(map(lambda x: (x.x-1,x.y-1), posAnimais))
        self.animais = dict(zip(posAnimaisTransf, animais))

    def generate_repr_interna(self):
        self.repr = []

        for i in range(self.y+1):
            linha = []
            for j in range(self.x+1):
                linha.append(".")
            self.repr.append(linha)

        for o in self.obs:
                self.repr[o[1]][o[0]] = "@"

        for key in self.animais:
            self.repr[key[1]][key[0]] = animal_para_char(self.animais[key])

    def __repr__(self) -> str:
        return str(self.repr)
    
    def __eq__(self, other): 
        if (self.x, self.y, self.obs, self.animais) == (other.x, other.y, other.obs, other.animais):
            return True
        return False



###
#   Construtor
###
def cria_prado(d: posicao, r: tuple, a:tuple, p:tuple) -> prado:
    '''
        d: lower right corner pos
        r: tuplo de posiçoes dos rochedos
        a: tuplo de animais
        p: tuplo de posiçoes desses animais
    '''
    if isinstance(d, posicao) and isinstance(r, tuple) and isinstance(a, tuple) and isinstance(p, tuple):
        if all(isinstance(i, animal) for i in a) and all(isinstance(i, posicao) for i in p):
                if len(p) == len(a):
                    if len(r) == 0 or all(isinstance(i, posicao) for i in r):
                        # TODO: Garantir que esta arg check esta funcional
                        pRes = prado(d, r, a, p)
                        return pRes


    return ValueError('cria_prado: argumentos invalidos')

def cria_copia_prado(m: prado) -> prado:
    '''
        TODO
    '''
    return cria_prado(m.input_cantInfDirPos, m.input_obs, m.input_animais, m.input_posAnimais)


###
#   Seletores
###
def obter_tamanho_x(m: prado) -> int:
    '''
        TODO
    '''
    return m.input_cantInfDirPos.x + 1

def obter_tamanho_y(m: prado) -> int:
    '''
        TODO
    '''
    return m.input_cantInfDirPos.y + 1

def obter_numero_predadores(m: prado) -> int:
    '''
        TODO
    '''
    return int(reduce(lambda c,obj: c+1 if (obj.tipo == "predador") else c, m.input_animais, 0))

def obter_numero_presas(m: prado) -> int:
    '''
        TODO
    '''
    return int(reduce(lambda x,y: x+1 if (y.tipo == 'presa') else x, m.input_animais, 0))

def obter_posicao_animais(m: prado) -> tuple:
    '''
        TODO
    '''
    listaPosAnimais = list(m.input_posAnimais)
    ## FIXME: Isto provavelmente não funciona para todos os casos ... 
    for i in range(len(listaPosAnimais)):
        for j in range(len(listaPosAnimais)-1):
            if listaPosAnimais[j].x > listaPosAnimais[j+1].x:
                listaPosAnimais[j], listaPosAnimais[j+1] = listaPosAnimais[j+1], listaPosAnimais[j]

    for i in range(len(listaPosAnimais)):
        for j in range(len(listaPosAnimais)-1):
            if listaPosAnimais[j].y > listaPosAnimais[j+1].y:
                listaPosAnimais[j], listaPosAnimais[j+1] = listaPosAnimais[j+1], listaPosAnimais[j]

    return tuple(listaPosAnimais) 

def obter_animal(m: prado, p: posicao) -> animal:
    '''
        TODO
    '''
    return m.animais[(p.x-1, p.y-1)]


###
#    Modificadores
###

def eliminar_animal(m: prado, p: posicao) -> prado:
    '''
        TODO
    '''
    del m.animais[(p.x-1, p.y-1)]
    return m

def mover_animal(m: prado, p1: posicao, p2: posicao) -> prado:
    '''
        TODO
    '''
    m.animais[(p2.x-1, p2.y-1)] = m.animais[(p.x-1, p.y-1)]
    del m.animais[(p1.x-1, p1.y-1)]
    return m

def inserir_animal(m: prado, a: animal, p: posicao) -> prado:
    '''
        TODO
    '''
    m.animais[(p.x-1, p.y-1)] = a
    return m


###
#    Reconhecedores
###

def eh_prado(arg) -> bool:
    '''
        TODO
    '''
    if isinstance(arg, prado):
        return True

    return False

def eh_posicao_animal(m: prado, p: posicao) -> bool:
    '''
        TODO
    '''
    if (p.x-1, p.y-1) in m.animais:
        return True
    
    return False

def eh_posicao_obstaculo(m: prado, p: posicao) -> bool:
    '''
        TODO
    '''
    if (p.x-1, p.y-1) in m.obs:
        return True

    return False

def eh_posicao_livre(m: prado, p: posicao) -> bool:
    '''
        TODO
    '''
    if (p.x-1, p.y-1) not in m.animais and (p.x-1, p.y-1) not in m.obs:
        return True

    return False

###
#    Teste
###

def prados_iguais(p1: prado, p2: prado) -> bool:
    '''
        TODO
    '''
    return p1 == p2

###
#    Transformador
###

def prado_para_str(m: prado) -> str:
    '''
        TODO
    '''
    m.generate_repr_interna()

    res = ""

    res += "+"
    for i in range(m.x+1):
        res += "-"
    res += "+\n"

    for l in m.repr:
        res += "|"
        res += ''.join(l)
        res += "|"
        res += "\n"
    
    res += "+"
    for i in range(m.x+1):
        res += "-"
    res += "+\n"

    return res


###
#    Funções Alto Nível
###
    















obs = (cria_posicao(4,2), cria_posicao(10,1), cria_posicao(5,2))
anpos = tuple(cria_posicao(p[0], p[1]) for p in ((5,1), (7,2), (10,1), (6,1)))
an2 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an1 = (cria_animal('lynx', 20, 15), ) 
an = an2+an1
p = cria_prado(cria_posicao(11,4), obs, an, anpos)
print(obter_tamanho_x(p), obter_tamanho_y(p))
print(prado_para_str(p))