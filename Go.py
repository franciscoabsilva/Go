'''
O TAD interseção é usado para representar uma interseção do tabuleiro de Go.

-Cada interseção é representada sobre forma de tuplo com a coluna e a linha da interseção.
'''

def cria_intersecao(col, lin):
    '''
    cria_intersecao: str x int → intersecao

    Esta função recebe um caracter e um inteiro correspondentes à coluna e à linha e devolve
    a interseção correspondente em forma de lista. 
    '''

    # Verifica que a coluna é válida
    if not isinstance(col, str) or not len(col) == 1 or not ('A' <= col <= 'S'):
        raise ValueError("cria_intersecao: argumentos invalidos")
    
    # Verifica que a linha é válida
    if not isinstance(lin, int) or isinstance(lin, bool) or not lin in range(1,20):
        raise ValueError("cria_intersecao: argumentos invalidos")
    
    return (col, lin)

def obtem_col(i):
    '''
    obtem_col: intersecao → str

    Esta função recebe uma interseção e devolve a coluna dessa interseção.
    '''

    return i[0]

def obtem_lin(i):
    '''
    obtem_lin: intersecao → int

    Esta função recebe uma interseção e devolve a linha dessa interseção.
    '''

    return i[1]

def eh_intersecao(arg):
    '''
    eh_intersecao: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD intersecao e False caso contrário.
    '''

    # Verifica que o formato do argumento está correto
    if not isinstance(arg, tuple) or not len(arg) == 2:
        return False
    
    # Verifica que a letra existiria em algum tabuleiro
    if not isinstance(obtem_col(arg), str) or not len(obtem_col(arg)) == 1 or not ('A' <= obtem_col(arg) <= 'S'):
        return False
    
    # Verifica que o número existiria em algum tabuleiro
    if not isinstance(obtem_lin(arg),int) or isinstance(obtem_lin(arg),bool) or not obtem_lin(arg) in range(1,20):
        return False
    
    return True

def intersecoes_iguais(i1, i2):
    '''
    intersecoes_iguais: universal x universal → booleano

    Esta função devolve True se os seus dois argumentos são interseções e são iguais e False caso contrário.
    '''

    if not eh_intersecao(i1) or not eh_intersecao(i2):
        return False
    
    return obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2)

def intersecao_para_str(i):
    '''
    intersecao_para_str: intersecao → str

    Esta função devolve a cadeia de caracteres que representa o seu argumento.
    '''

    return f"{obtem_col(i)}{obtem_lin(i)}"

def str_para_intersecao(s):
    '''
    str_para_intersecao: str → intersecao

    Esta função devolve a interseção representada pelo seu argumento.
    '''
    col = s[0]
    lin = int(s[1:])

    return cria_intersecao(col, lin)

def obtem_intersecoes_adjacentes(i, l):
    '''
    obtem_intersecoes_adjacentes: intersecao x intersecao → tuplo
    
    Esta função devolve um tuplo com as interseções adjacentes à interseção i de acordo com
    a ordem de leitura em que l corresponde à interseção superior direita do tabuleiro de Go.
    '''

    col = obtem_col(i)
    lin = obtem_lin(i)
    intersecoes_adjacentes = ()

    if lin > 1:
        intersecoes_adjacentes += cria_intersecao(col , lin-1), # Interseção abaixo
    if not col == 'A':
        intersecoes_adjacentes += cria_intersecao(chr(ord(col)-1), lin), # Interseção à esquerda 
    if not col == obtem_col(l):
        intersecoes_adjacentes += cria_intersecao(chr(ord(col)+1), lin), # Interseção à direita
    if lin < obtem_lin(l):
        intersecoes_adjacentes += cria_intersecao(col , lin+1), # Interseção acima

    return intersecoes_adjacentes

def ordena_intersecoes(t):
    '''
    ordena_intersecoes: tuplo → tuplo
    
    Esta função devolve um tuplo de interseções com as mesmas interseções de t ordenadas
    de acordo com a ordem de leitura do tabuleiro de Go.
    '''

    # Ordena pela linha e em caso de igualdade pela coluna
    return tuple(sorted(t, key=lambda i: (obtem_lin(i), obtem_col(i))))

