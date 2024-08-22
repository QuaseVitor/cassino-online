from random import randint
import os
saldo = int(input("Insira quanto quer jogar"))
multi = 0
balan = 0

while True:   
    print("Seu saldo atual é de ", saldo)
    valor = int(input("Quanto quer gastar?  R$  "))
     
    os.system("cls")
     
    if valor <= 20:
        if balan >= 4:
            sorte = 1
            multi = 1.3
        else:
            sorte = randint(0,2)
            multi = 1.5
    elif valor <= 50:
        if balan >= 10:
            sorte = 1
            multi = 1.2
        else:
            sorte = randint(0,4)
            multi = 1.25
    else:
        if balan >= 15:
            sorte = 1
            multi = 1.1
        else:
            sorte = randint(0,9) 
            multi = 1.1
            
    
    x = 0
    teste = randint (0,5)
    teste1 = randint (0,5)
    teste2 = randint (0,5)



    if sorte == 1:
        teste1 = teste
        teste2 = teste
    
    print(teste, teste1, teste2 )

    if teste == teste1 and teste == teste2 and teste1 == teste2:
        
        valor = valor*multi
        print("Parabens voce ganhou R$",valor)
        
        
    else:
        print("kkkkkkksefudeu")
        balan += 1  
        valor = valor*-1
     
 
    saldo += valor   
    
#Quando o saldo zerar    
    
    if saldo <= 0:
        jogar = input("seu saldo esta negativo, deseja adicionar mais?  ")
        if jogar != "nao":
            saldo += int(input("quanto deseja adicionar? "))
            while saldo < 0:
                print("Seu saldo atual é de ", saldo)
                print("valor ainda insuficiente")
                perg = input("adicionar mais?")
                if perg != "nao":
                    saldo += int(input("quanto deseja adicionar? "))                    
                else:
                    break            
        else:
            break    
                
                   
print("seu saldo final foi: ", saldo)