nome = input('Qual o seu nome ?')
nota1 = int(input(f'{nome} digite sua nota de Português: '))
nota2= int(input(f'{nome} digite sua nota de Matemática: '))
media = int(nota1 + nota2)/2
print(f'{nome} sua média é de {media}')
