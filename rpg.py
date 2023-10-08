# MEU PRIMEIRO RPG
# LABIRINTO MALDITO

from time import sleep

nome=""
escolha=0
pocao=False
amuleto=False 
dica=False
print('''
	\\\\hsjstwfk1111\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\				 
	\\\\nguwvwkutjamsewfksywekwujwls111\\\\\\\\\\\\\\\					
	\\\\wkksewfksywewhsjseafzshjafuwkskzsjs1\\\\\\\\\\		
	\\\\lwseg\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\					
	\\\\fsgngmxsdsjemalsugakshgjimwfsgkgmtgefakkg\\\\\			
	\\\\kgimwjaslwxsrwjmeshwjymfls1\\\\\\\\\\\\\\\\\\\				
	\\\\kzsjssdnwkjwkwfvw1nguwsuwalskwusksjugeayg1\\\\			
	''')
sleep(2)
print('''
	VOCÊ ESTÁ JOGANDO UM RPG DE MESA CRIADO POR GUTO SILVA.
	ESTE É MEU PRMEIRO JOGO DE RPG.
	ME INSPIREI NO LIVRO "SÓ AVENTURA".
	ESPERO QUE VOCÊ GOSTE...
	.....
	''')
sleep(2)
print('''
	A VIDA É FEITA DE ESCOLHAS...
	MAS AS CONSEQUÊNCIAS DELAS DEFINEM SE VOCÊ AGIU DE FORMA CORRETA OU ESTUPÍDA.
	PENSE BEM ANTES DE ESCOLHER.
	SIGA SEMPRE SEU CORAÇÃO.
	''')											
sleep(2)
print('''
	OLÁ JOVEM VIAJANTE!!!!
	A PARTI DAQUI VOCÊ IRÁ ESCREVER SUA PROPRIA HISTÓRIA...
	PARA COMEÇAR SUA JORNADA VOCÊ PRECISA SABER DE ALGUMAS COISAS:
	PRIMEIRO: VOCÊ AGORA É UM(A) GUERREIRO(A) QUE VIAJA A PROCURA DE NOVAS AVENTURAS E DESAFIOS 
	SEGUNDO: VOCÊ ESTÁ VIAJANDO PARA UMA PACATA CIDADE AO NORTE POIS OUVIU RUMORES DE QUE NAQUELA CIDADE 
	HÁ UM LABIRINTO COM MILHARES DE TESOUROS JAMAIS VISTOS...
	TERCEIRO: ANTES DE CHEGAR A CIDADE VOCÊ RESOLVER PARAR EM UMA PEQUENA TABERNA A BEIRA DA ESTRADA
	PARA DESCANÇAR UM POUCO...
		
	AGORA SUA JORNADA VAI COMEÇAR... 
	SÓ LHE DESEJO BOA SORTE...
	...
	BEM VINDO AO LABIRINTO MALDITO...
	''')
sleep(2)
print('''
	Você desce do seu cavalo e amarra ele no pequeno estabulo ao lado da cabana
	onde coloca um pouco de comida e água para ele, vocês tinha andado o dia todo estavam famintos e sedentos.
	Quando entrou ficou um pouco surpreso com o local, era bastante arrumado e organizado para uma simples taberna...
	Tinha um piano do outro lado do lugar onde um senhor tocava uma melodia bem harmonica
	...você gosta do local...
	Ninguém lhe dá atenção ao você entrar...
	Quando você chega proximo ao balcão observa que há uma pequena aglomeração ao redor de uma mesa.
	Mais precisamente as pessoas estão ao redor de um velho maltrapilho que parece estar gostando da atenção.
	''')
sleep(2)
print('O que você quer fazer agora?')
print('''
	[1] Você quer pedir uma bebida primeiro antes de se aproximar
	[2] Você prefere se aproximar da aglomeração na esperança de alguém pagar uma bebida pra você
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Você diz ao garçom que quer uma cerveja...
		Ele te observa alguns segundos antes de pegar para você
		Parece um pouco relutante em entregar a bebida...
		Mas entrega mesmo assim...
		Enquento você bebe sua cerveja fica observando a aquelas pessoas em volta do mendigo maltrapilho
		Parecia que ele estava contando uma história bem interessante...
		''')
