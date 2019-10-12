from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import json
import telegram

class ActionFaqEstagio(Action):
	def name(self):
		return 'action_faq_estagio'
	def run(self, dispatcher, tracker, domain):
		bot = telegram.Bot(token='ACCESS_TOKEN')
		bot.send_document(chat_id=tracker.sender_id,document='https://aprender.ead.unb.br/pluginfile.php/688847/mod_resource/content/5/faq_estagio_supervisionado.pdf')
