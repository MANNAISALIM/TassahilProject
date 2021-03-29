# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.MongoConnect import getWebinarDetailsFromMongo
from actions.wikiGetter import getFromwikipedia

class Actionwebinarname(Action):

    def name(self) -> Text:
        return "action_webinar_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarname = (getWebinarDetailsFromMongo()['name']) 
        dispatcher.utter_message(template="utter_webinar_name", webinarname=webinarname)

        return []
class Actionwebinardate(Action):

    def name(self) -> Text:
        return "action_webinar_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinardate = (getWebinarDetailsFromMongo()['datetime']) 
        dispatcher.utter_message(template="utter_webinar_date", webinardate=webinardate)
        return []
class Actionwebinarparticipant(Action):

    def name(self) -> Text:
        return "action_webinar_participants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarparticipants = (getWebinarDetailsFromMongo()['participants']) 
        dispatcher.utter_message(template="utter_webinar_participants", webinarparticipants=webinarparticipants)
        return []
class Actionwebinarduration(Action):

    def name(self) -> Text:
        return "action_webinar_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarduration = (getWebinarDetailsFromMongo()['duration']) 
        dispatcher.utter_message(template="utter_webinar_duration", webinarduration=webinarduration)
        return []
class Actionwebinarinstructor(Action):

    def name(self) -> Text:
        return "action_webinar_instructor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarinstructor = (getWebinarDetailsFromMongo()['instructor']) 
        dispatcher.utter_message(template="utter_webinar_instructor", webinarinstructor=webinarinstructor)
        return []
class Actionwebinardomain(Action):

    def name(self) -> Text:
        return "action_webinar_domain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinardomain = (getWebinarDetailsFromMongo()['domain']) 
        dispatcher.utter_message(template="utter_webinar_domain", webinardomain=webinardomain)
        return []
class Actionwebinarcontent(Action):

    def name(self) -> Text:
        return "action_webinar_content"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarcontent = (getWebinarDetailsFromMongo()['content']) 
        dispatcher.utter_message(template="utter_webinar_content", webinarcontent=webinarcontent)
        return []
class Actionwebinarregistration(Action):

    def name(self) -> Text:
        return "action_webinar_registration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarlink = (getWebinarDetailsFromMongo()['registraion_link']) 
        dispatcher.utter_message(template="utter_webinar_registration", webinarlink=webinarlink)
        return []
class Actionwebinarcost(Action):

    def name(self) -> Text:
        return "action_webinar_cost"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_webinar_cost")
        return []
class Actionwebinardetails(Action):


    def name(self) -> Text:
        return "action_webinar_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webinarname = (getWebinarDetailsFromMongo()['name']) 
        webinardate = (getWebinarDetailsFromMongo()['datetime']) 
        webinarduration = (getWebinarDetailsFromMongo()['duration']) 
        webinarinstructor = (getWebinarDetailsFromMongo()['instructor']) 
        webinarlink = (getWebinarDetailsFromMongo()['registraion_link']) 
        dispatcher.utter_message(template="utter_webinar_details", webinarname=webinarname ,webinardate=webinardate , webinarduration=webinarduration, webinarinstructor=webinarinstructor , webinarlink=webinarlink)
        return []

class Actionhelloworld(Action):

    def name(self) -> Text:
        return "action_fromwekipedia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        helloworld = getFromwikipedia()
        dispatcher.utter_message(template="utter_fromwekipedia", helloworld=helloworld)
        return []