if escolha==2:
	print('''
		Você decide chegar mais proximo do velho e escutar o que ele fala
		Quando você se aproxima ele sorri ainda mais contente e começa a falar mais alto
		''')				
sleep(2)							
print('''
	Era uma história de que havia uma casinha de madeira no alto de um morro do outro lado da cidade
	e nessa casa morava um mago que poderia te deixar muito rico...
	Era só fazer o que ele pedisse...
	''')
sleep(2)						
print('O que você acha dessa história?')	
print('''
	[1] A história é pura besteira
	[2] A história é verdadeira
	''')			
escolha=int(input('Sua escolha:'))
if escolha==1:		
	print('''		
		Era pura asneira-você pensa-esse negocio de magia, magos, feitiços, não existe
		Você se vira para sair dali
		''')
if escolha==2:
	print('''
		Você fica adimirado com aquela história
		rapidamente se vira para ir embora dali.
		Não queria perder tempo ali naquele bar com aquele velho por mais que a história seja magnifica
		''')
sleep(2)
print('''	
	Era como se o velho lesse sua mente:
	no momento em que você se vira para sair dali ele diz para você:
	''')
print('"Qual seu nome jovem guerreiro(a)?"')
nome=input('Você responde:')
print('{}, nome de um verdadeiro guerreiro(a)'.format(nome)) 
print('''
	Você parece ser um(a) guerreiro(a) muito esperto(a). 
	Por que não tenta ficar rico e vai até a cabana?
	Já que você me parece ser bem corajoso...
	''')
print('Você aceita o desafio?')
print('''
	[1] Sim
	[2] Não
	''')
escolha=int(input('Sua escolha:'))
sleep(2)
if escolha==1:
	print('''
		"Eu aceito o desafio, pois sou {} o(a) melhor guerreiro(a) desse país
		e não tenho medo de nada..."
		'''.format(nome))
if escolha==2:
	print('''
		Não tenho tempo para esse tipo de idiotice
		''')				
sleep(2)
print('''
	Você saí daquela taberna um pouco confuso, pega seu cavalo no estabulo, e segue rumo a cidade.
	Chegando no centro da cidade você percebe que há um morro do outro lado dela
	e olhando mais atentamente percebe-se que há alguma coisa no alto do morro...
	Será a cabana de madeira?
	Será que a história daquele mendigo moribundo da taberna é mesmo verdade?
	Bom só tem um jeito de descobrir...
	
	Você atravessa a cidade em cima do seu cavalo.
	Sobe o morro com um certo receio
	Não sabe se tá fazendo a coisa certa...
	Quando chega a cabana percebe que não há nada de diferente nela pelo menos no seu exterior.
	Parecia uma cabana normal de madeira, um pouco abandonada, porém conservada...
	Você vai até a porta, decide bater primeiro antes de entrar, porém...
	Quando você levanta a mão para bater, a porta se abre sozinha antes mesmo de você encostar nela...
	Lá dentro era muito estranho. Havia varias prateleiras apinhadas de vidros com liquidos estranhos,
	havia também algumas jaulas penduradas no teto com bichos que você nunca tinha vistos.
	A cabana parecia estar vazia...
	''')
sleep(5)
print('''
	......
	....
	BAAAAAAAMMMMM!!!!!!
	....
	...
	''')			
sleep(5)
print('''
	Uma esplosão acontece de repente, uma função branca muito densa sai do local da esplosão...
	Bem na sua frente surge um velho vestido de um manto azul 
	e um chapeu pontudo, sua barba era muito grande 
	quase arrastava no chão.
	Era um mago
	Para sua surpresa aquele mago era o mendigo da taberna...
	''')
print('''
	"Sabia que você viria nobre guerreiro(a) {} "
	"sabia que você não resistiria a tentação..."
	"Para sair com muitas riquezas e vivo daqui você tem que escolher 
	'''.format(nome))
print('''
	sabiamente senhor(a) {} ou o(a) senhor(a) encontrara 
	a MORTE antes mesmo de ter qualquer reação...".
	'''.format(nome))
sleep(2)
print('''
	"O desafio vai começar! Se conseguir sair do meu labirinto cheio de magia e obstaculos
	você vai ser um homem muito rico..."
	''')			