'''
O TAD pedra é usado para representar as pedras do Go. 
As pedras podem pertencer ao jogador branco ou ao jogador preto ou serem
pedras neutras caso a interseção não pertença a nenhum jogador.

-Uma pedra branca é representada pelo caracter 'O'
-Uma pedra preta é representada pelo caracter 'X'
-Uma pedra neutra é representada pelo caracter '.'
'''

def cria_pedra_branca():
    '''
    cria_pedra_branca: {} → pedra
    
    Esta função devolve uma pedra pertencente ao jogador branco.
    '''
    
    return 'O'

def cria_pedra_preta():
    '''
    cria_pedra_preta: {} → pedra
    
    Esta função devolve uma pedra pertencente ao jogador preto.
    '''

    return 'X'

def cria_pedra_neutra():
    '''
    cria_pedra_neutra: {} → pedra
    
    Esta função devolve uma pedra neutra.
    '''

    return '.'

def eh_pedra(arg):
    '''
    eh_pedra: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD pedra e False caso contrário.
    '''

    return arg in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra())

def eh_pedra_branca(p):
    '''
    eh_pedra_branca: pedra → booleano

    Esta função devolve True caso a pedra p seja do jogador branco e False caso contrário.
    '''

    return p == cria_pedra_branca()

def eh_pedra_preta(p):
    '''
    eh_pedra_preta: pedra → booleano

    Esta função devolve True caso a pedra p seja do jogador preto e False caso contrário.
    '''

    return p == cria_pedra_preta()

def pedras_iguais(p1, p2):
    '''
    pedras_iguais: universal x universal → booleano

    Esta função devolve True apenas se p1 e p2 são pedras e são iguais. 
    '''

    if not eh_pedra(p1) or not eh_pedra(p2):
        return False

    return eh_pedra_branca(p1) and eh_pedra_branca(p2) or eh_pedra_preta(p1) and eh_pedra_preta(p2) or not eh_pedra_jogador(p1) and not eh_pedra_jogador(p2)

def pedra_para_str(p):
    '''
    pedra_para_str: pedra → str

    Esta função devolve a cadeia de caracteres que representa o jogador dono da pedra, isto  ́e,
    'O', 'X' ou '.' para pedras do jogador branco, preto ou neutra respetivamente.
    '''

    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p):
        return 'X'
    else:
        return '.'

def eh_pedra_jogador(p):
    '''
    eh_pedra_jogador: pedra → booleano

    Esta função devolve True caso a pedra p seja de um jogador e False caso contrário.
    '''

    return eh_pedra_branca(p) or eh_pedra_preta(p)

'''
O TAD goban é usado para representar um tabuleiro do jogo Go e as pedras dos jogadores
que nele são colocadas.

-Cada goban é representado por uma lista de listas de interseções onde cada uma das listas (dentro da lista que
representa o goban) representa uma coluna do tabuleiro.
'''

def cria_goban_vazio(n):
    '''
    cria goban vazio: int → goban

    Esta função devolve um goban de tamanho nxn, sem interseções ocupadas.
    '''

    # Verifica o argumento
    if not n in (9, 13, 19) or not isinstance(n, int):
        raise ValueError("cria_goban_vazio: argumento invalido")
    
    goban = []

    # Adiciona ao goban n colunas com n pedras neutras
    for coluna in range(n):
        goban += [[cria_pedra_neutra()] * n]

    return goban

def cria_goban(n, ib, ip):
    '''
    cria_goban: int x tuplo x tuplo → goban

    Esta função devolve um goban de tamanho nxn, com as interseções do tuplo ib ocupadas por pedras brancas
    e as interseções do tuplo ip ocupadas por pedras pretas.
    '''
    
    # Verifica o tamanho do tabuleiro e que ib e ip são tuplos
    if not n in (9, 13, 19) or not isinstance(n, int) or not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError("cria_goban: argumentos invalidos")
    
    # Verifica que duas pedras diferentes não estão na mesma interseção
    for intersecao in ib:
        if intersecao in ip:
            raise ValueError("cria_goban: argumentos invalidos")

    # Cria o goban
    goban = cria_goban_vazio(n)
    
    # Verifica os elementos dos tuplos ib e ip são intercesões e não se repetem
    for tuplo in (ib, ip):
        for intersecao in tuplo:
            if not eh_intersecao(intersecao) or not eh_intersecao_valida(goban, intersecao):
                raise ValueError("cria_goban: argumentos invalidos")
        for posicao_intercesao1 in range(len(tuplo)):
            for posicao_intercesao2 in range(posicao_intercesao1 + 1, len(tuplo)):
                if tuplo[posicao_intercesao1] == tuplo[posicao_intercesao2]:
                    raise ValueError("cria_goban: argumentos invalidos")

    # Adiciona ao goban as respectivas pedras
    for intersecao in ib:
        goban[ord(obtem_col(intersecao))-ord("A")][obtem_lin(intersecao)-1] = cria_pedra_branca()
    for intersecao in ip:
        goban[ord(obtem_col(intersecao))-ord("A")][obtem_lin(intersecao)-1] = cria_pedra_preta()

    return goban

