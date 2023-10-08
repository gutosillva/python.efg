import time

# Definindo variáveis globais para o jogador
nome = ""
pocao = False
amuleto = False
dica = False

def introducao():
    print('''
    Bem-vindo ao Labirinto Maldito!
    Neste jogo, você é um guerreiro em busca de tesouros em um labirinto misterioso.
    Sua jornada está prestes a começar...
    ''')
    time.sleep(2)

def taberna():
    print('''
    Você chega a uma taberna na estrada. Há um mendigo contando histórias.
    O que você quer fazer?
    [1] Pedir uma bebida
    [2] Se aproximar do mendigo
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você pede uma bebida e observa o mendigo contar sua história.')
        # Continuar a história...
    elif escolha == 2:
        print('Você se aproxima do mendigo para ouvir sua história.')
        # Continuar a história...

def escolha_magico():
    print('''
    O mendigo conta sobre um mago que pode torná-lo rico, mas o mago é perigoso.
    Você acredita na história?
    [1] Sim
    [2] Não
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você decide acreditar na história do mendigo e continua sua jornada.')
        # Continuar a história...
    elif escolha == 2:
        print('Você acha a história do mendigo absurda e segue em frente.')
        # Continuar a história...

def entrada_labirinto():
    print('''
    Você chega ao labirinto e encontra um mago que oferece um desafio.
    Você aceita?
    [1] Sim
    [2] Não
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você aceita o desafio do mago e entra no labirinto.')
        # Continuar a história...
    elif escolha == 2:
        print('Você recusa o desafio do mago e tenta sair do labirinto.')
        # Continuar a história...

def acao_magico():
    print('''
    O mago lança um feitiço e você cai em um calabouço.
    Você se depara com duas alavancas.
    Qual alavanca você quer puxar?
    [1] Alavanca da esquerda
    [2] Alavanca da direita
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você puxa a alavanca da esquerda e algo acontece.')
        # Continuar a história...
    elif escolha == 2:
        print('Você puxa a alavanca da direita e algo acontece.')
        # Continuar a história...

def encontro_gargulas():
    print('''
    Você encontra duas gargulas discutindo no corredor.
    Como você pretende abordá-las?
    [1] Atacar sem aviso
    [2] Tentar conversar
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você ataca as gargulas, mas elas fogem e você as persegue.')
        # Continuar a história...
    elif escolha == 2:
        print('Você tenta conversar com as gargulas, mas elas fogem e você as persegue.')
        # Continuar a história...

def escolha_gargulas():
    print('''
    Você alcança as gargulas e elas oferecem ajuda em troca de moedas.
    Você aceita pagar?
    [1] Sim
    [2] Não
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você paga as moedas às gargulas e recebe informações úteis.')
        # Continuar a história...
    elif escolha == 2:
        print('Você recusa a oferta das gargulas e segue seu caminho.')
        # Continuar a história...

def escolha_final():
    print('''
    Você chega a uma bifurcação.
    Para onde você deseja ir?
    [1] Caminho da esquerda
    [2] Caminho da direita
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('Você escolhe o caminho da esquerda e continua sua jornada.')
        # Continuar a história...
    elif escolha == 2:
        print('Você escolhe o caminho da direita e continua sua jornada.')
        # Continuar a história...

def main():
    introducao()
    taberna()
    escolha_magico()
    entrada_labirinto()
    acao_magico()
    encontro_gargulas()
    escolha_gargulas()
    escolha_final()

if __name__ == "__main__":
    main()
def confronto_inimigo():
    global pocao, amuleto
    print('''
    Você continua pelo corredor e encontra um inimigo poderoso bloqueando o caminho.
    Você deseja lutar ou fugir?
    [1] Lutar
    [2] Fugir
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        if pocao:
            print('Você usa sua poção mágica para fortalecer-se na batalha.')
            # Continuar a história...
        else:
            print('Você luta contra o inimigo, mas ele é muito forte e você é derrotado.')
            # Fim do jogo...
    elif escolha == 2:
        print('Você decide fugir do inimigo e corre de volta ao corredor anterior.')
        escolha_final()

def encontrar_tesouro():
    global amuleto
    print('''
    Você continua explorando o labirinto e encontra uma sala cheia de tesouros.
    No centro da sala, há um amuleto brilhante.
    Você deseja pegar o amuleto?
    [1] Sim
    [2] Não
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        amuleto = True
        print('Você pega o amuleto e sente seu poder mágico fluir por você.')
        # Continuar a história...
    elif escolha == 2:
        print('Você decide não pegar o amuleto e continua sua exploração.')
        # Continuar a história...

def encontrar_final():
    global dica
    print('''
    Você chega ao final do labirinto, onde um grande baú está trancado.
    Há uma placa que diz: "Para abrir o baú, você deve responder a uma pergunta."
    Você quer tentar abrir o baú?
    [1] Sim
    [2] Não
    ''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        if dica:
            print('Você responde corretamente à pergunta e o baú se abre, revelando tesouros incríveis.')
            # Final vitorioso...
        else:
            print('Você não consegue responder à pergunta e o baú permanece trancado.')
            # Continuar a história...
    elif escolha == 2:
        print('Você decide não arriscar e volta a explorar o labirinto.')
        # Continuar a história...

def continuar_exploracao():
    print('''
    Você continua explorando o labirinto, passando por corredores misteriosos e salas sombrias.
    Sua jornada está longe de terminar...
    ''')
    # Continuar a história...

def main():
    introducao()
    taberna()
    escolha_magico()
    entrada_labirinto()
    acao_magico()
    encontro_gargulas()
    escolha_gargulas()
    escolha_final()
    confronto_inimigo()
    encontrar_tesouro()
    encontrar_final()
    continuar_exploracao()

if __name__ == "__main__":
    main()
def final_vitorioso():
    print('''
    Parabéns, {}, você conseguiu superar todos os desafios e obstáculos do Labirinto Maldito!
    Com o amuleto mágico em sua posse, você encontra a saída e retorna à superfície.
    Você emerge do labirinto como um herói lendário, carregando riquezas incalculáveis e conhecimento mágico.
    A cidade ao norte recebe você com festa, e sua fama se espalha por todo o reino.
    Sua jornada foi um sucesso, e você vive seus dias em prosperidade e renome.
    O Labirinto Maldito é agora apenas uma lenda, graças à sua coragem e inteligência.
    Você venceu o jogo!
    '''.format(nome))

def final_derrota():
    print('''
    Infelizmente, {}, você não conseguiu superar os perigos do Labirinto Maldito.
    Seu corpo é encontrado dentro do labirinto, e sua história se torna uma triste lenda.
    O amuleto e os tesouros permanecem ocultos no interior do labirinto, enquanto o mistério do lugar
    persiste para sempre.
    Você não conseguiu vencer o jogo, mas sua valentia será lembrada.
    '''.format(nome))

def final_alternativo():
    print('''
    Você decide não enfrentar o desafio final e, em vez disso, retorna à superfície.
    Sua jornada termina sem a recompensa do tesouro e do amuleto, mas você sobrevive.
    A cidade ao norte recebe você de volta com alívio, e você vive uma vida tranquila.
    O Labirinto Maldito permanece um enigma não resolvido.
    ''')

def main():
    # ...
    # (Código anterior)
    # ...

    # Após os eventos finais, você pode adicionar um código para determinar o final com base nas ações do jogador.
    if amuleto:
        final_vitorioso()
    else:
        final_derrota()

if __name__ == "__main__":
    main()
