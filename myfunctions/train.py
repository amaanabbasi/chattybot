from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def trainBot(filename):
    ''' Training on the cleaned chat. '''
    chat_data = []

    # Loading chat data into a list
    with open(filename, 'r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            chat_data.append(line.strip()) # strip to remove /n characters
            
    # Intializing the bot and then training it on the data.
    chatbot = ChatBot('Amaan')
    conversation =  chat_data
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

    # Returning the trained bot 
    return chatbot