def cria_copia_goban(t):
    '''
    cria_copia_goban: goban → goban
    
    Esta função recebe um goban e devolve uma cópia do goban.
    '''

    copia = []

    for coluna in t:
        nova_coluna = coluna[:]
        copia += [nova_coluna]

    return copia

def obtem_ultima_intersecao(g):
    '''
    obtem_ultima_intersecao: goban → intersecao
    
    Esta função recebe um goban e devolve a interseção correspondente ao canto superior direito do goban.
    '''

    col = chr(len(g)+ord("A")-1)
    lin = len(g)

    return cria_intersecao(col, lin)

def obtem_pedra(g, i):
    '''
    obtem_pedra: goban x intersecao → pedra
    
    Esta função recebe um goban e uma interseção e devolve a pedra na interseção do goban.
    Se a posição não estiver ocupada, devolve uma pedra neutra.
    '''

    valor_da_pedra = g[ord(obtem_col(i))-ord("A")][obtem_lin(i)-1]

    if eh_pedra_branca(valor_da_pedra):
        return cria_pedra_branca()
    if eh_pedra_preta(valor_da_pedra):
        return cria_pedra_preta()
    else:
        return cria_pedra_neutra()

def obtem_cadeia(g, i):
    '''
    obtem_cadeia: goban x intersecao → tuplo
    
    Esta função recebe um goban e uma interseção e devolve um tuplo formado pelas interseções 
    (em ordem de leitura) das pedras da cadeia que passa pela interseção. 
    Se a posição não estiver ocupada, devolve a cadeia de posições livres.
    '''

    def cadeia(g,i,tup):
        '''
        cadeia: goban x intersecao x tuplo de interseções → tuplo

        Esta função recursiva encontra as interseções adjacentes com o mesmo valor da interseção recebida.
        Depois as adjacentes com o mesmo valor dessas interseções e assim successivamente até que todas as
        interseçoes da cadeia estejam contabilizadas. Ela devolve um tuplo formado por todas essas interseções.
        '''

        for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):

            # Descobre a pedra da adjacente
            if eh_pedra_branca(obtem_pedra(g, adjacente)):
                valor_intersecao_adjacente = cria_pedra_branca()
            elif eh_pedra_preta(obtem_pedra(g, adjacente)):
                valor_intersecao_adjacente = cria_pedra_preta()
            else:
                valor_intersecao_adjacente = cria_pedra_neutra()
            
            # Se a pedra da adjacente e da intercesão forem iguais e a adjacente não estiver no tuplo, adiciona-a
            if pedras_iguais(valor_intersecao_base, valor_intersecao_adjacente) and not adjacente in tup:
                tup += adjacente,
                tup = cadeia(g, adjacente, tup)
        
        return tup
    
    # Este tuplo vai conter todas as interseções da cadeia
    tup=(i),

    # Descobre a pedra da interseção
    if eh_pedra_branca(obtem_pedra(g, i)):
        valor_intersecao_base = cria_pedra_branca()
    elif eh_pedra_preta(obtem_pedra(g, i)):
        valor_intersecao_base = cria_pedra_preta()
    else:
        valor_intersecao_base = cria_pedra_neutra()

    return ordena_intersecoes(cadeia(g, i, tup))

def coloca_pedra(g, i, p):
    '''
    coloca_pedra: goban x intersecao x pedra → goban

    Esta função modifica destrutivamente o goban g colocando a pedra do jogador p na interseção i,
    e devolve o próprio goban.
    '''
    
    col = ord(obtem_col(i))-ord("A")
    lin = obtem_lin(i)-1

    g[col][lin] = p

    return g

def remove_pedra(g, i):
    '''
    remove_pedra: goban x intersecao → goban

    Esta função modifica destrutivamente o goban g removendo a pedra
    da interseção i, e devolve o próprio goban.
    '''

    return coloca_pedra(g, i, cria_pedra_neutra())

