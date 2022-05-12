from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Wilson')
bot = ChatBot(
    'Wilson',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Wislon, irmão do jason',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
    'Qual o seu projeto?',
    'Como diminuir o desinteresse dos alunos?',
    'Uma das nossas propostas é a gameficação',
    'Como pretende fazer isso?',
    'Por meio de um mascote virtual, estilo tamagoshi',
])
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Wilson: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
