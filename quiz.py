print("Seja muito bem vindo(a/e) ao quiz!")
resposta_usuario = input("Quer começar? (S/N) ")

if resposta_usuario != "S":
    quit()
    
score = 0   
    
print("Começando...")
print("Para que serve a função print? \n (A) Para mostrar uma mensagem ao usuário \n (B) Para pedir uma informação ao usuário \n (C) Para emitir uma captura de tela \n (D) Para sair do programa")
resposta_1 = input("Resposta: ")

if resposta_1 == "A":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta Incorreta :(")
    
print("Para que serve a função input? \n (A) Para mostrar uma mensagem \n (B) Para pedir ao usuário para digitar algo \n (C) Para que armazenar dados \n (D) Para executar uma captura de tela")
resposta_2 = input("Resposta: ")

if resposta_2 == "B":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta Incorreta :(")
    
print("O que é uma variavél? \n (A) Serve para pedir um dado/valor \n (B) São informações que variam \n (C) São dados/valores \n (D) É um espaço para armazenar dados/valores")
resposta_3 = input("Resposta: ")

if resposta_3 == "D":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposta Incorreta :(")
    
print("Como utilizar variáveis para guardar os dados inseridos pelos usuários? \n (A) Colocando primeiro a função 'if' e depois a variável \n (B) Colocando a variável antes da função 'input' \n (C) Colocando a função 'input' antes da variável \n (D) Colocando a variável dentro da função 'input'")
resposta_4 = input("Resposta: ")

if resposta_4 == "B":
    print("Resposta Correta!")
    score = score + 1
else:
    print("Resposta Incorreta :(")
    
    
print(f"Quiz acabou... Pontuação: {score}/4")