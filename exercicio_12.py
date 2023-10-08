
#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
   #     Salário Bruto: (5 * 220)        : R$ 1100,00
   #  (-) IR (5%)                     : R$   55,00  
   #     (-) INSS ( 10%)                 : R$  110,00
   #     FGTS (11%)                      : R$  121,00
   #     Total de descontos              : R$  165,00
   #     Salário Liquido                 : R$  935,00

ganho_hora=int(input("Quanto você recebe por hora?"))
hora_trabalho=int(input("Quantas horas você trabalhou?"))
salario=(ganho_hora * hora_trabalho)
print(f"Você recebeu:R${salario}")

if salario <= 900:
    print("você é insento do Imposto de Renda")
elif salario > 900 and salario <= 1500:
    porcentagem_IR= 5
    porcentagem_inss= 10
    porcentagem_fgts= 11
    IR=(porcentagem_IR/100)* salario
    INSS=(porcentagem_inss/100)*salario
    FGTS=(porcentagem_fgts/100)*salario
    desconto=IR+INSS
    salario_final= salario-IR-INSS-FGTS+FGTS

    print(f"Imposto Renda: R${IR:.2f}")
    print(f"INSS: R${INSS:.2f}")
    print(f"FGTS: R${FGTS:.2f}")
    print(f"total desconto: R${desconto:.2f}")
    print(f"Salário Liquido: R${salario_final:.2f}")
    
elif salario > 1500 and salario <= 2500:
    porcentagem_IR= 10
    porcentagem_inss= 10
    porcentagem_fgts= 11
    IR=(porcentagem_IR/100)* salario
    INSS=(porcentagem_inss/100)*salario
    FGTS=(porcentagem_fgts/100)*salario
    desconto=IR+INSS
    salario_final= salario-IR-INSS-FGTS+FGTS

    print(f"Imposto Renda: R${IR:.2f}")
    print(f"INSS: R${INSS:.2f}")
    print(f"FGTS: R${FGTS:.2f}")
    print(f"total desconto: R${desconto:.2f}")
    print(f"Salário Liquido: R${salario_final:.2f}")
    
elif salario > 2500:
    porcentagem_IR= 20
    porcentagem_inss= 10
    porcentagem_fgts= 11
    IR=(porcentagem_IR/100)* salario
    INSS=(porcentagem_inss/100)*salario
    FGTS=(porcentagem_fgts/100)*salario
    desconto=IR+INSS
    salario_final= salario-IR-INSS-FGTS+FGTS

    print(f"Imposto Renda: R${IR:.2f}")
    print(f"INSS: R${INSS:.2f}")
    print(f"FGTS: R${FGTS:.2f}")
    print(f"total desconto: R${desconto:.2f}")
    print(f"Salário Liquido: R${salario_final:.2f}")
    
    