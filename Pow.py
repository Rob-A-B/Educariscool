import os
import forcapou, estatisticas

def limpa():
    os.system('cls')

    #Variáveis globais
moedas = 30
exp = 0
saude = 0
felicidade = 0

def opcoes(local, um, dois):
    limpa()
    print(f'''{local}

[1] {um}
[2] {dois}
[3] Loja
[0] Voltar ao início   
''')

    resposta= int(input('O que deseja fazer? '))

    if (local == 'SALA DE ESTAR'):
        if (resposta == 1):
            jogos()
        elif (resposta == 2):
            #bolinha()
            pass
    elif (local == 'SALA DE ESTUDOS'):
        if (resposta == 1):
            #atividades()
            pass
        elif (resposta == 2):
            #material()
            pass
        
    elif (local == 'SALA DE AULA'):
        if (resposta == 1):
            estatisticas.barras()
            pass
        elif (resposta == 2):
            #ranking()
            pass


    if (resposta == 3):
        loja()
    if(resposta == 0):
        menu()


    #LOJA
def loja():

    limpa()
    print('''LOJA

[1] 
[2] 
[0] Voltar ao início
''')
    resposta= int(input('O que deseja fazer? '))
    if (resposta == 1):
       pass
    elif (resposta == 2):
       pass
    elif(resposta == 0):
        menu()


    #SALA DE ESTAR
def sala_de_estar():
    um = 'Jogos'
    dois = 'Bolinha'
    opcoes('SALA DE ESTAR', um, dois)


    #SALA DE ESTUDOS   
def sala_de_estudos():
    um = 'Atividades'
    dois = 'Materias de aula'
    opcoes('SALA DE ESTUDOS', um, dois)
        

    #SALA DE AULA
def sala_de_aula():
    um = 'Estatísticas'
    dois = 'Ranking'
    opcoes('SALA DE AULA', um, dois)

    #JOGOS
def jogos():
    limpa()
    print('''O que deseja jogar?

[1] Forca
[2] 
''')
    resposta = int(input(""))
    if (resposta == 1):
        forcapou.jogar()
    elif (resposta == 2):
        pass
    



    #---------------MENU--------------
def menu():
    limpa()
    print(f'Saúde: {saude}/100 | Felicidade: {felicidade}/100 | Experiência: {exp}/100 | Moedas: {moedas}')
    print('''
INÍCIO
[1] Sala de estar
[2] Sala de estudos
[3] Sala de aula
''')

    resposta = int(input(""))
    if resposta == 1:
        sala_de_estar()
    elif resposta == 2:
         sala_de_estudos()
    elif resposta == 3:
        sala_de_aula()
            
if(_name_ == "_main_"):
    menu()