def remove_cadeia(g, t):
    '''
    remove_cadeia: goban x tuplo → goban

    Esta função modifica destrutivamente o goban g removendo as pedras nas interseções to tuplo t,
    e devolve o próprio goban.
    '''
    
    for intersecao in t:
        g = remove_pedra(g, intersecao)

    return g

def eh_goban(arg):
    '''
    eh_goban: universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD goban e False caso contrário.
    '''

    # Verifica se o argumento tem um tamanho
    try:
        tamanho_goban = obtem_lin(obtem_ultima_intersecao(arg))
    except (TypeError, ValueError):
        return False

    # Verifica se o formato do argumento está correto
    if not tamanho_goban in (9, 13, 19) or not type(arg) == type(cria_goban_vazio(tamanho_goban)):
        return False
    
    for coluna in arg:
        # Verifica se cada coluna está correta
        if not type(coluna) == type(cria_goban_vazio(tamanho_goban)[0]) or not len(coluna) == tamanho_goban:
            return False
        for intersecao in coluna:
            # Verifica se cada interseção está correta
            if not eh_pedra(intersecao):
                return False
            
    return True

def eh_intersecao_valida(g, i):
    '''
    eh_intersecao_valida: goban x intersecao → booleano

    Esta função devolve True se i ́e uma interseção válida dentro do goban g e False caso contrário.
    '''

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g))

    # Verifica se a letra pertence ao goban
    if not ord(obtem_col(i))-ord("A")+1 in range(1, tamanho_goban +1): 
        return False
    
    # Verifica se o número pertence ao goban
    for coluna in g:
        if not obtem_lin(i) in range(1, tamanho_goban +1):
            return False
    
    return True

def gobans_iguais(g1, g2):
    '''
    gobans_iguais: universal x universal → booleano

    Esta função devolve True apenas se g1 e g2 forem gobans e forem iguais.
    '''

    if not eh_goban(g1) or not eh_goban(g2):
        return False 

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g1))

    # Verifica que os dois gobans têm o mesmo tamanho
    if not tamanho_goban == obtem_lin(obtem_ultima_intersecao(g2)):
        return False
    
    for linha in range(tamanho_goban):
        for coluna in range(tamanho_goban):
            col = chr(coluna + ord("A"))
            lin = linha+1
            intersecao = cria_intersecao(col,lin)
            # Verifica se cada interseção em g1 é igual em g2
            if not pedras_iguais(obtem_pedra(g1, intersecao), obtem_pedra(g2, intersecao)):
                return False
            
    return True

def goban_para_str(g):
    '''
    goban_para_str: goban → str

    Esta função recebe um goban e devolve a cadeia de caracteres que representa o goban.
    '''

    # Tamanho do goban
    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g))

    # Linha com letras das colunas inicial
    linha_das_colunas = "   "
    for coluna in range(tamanho_goban):
        linha_das_colunas += chr(coluna + ord("A")) + " "
    linha_das_colunas = linha_das_colunas[:-1] # Retira o espaço final
    str_goban = linha_das_colunas + "\n"

    # Linhas do Goban
    for linha in range(tamanho_goban, 0, -1):

        linha_goban = str(linha) # Número da linha

        if linha < 10:
            linha_goban = " " + linha_goban
        linha_goban += " " # Número da linha no início da linha

        for coluna in range(tamanho_goban):
            linha_goban += pedra_para_str(g[coluna][linha - 1]) + " " # Pedra

        if linha < 10:
            linha_goban += " "
        linha_goban += str(linha) + "\n" # Número da linha no final da linha
        
        str_goban += linha_goban

    # Linha com letras das colunas final
    str_goban += linha_das_colunas

    return str_goban

