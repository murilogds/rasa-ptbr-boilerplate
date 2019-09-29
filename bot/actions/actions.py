from rasa_core_sdk import Action

class ActionAtividadesEstagio(Action):
	def name(self):
		return "action_atividades_estagio"
	def run(self, dispatcher, tracker, domain):
		try:
			topico = '0'
			with open('actions/Perguntas_do_BOT.txt','r') as file:
				for line in file:
					if line[1] == '.':
						topico = line[0]
						continue
					if topico == '1':
						dispatcher.utter_message("{}".format(line))
		except ValueError:
			dispatcher.utter_message(ValueError)
        
