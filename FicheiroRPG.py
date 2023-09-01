import random
print('escolha um nome, idade, uma raça(anão, humano, elfo, gnomo, meio-elfo, meio-orc ou halfling) e uma classe(barbaro, bardo, clerigo, druida, lutador, monge, paladino, ranger, ladino, bruxo ou mago) para o seu personagem')
print()
nome=input('Nome do seu personagem:')
idade=int(input('Idade:'))
raca=input('Raça:')
classe=input('Classe:')

d20= 21
dado= range(d20)
t1=random.choice((dado))
if t1 == 0:
    t1 +=1
t2=random.choice((dado))
if t2 == 0:
    t2 +=1
t3=random.choice((dado))
if t3 == 0:
    t3 +=1
t4=random.choice((dado))
if t4 == 0:
    t4 +=1
t5=random.choice((dado))
if t5 == 0:
    t5 +=1
t6=random.choice((dado))
if t6 == 0:
    t6 +=1

print()
print('FICHA DO JOGADOR')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Raça: {raca}')
print(f'Classe: {classe}')
print()
if raca == 'gnomo':
    print('Força:', t1-2)
    print('Detreza:',t2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4)
    print('Constituição:', t5 + 2)
    print('Carisma:', t6 + 2)
if raca == 'anao':
    print('Força:', t1)
    print('Detreza:',t2)
    print('Sabedoria:',t3 + 2)
    print('Inteligência:',t4)
    print('Constituição:', t5 + 2)
    print('Carisma:', t6 - 2)
elif raca == 'humano':
    print('Força:', t1)
    print('Detreza:',t2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4)
    print('Constituição:', t5 )
    print('Carisma:', t6)
    print('seus modificadores são +2 em uma habilidade qualquer')
elif raca == 'halfling':
    print('Força:', t1 - 2)
    print('Detreza:',t2 + 2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4)
    print('Constituição:', t5)
    print('Carisma:', t6 + 2)
elif raca == 'meio-orc':
    print('Força:', t1)
    print('Detreza:',t2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4)
    print('Constituição:', t5)
    print('Carisma:', t6)
    print('seus modificadores são +2 em uma habilidade qualquer')
elif raca == 'elfo':
    print('Força:', t1)
    print('Detreza:',t2 + 2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4 + 2)
    print('Constituição:', t5 - 2)
    print('Carisma:', t6)
elif raca == 'meio-elfo':
    print('Força:', t1)
    print('Detreza:',t2)
    print('Sabedoria:',t3)
    print('Inteligência:',t4)
    print('Constituição:', t5)
    print('Carisma:', t6)
    print('seus modificadores são +2 em uma habilidade qualquer')

else:
    print('essa raça não está disponivel ou foi escrito incorretamente, escreva exatamente como é mostrado no tutorial do inicio!')
    