sleep(2)
print('''
	Antes mesmo de você dizer qualquer coisa o mago puxa uma alavanca e imediatamente um 
	buraco,era uma especie de escorregador, que se abre ao seus pés e você não tem tempo de escapar
	e acaba caindo nele
	....
	Você escorrega durante um bom tempo, parecia que o tunel tinha varios metros de profundidade e você
	caia muito rapido
	....
	Quando você chega ao fim do escorregador percebe que você está em um calabouço mal iluminado.
	Não tem como voltar pelo escorregador...
	Mas você percebe que há duas alavancas a sua frente
	''')
print('Qual alavanca você quer puxar?')
print('''
	[1] alavanca da esquerda
	[2] alavanca da direita
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Quando você puxa a alavanca um buraco se abre em cima da sua cabeça.
		De lá começa a chover um liquido estranho que ao entrar em contato com sua pele
		começa a queimar...
		Era acído...
		....
		Você morre senhor(a) {} 
		'''.format(nome))
				
if escolha==2:
	print('''
		Guerreiro(a) {}, o senhor(a) está em um corredor comprido e pouco iluminado 
		por tochas de fogo ardente e vivo...
    	No fim do corredor há uma luz mais forte que você quer investigar mais de perto, porém...
   		Há uma porta antes do fim do corredor
		''')
print('O que você está pensando em fazer?')
print('''
	[1] Vou ignorar a porta
	[2] Quero saber o que há atrás da porta
	''')
if escolha==1:
	print('''
		Você entra em uma sala pequena e pouco iluminada que não tem nada 
		exceto por um baú no meio da sala...
   		Guerreiro(a) {} fica curioso para saber o que há dentro do baú 
		mas tem medo de abri-lo então pega sua espada antes de encosta no nel
    	com sua espada em uma das mãos você abre a tampa do baú...
    	Fica surpreso e alegre com que encontra lá dentro...
    	Era algumas moedas de ouro e um frasco com um liquido estranho dentro 
		que você pega mesmo não sabendo o que é
    	Você sai da sala e continua a andar pelo corredor...
		'''.format(nome))
pocao=True
if escolha==2:
	print('''
		Guerreiro(a) {}, o senhor(a) está em uma sala circular e ampla que está vazia exceto 
		por uma estatua de pedra maciça no centro da sala
		olhando mais de perto você observa que a estatua tem no lugar dos olhos 
		grandes rubis e na mão direita da estatua há um papel...	
		'''.format(nome))		
sleep(2)
print('''
   	Guerreiro(a) {}, o senhor(a) está em uma sala circular e ampla que está vazia exceto 
	por uma estatua de pedra maciça no centro da sala
   	olhando mais de perto você observa que a estatua tem no lugar dos olhos 
	grandes rubis e na mão direita da estatua há um papel...	
	'''.format(nome))
sleep(2)
print('O que você quer fazer agora?')
print('''
	[1] Retirar o rubi esquerdo
	[2] Retirar o rubi
	[3] Retirar o papel
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Você saca sua espada à intruduz no olho esquerdo 
		da estatua arrancando o rubi que cai na sua mão...
		era grande e ipnotizante...
		você olha para a estatu novamente com a intençao 
		de retirar o segundo olho da estatua mas...
		O chão ao seus pés começa a rachar e se abrir 
		em grandes fissuras que começam a expelir lava vulcânica...
		O bravo guerreiro(a) {} tenta correr para o corredor para tentar se salvar
		mas é tarde demais...
		o acesso ao corredor está fechado com uma parede solida...
		Você morre queimado gritando e se agonizando de dor...
		'''.format(nome))