def obtem_territorios(g):
    '''
    obtem_territorios: goban → tuplo

    Esta função devolve o tuplo formado pelos tuplos com as interseções de cada território de g.
    A função devolve as interseções de cada território ordenadas em ordem de leitura do tabuleiro de Go,
    e os territórios ordenados em ordem de leitura da primeira interseção do território.
    '''

    def eh_intersecao_contabilizada(intersecao, territorios):
        '''
        eh_intersecao_contabilizada: intersecao x tuplo → booleano

        Esta função retorna True se a interseção já foi contabilizada em algum território
        e false caso contrário.
        '''

        for territorio in territorios:
            # Verifica se a interseção está em algum território
            if intersecao in territorio:
                return True
            
        return False
    
    territorios = ()

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g))

    for num_col in range(tamanho_goban):
        for num_lin in range(1, tamanho_goban + 1):
            col = chr(ord("A") + num_col)
            lin = num_lin
            intersecao = cria_intersecao(col, lin)
            # Se for um território não contabilizado, adiciona-o ao tuplo territórios
            if not eh_intersecao_contabilizada(intersecao, territorios) and not eh_pedra_jogador(obtem_pedra(g, intersecao)):
                territorios += (obtem_cadeia(g, intersecao)),

    # Organiza os territórios por ordem de leitura da primeira interseção do território
    return tuple(sorted(territorios, key=lambda territorio: (obtem_lin(territorio[0]), obtem_col(territorio[0]))))

def obtem_adjacentes_diferentes(g, t):
    '''
    obtem_adjacentes_diferentes: goban x tuplo → tuplo

    Esta função devolve o tuplo ordenado formado pelas interseções adjacentes às interseções do tuplo t:

    (a) livres, se as interseções do tuplo t estão ocupadas por pedras de jogador;
    
    (b) ocupadas por pedras de jogador, se as interseções do tuplo t estão livres.
    '''

    adjacentes_diferentes = ()

    for intersecao in t:
        adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))
        for adjacente in adjacentes:
            # Se a adjacente for diferente da interseção e a adjacente não estiver no resultado
            if not obtem_pedra(g, adjacente) == obtem_pedra(g, intersecao) and adjacente not in adjacentes_diferentes: 
                # Se a interseção tiver uma pedra de um jogador
                if eh_pedra_jogador(obtem_pedra(g, intersecao)):
                    # Se a adjacente for neutra
                    if not eh_pedra_jogador(obtem_pedra(g, adjacente)):
                            adjacentes_diferentes += (adjacente),
                else:
                    adjacentes_diferentes += (adjacente),
        
    return ordena_intersecoes(adjacentes_diferentes)

def jogada(g, i, p):
    '''
    jogada: goban x intersecao x pedra → goban

    Esta função modifica destrutivamente o goban g colocando a pedra do jogador p
    na interseção i e remove todas as pedras do jogador contrário pertencentes a
    cadeias adjacentes à i sem liberdades, devolvendo o próprio goban.
    '''
    
    # Coloca a pedra na interseção i
    coloca_pedra(g, i, p)
    
    # Obtém as pedras adversárias adjacentes à interseção i
    pedras_adversarias_adjacentes = []

    # Descobre a cor da pedra
    if eh_pedra_branca(p):
        pedra = cria_pedra_branca()
    if eh_pedra_preta(p):
        pedra = cria_pedra_preta()
    
    # Descobre as pedras adversárias adjacentes
    for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        pedra_adjacente = obtem_pedra(g, adjacente)
        if eh_pedra_jogador(pedra_adjacente):
            if eh_pedra_branca(pedra) and not eh_pedra_branca(pedra_adjacente):
                pedras_adversarias_adjacentes += [adjacente]
            elif eh_pedra_preta(pedra) and not eh_pedra_preta(pedra_adjacente):
                pedras_adversarias_adjacentes += [adjacente]

    # Remove pedras adversárias sem liberdades
    for adversaria in pedras_adversarias_adjacentes:
        if not tem_liberdades(g, adversaria):
            remove_cadeia(g, obtem_cadeia(g, adversaria))

    return g

def obtem_pedras_jogadores(g):
    '''
    obtem_pedras_jogadores: goban → tuplo

    Esta função devolve um tuplo de dois inteiros que correspondem ao número de interseções 
    ocupadas por pedras do jogador branco e preto, respetivamente.
    '''
    
    pedras_branco = 0
    pedras_preto = 0

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g))

    for num_col in range(tamanho_goban):
        for num_lin in range(1, tamanho_goban + 1):
            col = chr(ord("A") + num_col)
            lin = num_lin
            intersecao = cria_intersecao(col, lin)

            # Verifica a cor da pedra e contabiliza o ponto para o jogador
            if eh_pedra_branca(obtem_pedra(g, intersecao)):
                pedras_branco += 1
            elif eh_pedra_preta(obtem_pedra(g, intersecao)):
                pedras_preto += 1

    return (pedras_branco, pedras_preto)

