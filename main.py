from random import randint
import os
saldo = int(input("Insira quanto quer depositar para jogar: "))

multi = 0
balan = 0
jogadas = 0

while jogadas != 100:   
    print("Seu saldo atual é de", saldo)
    valor = int(input("Quanto quer Apostar?  R$  "))   
    os.system("cls")
     
# Balanço de 3 primeiras jogadas    
     
    if jogadas==0 and valor<= 10:
         sorte = 1
         multi = 2.5
         
    elif jogadas == 1 and valor<= 10:
        sorte = randint(0,1) 
        multi = 1.5
        
    elif jogadas == 2 and valor >= 10:
        sorte =  randint(0,9)
        multi = 1.4
    
    else: 
             
#  Balanceamento de jogadas não manipuladas             
             
        if valor <= 20:
            if balan <= 3:
                sorte = randint(0,2)
                multi = 1.3
            else:
                sorte = randint(0,3)
                multi = 1.5
        elif valor <= 50:
            if balan >= 10:
                sorte = 1
                multi = 1.2
            else:
                sorte = randint(0,4)
                multi = 1.25
        elif valor <= 100:
            sorte = randint (0,9)
            multi = 1.2
            
        elif valor <= 500:   
            sorte = randint(0,25) 
            multi = 1.5   
        else:
            sorte = randint(0,30) 
            multi = 1.25
            
               
    teste = randint (0,5)
    teste1 = randint (0,5)
    teste2 = randint (0,5)



    if sorte == 1:
        teste1 = teste
        teste2 = teste
    
    
    print("---------------------------------Lucky Tiger------------------------------------")
    print("    ")
    
    print(teste, teste1, teste2 )

    print("    ")
    if teste == teste1 and teste == teste2 and teste1 == teste2:
        
        valor = valor*multi
        print('\x1b[1;30;42m' + 'Parabens' + '\x1b[0m' + " voce ganhou R$", valor)
        balan = 0
        

        
    else:
        print('\x1b[0;30;41m' +  'Poxa, não foi dessa vez.' + '\x1b[0m' + " Vamos outra?")
        balan += 1  
        valor = valor*-1

    print("    ")

    saldo += valor   
    
    jogadas += 1
    

    
#Quando o saldo zerar    
    
    if saldo <= 0:
        jogar = input("seu saldo esta " + '\x1b[1;30;41m' + "negativo" + '\x1b[0m' ", deseja adicionar mais?  ")
        if jogar != "nao":
            saldo += int(input("quanto deseja adicionar? "))
            while saldo < 0:
                print("Seu saldo atual é de ", saldo)
                print("valor ainda " '\x1b[1;30;41m' + "insuficiente" + '\x1b[0m')
                perg = input("Adicionar mais?")
                if perg != "nao":
                    saldo += int(input("quanto deseja adicionar? "))                    
                else:
                    break            
        else:
            break    
                
                   
print("seu saldo final foi: ", saldo)