
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3

engine = pyttsx3.init()

chatbot = ChatBot(
	"Asily",
	trainer = "chatterbot.trainers.ChatterBotCorpusTrainer", 
	)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.custom")



while True:
	usuario = input(">>> ") 
	respuesta = chatbot.get_response(usuario) 
	engine.say("Bot: "+str(respuesta))
	engine.runAndWait()
	engine.stop()

	
