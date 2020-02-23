#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Create a chatbot
bot=ChatBot('Candice')

## 
# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)




#training on english dataset
for files in os.listdir('./bengali/'):
    data=open('./bengali/'+files,'r').readlines()
    trainer.train(data)#chat feature
while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Candice:',reply)
    if message.strip()=='Bye':
        print('Candice: Bye')
        break