if escolha==2:
	print('''
		Você saca sua espada à intruduz no olho direito 
		da estatua arrancando o rubi que cai na sua mão...
		era grande e ipnotizante...
		você olha para a estatua novamente com a intençao 
		de retirar o segundo olho da estatua, mas...
		prefere não arriscar... Tava facil demais...
		Você olha para  a mão da estatua e retira o papel que está lá...
			
							NO PAPEL DIZ:
		"JOVEM GUERREIRO(A) NÃO PEGUE A PEDRA DO OLHO ESQUERDO DA ESTATUA,
		POIS ENCONTRARÁ UMA MORTE TERRIVEL.
		PORÉM FIQUE A VONTADE PARA PEGAR A PEDRA DO OLHO DIREITO."
			
		você não mexe no olho esquerdo da estatua...
		você observa a sala mais atentamente agora e vê que do outro lado há um corredor...
		na esperança de sair daquele lugar o mais rapido possivel você rapidamente segue por ele
		no caminho você escuta vozes sussurrando mais a frente onde está mais claro
		Chegando mais perto e com cuidado você consegue ver duas criaturas...
		eram gargulas parecia que estavam discutindo... e eram horrorosas...	
		''')
if escolha==3:
	print('''
							NO PAPEL DIZ:
		"JOVEM GUERREIRO(A) NÃO PEGUE A PEDRA DO OLHO ESQUERDO DA ESTATUA,
		POIS ENCONTRARÁ UMA MORTE TERRIVEL.
		PORÉM FIQUE A VONTADE PARA PEGAR A PEDRA DO OLHO DIREITO."
			
		com as instruçoes do papel você
		saca sua espada à intruduz no olho direito 
		da estatua arrancando o rubi que cai na sua mão...
		era grande e ipnotizante...
		você não mexe no olho esquerdo da estatua...
		você observa a sala mais atentamente agora e vê que do outro lado há um corredor...
		na esperança de sair daquele lugar o mais rapido possivel você rapidamente segue por ele
		no caminho você escuta vozes sussurrando mais a frente onde está mais claro
		Chegando mais perto e com cuidado você consegue ver duas criaturas...
		eram gargulas parecia que estavam discutindo... e eram horrorosas...
		''')
sleep(2)
print('Qual é o melhor jeito de se aproximar delas?')
print('''
	[1] Chegar atacando
	[2] Tentar conversar com elas
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		O(A) bravo(a) guerreiro(a) {} saca sua espada de lamina muito afiada...
		Você começa a andar devagar em direção as gargulas na intenção de pega-las de surpresa...
		Porém elas percebem sua aproximação... param de discutir e...
		fogem desesperadas e com medo...
		Você fica sem entender o que aconteceu...então sem pensar resolve correr atrás delas...
		Elas são rapidas mas você consegue correr tão depressa quanto elas 
		quando você estava quase alcançando elas...
		Vocês chegam em uma bifurcação...
		As gargulas vão pelo caminho da esquerda...
		'''.format(nome))
if escolha==2:
	print('''
		Você resolvel chegar na diplomacia, ou seja, tentar conversar com elas
		O bravo guerreiro {} guarda sua espada de lamina muito afiada...
		Você começa a andar devagar em direção as gargulas com um pouco de receio...
		Elas percebem sua aproximação... param de discutir e...
		antes de você abrir a boca para falar um 'Olá' elas...
		fogem desesperadas e com medo...
		Você fica sem entender o que aconteceu...então sem pensar resolve correr atrás delas...
		Elas são rapidas mas você consegue correr tão depressa quanto elas 
		quando você estava quase alcançando elas...
		Vocês chegam em uma bifurcação...
		As gargulas vão pelo caminho da esquerda...
		'''.format(nome))			
sleep(2)
print('O que sua curiosidade manda você fazer?')
print('''
	[1] Continuar perseguindo as gargulas 
	[2] Seguir pela direita e ignorar as criaturas pr enquanto (elas podem estar te levando para uma armadilha)
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Você opita por perseguir as gargulas mesmo sem saber para onde elas estão te levando...
		...pode ser uma armadilha...
		Você consegue alcançar as gargulas e antes de você fazer qualquer coisa...
		Elas dizem:"Não nós mate guerreiro estamos em paz...
		podemos te ajudar a sair desse lugar...
		por algumas moedas podemos te dar algumas intruções de como sair daqui"
		''')
	print('Quer pagar pra ver senhor(a) {}'.format(nome))
	print('''
			[1] SIM
			[2] NẪO
			''')
