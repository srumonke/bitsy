import discord
import key
from neuralintents import GenericAssistant
import nltk



client = discord.Client()
@client.event
async def on_ready():
    print("connected")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!bitsy"):
        responce = chatbot.request(message.content[9:])
        await message.channel.send(responce)





if __name__=="__main__":
    nltk.download("omw-1.4")
    chatbot = GenericAssistant("intents-bits.json")
    chatbot.train_model()
    chatbot.save_model()
    print("model done training and saving")




    client.run(key.TOKEN)