from myfunctions.chatparser import cleanText
from myfunctions.train import trainBot
from chatterbot import ChatBot
import sys
import os
import pyttsx3


def start():
    ''' A function that starts the application. '''

    if sys.argv[1] == 'train' and sys.argv[2]:

        cleaned_chat = cleanText(os.path.join(os.getcwd(),'chat_data','raw_chat_data',sys.argv[2]))
        filename = os.path.join('chat_data','cleaned_chat.txt')

        with open(filename, 'w', encoding="utf-8") as f:
            for lines in cleaned_chat:
                f.write("%s\n" % lines)
        
        chatbot = trainBot(filename)
        print("traing complete chatbot:{chatbot} trained.")
        sys.exit(1)

    elif sys.argv[1] == 'chat':
        engine = pyttsx3.init()
        chatbot = ChatBot('Amaan')
        while True:
            con = str(input("You: "))
            response = chatbot.get_response(str(con))
            print(f"Bot: {response}")
            engine.say(f"{response}")
            engine.runAndWait()
    
    elif sys.argv[1] == 'api':
    	os.system('python app.py') 

    else :
        print ("for training: python main.py train <Input TextFileName> \nfor chat : python main.py chat")
        sys.exit(1)
    

if __name__ == "__main__":
    
    start()
   	