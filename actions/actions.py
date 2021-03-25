# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.events import event
from actions.MongoConnect import getFromMongo
from actions.wikiGetter import getFromwikipedia

class Actionwebinarname(Action):

    def name(self) -> Text:
        return "action_webinar_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarname = event()['name']
        dispatcher.utter_message(template="utter_webinar_name", webinarname=webinarname)

        return []
class Actionwebinardate(Action):

    def name(self) -> Text:
        return "action_webinar_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinardate = event()['datetime']
        dispatcher.utter_message(template="utter_webinar_date", webinardate=webinardate)
        return []
class Actionwebinarparticipant(Action):

    def name(self) -> Text:
        return "action_webinar_participants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarparticipants = event()['participants']
        dispatcher.utter_message(template="utter_webinar_participants", webinarparticipants=webinarparticipants)
        return []
class Actionwebinarduration(Action):

    def name(self) -> Text:
        return "action_webinar_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarduration = event()['duration']
        dispatcher.utter_message(template="utter_webinar_duration", webinarduration=webinarduration)
        return []
class Actionwebinarinstructor(Action):

    def name(self) -> Text:
        return "action_webinar_instructor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarinstructor = event()['instuctor']
        dispatcher.utter_message(template="utter_webinar_instructor", webinarinstructor=webinarinstructor)
        return []
class Actionwebinardomain(Action):

    def name(self) -> Text:
        return "action_webinar_domain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinardomain = event()['domain']
        dispatcher.utter_message(template="utter_webinar_domain", webinardomain=webinardomain)
        return []
class Actionwebinarcontent(Action):

    def name(self) -> Text:
        return "action_webinar_content"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarcontent = event()['content']
        dispatcher.utter_message(template="utter_webinar_content", webinarcontent=webinarcontent)
        return []
class Actionwebinarregistration(Action):

    def name(self) -> Text:
        return "action_webinar_registration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idEvent= 2
        webinarlink = event()['registrationLink']
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
        idEvent= 2
        webinar = event()
        webinarname = webinar['name']
        webinardate = webinar['datetime']
        webinarduration = webinar['duration']
        webinarinstructor = webinar['instuctor']
        webinarlink = webinar['registrationLink']
        dispatcher.utter_message(template="utter_webinar_details", webinarname=webinarname ,webinardate=webinardate , webinarduration=webinarduration, webinarinstructor=webinarinstructor , webinarlink=webinarlink)
        return []
class Actionjobs(Action):

    def name(self) -> Text:
        return "action_jobs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        key= "tassahil AI developer"
        jobs = (getFromMongo()['JobTitle']) 
        company = (getFromMongo()['Company']) 
        dispatcher.utter_message(template="utter_jobs", jobs=jobs , company=company)
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