escolha=int(input('Sua escolha:'))
if escolha==1:
		print('''
			entrega algumas moedas para as gargulas...
			Elas ficam admiradas com as moedas de ouro e começam a falar:
			"Se entrar na porta numero 1: ATAQUE SEM VER; 
			Se entrar na porta numero 2: PEGUE O QUE È OFERECIDO; 
			Não entre na porta numero 3 ou morrerá"		
			Você agradece as gargulas dá as costas para elas e sai.
			''')
dica=True
if escolha==2:
		print('''
			Você não entrega as moedas as gargulas
			fica furioso, acha que elas querem passar a perna em você
			{} saca sua espada e com apenas alguns golpes mata as gargulas...
			Você fica olhando por alguns instantes os corpos caídos das criaturas, se vira e saí...
			com um pouco de remorsso pois não sabe se fez o certo...
			'''.format(nome))										
if escolha==2:
	print('''
		{} segui pelo corredor da direita
		neste corredor há duas portas e uma bifurcação...
		'''.format(nome))
sleep(2)
print('Onde quer se aventurar primeiro?')
print('''
	[1] Porta de ouro
	[2] Porta de prata
	[3] Ir dereto para a bifurcação
		''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Era uma sala grande com muito ouro,joias e varias estatuas de pedra...
		Você começa a saquear as peças de ouro e as joias... até que...
		O bravo {} percebe que mais a frente há uma silhueta de uma pessoas...
		parece ser uma mulher...
		...ou não...
		'''.format(nome))
	print('''
		é quando você percebe que as estatuas que estão na sala não são estatuas comuns...
		elas estão com expressões diferentes das normais...
		parece que estão com medo de algo, estão com expressão de pavor no rosto...
		você olha para a silhueta da mulher novamente...
		então você consegue perceber que no lugar dos cabelos delas haviam cobras...
		antes que pudesse você se defender...
		guerreiro {} você é petrificado...
		era uma medusa...
		'''.format(nome))
if escolha==2:
	print('''
		Era uma sala cheia de estantes...
		nessas estantes haviam bonequinhos de madeira... 
		varios deles... você podia até dizer que eram milhares...
		no fundo da sala estava um anão com uma faca entalhando mais bonequinhos de madeira...
		ele levanta a cabeça quando se aproxima e diz com uma voz que parecia mais um grunido:
		"Olá jovem guerreiro {}, fico feliz e surpreso de ter chegado até aqui..."
		Como você sabe meu nome - você pergunta meio confuso pois nunca havia visto aquele ser...
		"Sei de tudo que acontece aqui..."
		Você pergunta para criatura se ele conhece uma saída já que está alí a muito tempo
		Ele diz que não tem como sair dali - você vai morrer aqui...
		"Então tem algum jeito de sobreviver neste lugar?" você pergunta
		"Felizmente tenho o que o senhor precisa...
		Tenho um amoleto que pode fazer com que viva durante um tempo aqui embaixo...
		porém ele não é nada barato..."
		'''.format(nome))
	print('O que você responde para o anão?')
	print('''
		[1] "Não tenho dinheiro para isso"
		[2] "Tenho algumas moedas aqui, não sei se é o sulficiente"
		''')
	escolha=int(input('Sua escolha:'))
if escolha==1:
		print('''
			O anão responde:
			"Eu sei que você tem moedas de ouro que você pegou do báu..."
			"Mas já que não quer o amuleto saia daqui que eu tenho mais o que fazer."
			''')
amuleto=False
if escolha==2:
		print('''
			O anão responde:
			"Não se preocupe isso é o sulficiente."
			"Pode levar o amuleto senhor(a) {}"
			'''.format(nome))
amuleto=True
if escolha==3:
	print('''
		Você prefere seguir direto para a bifurcação
		Nesta bifurcação há uma porta a direita e uma há esquerda
		''')
print('Você quer abrir qual porta?')
print('''
	[1] Porta da esquerda 
	[2] Porta da direita
	''')
escolha=int(input('Sua escolha:'))
if escolha==1:
	print('''
		Você segue para a porta esquerda...
		Você tenta abri-la mas,ela está trancada...
		''')
	print('O que você pretende fazer?')
	print('''
		[1] Sua curiosidade é muito grande e você quer abrir a porta de qualquer jeito
		[2] Você não quer arriscar pois tem medo do que há do outro lado da porta
		''')