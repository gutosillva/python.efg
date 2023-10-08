#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Nome do usuario: ")
senha = input("senha: ")
while usuario == senha:
    print("senha não pode ser igual ao usuario")
    senha = input("senha: ")
print("USUARIO:",usuario)
print("SENHA:", senha)