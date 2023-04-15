from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionRespostaUtil(Action):

    def name(self) -> Text:
        return "action_resposta_util"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mensagem = "Essa resposta foi útil? (responda com sim ou não)"
        dispatcher.utter_message(text=mensagem)

        return []


class ActionProximaPergunta(Action):

    def name(self) -> Text:
        return "action_proxima_pergunta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resposta = tracker.latest_message.get('text').lower()

        if resposta == "sim":
            mensagem = "Tem mais alguma pergunta?"
            dispatcher.utter_message(text=mensagem)

        elif resposta == "não":
            mensagem = "Poderia refazer a pergunta"
            dispatcher.utter_message(text=mensagem)

        return []

class ActionSessionStart(Action):

    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Incluindo uma mensagem de saudação
        dispatcher.utter_message(text="Olá! Que bom ter você aqui! Sou um chatbot especializado em responder perguntas sobre o Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Universidade Estadual do Ceará. Como posso ajudá-lo(a) hoje?")

        return []
