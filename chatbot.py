from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import Jarvis



chatbot = ChatBot('Test ')

conv = open('conversations.txt', 'r').readlines()

#trainer = ListTrainer(chatbot)

#trainer.train(conv)

def main():
    while True:
        request = Jarvis.takeCommand()
        response = chatbot.get_response(request)

        Jarvis.speak(response)
        print('Jarvis: ', response)
        if "exit" in request or "quit" in request or "bye" in request:
            Jarvis.speak("bye sir,Thanks for talking with me")
            print("Jarvis: bye sir,Thanks for talking with me")
            exit()