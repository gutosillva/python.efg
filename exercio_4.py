#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra=input("Digite uma letra: ")
vogal=a 
vogal=e
vogal=i
vogal=o
vogal=u
if letra == vogal:
    print("A letra digitada é uma vogal")
elif letra != vogal:
    print(" A letra digitada é uma consoante")
else:
    print("Isso é um numero")
	
#
letra=input("Digite uma letra: ")
vogal=a 
vogal=e
vogal=i
vogal=o
vogal=u
if letra == vogal:
    print("A letra digitada é uma vogal")
elif letra != vogal:
    print(" A letra digitada é uma consoante")
else:
    print("Isso é um numero")
	
	#letra=input("Digite uma letra: ")
vogal=a 
vogal=e
vogal=i
vogal=o
vogal=u
if letra == vogal:
    print("A letra digitada é uma vogal")
elif letra != vogal:
    print(" A letra digitada é uma consoante")
else:
    print("Isso é um numero")
	
#
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ")

# Lista de vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Verifica se a entrada é uma letra
if letra.isalpha():
    # Converte a letra para minúscula (para tornar o código não sensível a maiúsculas/minúsculas)
    letra = letra.lower()
    
    # Verifica se a letra é uma vogal
    if letra in vogais:
        print("A letra digitada é uma vogal")
    else:
        print("A letra digitada é uma consoante")
else:
    print("Isso não é uma letra")