# FUNÇÕES ADICIONAIS

def calcula_pontos(g):
    '''
    calcula_pontos: goban → tuple

    Esta função ́e uma função auxiliar que recebe um goban e devolve o tuplo de dois
    inteiros com as pontuações dos jogadores branco e preto, respetivamente.
    '''

    def obtem_adjacentes_cadeia(g, cadeia):
        '''
        obtem_adjacentes_cadeia: goban x cadeia → tuplo
        
        Esta função retorna um tuplo contendo todas as interseções adjacentes à cadeia.
        '''

        adjacentes = ()

        for intersecao in cadeia:
            intersecoes_adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(g))
            for adjacente in intersecoes_adjacentes:
                if adjacente not in cadeia and adjacente not in adjacentes:
                    adjacentes += (adjacente),

        return adjacentes

    pontos_branco, pontos_preto = obtem_pedras_jogadores(g)

    territorios = obtem_territorios(g)

    tamanho_goban = obtem_lin(obtem_ultima_intersecao(g))

    # Caso o goban esteja vazio 
    if g == cria_goban_vazio(tamanho_goban):
        return (0, 0)
    

    for territorio in territorios:
        adjacentes_territorio = obtem_adjacentes_cadeia(g, territorio)
        adjacentes_brancas = 0
        adjacentes_pretas = 0

        # Contagem da quantidade de adjacentes ao território da mesma cor
        for adjacente in adjacentes_territorio:
            if eh_pedra_branca(obtem_pedra(g, adjacente)):
                adjacentes_brancas += 1
            elif eh_pedra_preta(obtem_pedra(g, adjacente)):
                adjacentes_pretas += 1

        # Contabiliza os territórios pertencentes a cada jogador        
        if adjacentes_brancas == len(adjacentes_territorio):
            pontos_branco += len(territorio)
        elif adjacentes_pretas == len(adjacentes_territorio):
            pontos_preto += len(territorio)

    return (pontos_branco, pontos_preto)

def eh_jogada_legal(g, i, p, l):
    '''
    eh_jogada_legal: goban x intersecao x pedra x goban → booleano

    Esta função ́e uma função auxiliar que recebe um goban g, uma interseção
    i, uma pedra de jogador p e um outro goban l e devolve True se a jogada for legal ou
    False caso contrário, sem modificar g ou l.
    '''
    
    # Verifica se a interseção i é válida e vazia
    if not eh_intersecao_valida(g, i) or eh_pedra_jogador(obtem_pedra(g, i)):
        return False
    
    # Faz uma cópia do goban e realiza um jogada nessa cópia
    copia_goban = cria_copia_goban(g)
    jogada(copia_goban, i, p)

    # Verifica se a jogada cumpre a regra do suícidio e não repete o estado do goban
    if not tem_liberdades(copia_goban, i) or gobans_iguais(copia_goban, l):
        return False

    return True

def turno_jogador(g, p, l):
    '''
    turno_jogador: goban x pedra x goban → booleano

    Esta função é uma função auxiliar que oferece ao jogador que joga com pedras p
    a opção de passar a jogada ou de colocar uma pedra própria numa interseção.
    Se o jogador passar, a função devolve False sem modificar os argumentos.
    Se o jogador fizer uma jogada ilegal, ele terá que repetir a jogada até ser legal.
    Caso contrário, a função devolve True e modifica destrutivamente o tabuleiro g de acordo com a jogada realizada.
    '''
    
    pedra = pedra_para_str(p)

    while True: # Caso o input não seja a representação externa de uma intercesão do goban ou "P", repete o input
        jogada_realizada = input(f"Escreva uma intersecao ou 'P' para passar [{pedra}]:")

        if jogada_realizada == 'P':
            return False # O jogador passa a vez
        else:
            if str_intersecao_valida(jogada_realizada):
                jogada_realizada = str_para_intersecao(jogada_realizada)
                if eh_jogada_legal(g, jogada_realizada, p, l):
                    jogada(g, jogada_realizada, p)
                    return True # Se a jogada for legal, executa-a e passa a vez

