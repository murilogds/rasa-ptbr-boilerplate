from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionFaqEstagio(Action):
	def name(self):
		return 'action_faq_estagio'
	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message('Calma aí, rapidinho!')
		dispatcher.utter_message('Vou buscar isso daí para você')
		dispatcher.utter_template("utter_faq_estagio",tracker)