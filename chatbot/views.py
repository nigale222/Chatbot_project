from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

import time
time.clock = time.time

bot = ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                        'import_path':'chatterbot.logic.BestMatch',
                        # 'default_response':'Sorry, I dont know what that means',
                        # 'maximum_similarity_threshold':0.90

                    }
                    ])

list_to_train = [
    "hi",
    "hi, there",
    "what's your name?",
    "I'm just a chatbot",
    "what is your fav food?",
    "I like cheese",
    "what is your fav sport?",
    "Cricket",
    "do you have childrens?",
    "No"
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'chatbot/index.html')
def specific(request):
    number = 55
    return HttpResponse(number)
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