def go(n, tb, tp):
    '''
    go: int x tuple x tuple → booleano

    Esta função permite jogar um jogo completo do Go de dois jogadores.
    A função recebe um inteiro correspondente à dimensão do tabuleiro, e dois
    tuplos (potencialmente vazios) com a representação externa das interseções ocupadas
    por pedras brancas (tb) e pretas (tp) inicialmente. A função devolve True se o jogador
    com pedras brancas conseguir ganhar o jogo, ou False caso contrário.
    '''

    def fazer_jogada(goban, pedra, ultimo_goban):
        '''
        fazer_jogada: goban x pedra x goban → booleano

        Esta função retorna True caso o jogador passe a jogada,
        caso contrário executa a jogada no goban e retorna False.
        '''

        pontuacao = calcula_pontos(goban)
        print(f'Branco (O) tem {pontuacao[0]} pontos')
        print(f'Preto (X) tem {pontuacao[1]} pontos')
        print(goban_para_str(goban))

        return not turno_jogador(goban, pedra, ultimo_goban) # Retorna se o jogador passou ou não

    # Verifica a validade dos argumentos
    if not n in (9, 13, 19) or not isinstance(n, int):
        raise ValueError('go: argumentos invalidos')

    if not isinstance(tb, tuple) or not isinstance(tp, tuple):
        raise ValueError('go: argumentos invalidos')

    # Transforma a representação externa em interseções se os argumentos forem válidos
    tbranco = ()
    tpreto = ()
    for intercesao in tb:
        if not str_intersecao_valida(intercesao) or not eh_intersecao_valida(cria_goban_vazio(n), str_para_intersecao(intercesao)) or str_para_intersecao(intercesao) in (tbranco, tpreto):
            raise ValueError('go: argumentos invalidos')
        tbranco += (str_para_intersecao(intercesao)),
    for intercesao in tp:
        if not str_intersecao_valida(intercesao) or not eh_intersecao_valida(cria_goban_vazio(n), str_para_intersecao(intercesao)) or str_para_intersecao(intercesao) in (tbranco, tpreto):
            raise ValueError('go: argumentos invalidos')
        tpreto += (str_para_intersecao(intercesao)),
    
    # Se os argumentos forem válidos cria o goban
    goban = cria_goban(n,tbranco,tpreto)

    
    # O jogo acaba quando estas duas variaveis valerem True
    branco_passou = False
    preto_passou = False

    # As duas variáveis ultimo_goban verificam que não se repete o estado do goban
    ultimo_goban_1 = cria_goban_vazio(n)

    # Enquanto não passarem os dois o jogo continua
    while True:
        # Jogada do preto
        ultimo_goban_2 = cria_copia_goban(goban)
        preto_passou = fazer_jogada(goban, cria_pedra_preta(), ultimo_goban_1)
        if preto_passou and branco_passou:
            break

        # Jogada do branco
        ultimo_goban_1 = cria_copia_goban(goban)
        branco_passou = fazer_jogada(goban, cria_pedra_branca(), ultimo_goban_2)
        if preto_passou and branco_passou:
            break
    
    # Mostra o tabuleiro e a pontuação final
    pontuacao = calcula_pontos(goban)
    print(f'Branco (O) tem {pontuacao[0]} pontos')
    print(f'Preto (X) tem {pontuacao[1]} pontos')
    print(goban_para_str(goban))

    return pontuacao[0] > pontuacao[1]

#FUNÇÕES EXTRA

def tem_liberdades(g, i):
        '''
        tem_liberdades: goban x intersecao → bool

        Esta função auxiliar verifica se uma cadeia de pedras tem pelo menos uma liberdade.
        '''

        # Verifica se pelo menos uma fronteira da cadeia é uma pedra neutra
        for adjacente in obtem_adjacentes_diferentes(g, obtem_cadeia(g, i)):
            if not eh_pedra_jogador(obtem_pedra(g, adjacente)):
                return True
            
        return False

def str_intersecao_valida(str_intersecao):
    '''
    str_intersecao_valida: str → bool

    Esta função auxiliar verifica se uma representação ext.
    '''
    # Verifica se a entrada é uma string
    if not isinstance(str_intersecao, str) or not len(str_intersecao) in [2, 3]:
        return False

    # Verifica se o primeiro caracter está entre 'A' e 'S'
    if not ('A' <= str_intersecao[0] <= 'S'):
        return False

    # Verifica se os caracteres restantes são dígitos
    if not str_intersecao[1:].isdigit():
        return False

    
    # Verifica se o número está entre 1 e 19
    num = int(str_intersecao[1:])
    if not num in range(1, 20):
        return False
    
    return True
