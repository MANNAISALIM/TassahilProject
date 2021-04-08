from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.MongoConnect import getWebinarDetailsFromMongo
from actions.MongoConnect import getAiInfoFromMongo
from actions.wikiGetter import getFromwikipedia


#Actions for webinar details
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
# actions with wekipedia
class Actionhelloworld(Action):


    def name(self) -> Text:
        return "action_fromwekipedia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        helloworld = getFromwikipedia("hello world program")
        dispatcher.utter_message(template="utter_fromwekipedia", helloworld=helloworld)
        return []
#actions for getting information for AI 
class ActionAIDefintion(Action):

    def name(self) -> Text:
        return "action_definition_of_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("title")
        Definition = ""
        try:
            try: 
                try:
                    Definition = (getAiInfoFromMongo(name.lower())['Definition']) 
                except KeyError:
                    Definition = (getAiInfoFromMongo(name.capitalize())['Definition'])
            except KeyError:
                Definition = (getAiInfoFromMongo(name.upper())['Definition'])
        except KeyError:
            print("********** From wekipedia **************")   
            Definition = getFromwikipedia(name.lower())  
        except wikipedia.exceptions.PageError:
            Definition =" actually, i don't know what you mean exactly."   
        dispatcher.utter_message(template="utter_definition_of_ai_component", definition=Definition)
        return []
class ActionAIstart(Action):

    def name(self) -> Text:
        return "action_start_with_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("title")
        start = ""
        try:
            try: 
                start = (getAiInfoFromMongo(name.lower())['HowToStart']) 
            except KeyError:
                start = (getAiInfoFromMongo(name.capitalize())['HowToStart'])
        except KeyError:
                start = (getAiInfoFromMongo(name.upper())['HowToStart'])
        dispatcher.utter_message(template="utter_start_with_ai_component", start=start)
        return []
class ActionAIversion(Action):

    def name(self) -> Text:
        return "action_version_of_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_version_of_ai_component")
        return []
class ActionAIwebsite(Action):

    def name(self) -> Text:
        return "action_website_to_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("title")
        website = ""
        try:
            try: 
                website = (getAiInfoFromMongo(name.lower())['WebSite']) 
            except KeyError:
                website = (getAiInfoFromMongo(name.capitalize())['WebSite'])
        except KeyError:
                website = (getAiInfoFromMongo(name.upper())['WebSite'])
        dispatcher.utter_message(template="utter_website_to_ai_component", website=website)
        return []
class ActionAInext(Action):

    def name(self) -> Text:
        return "action_next_step_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("title")
        next = ""
        try:
            try: 
                next = (getAiInfoFromMongo(name.lower())['WhatIsTheNext']) 
            except KeyError:
                next = (getAiInfoFromMongo(name.capitalize())['WhatIsTheNext'])
        except KeyError:
                next = (getAiInfoFromMongo(name.upper())['WhatIsTheNext'])
        dispatcher.utter_message(template="utter_next_step_ai_component", next=next)
        return []
class ActionAIimage(Action):

    def name(self) -> Text:
        return "action_architecture_of_ai_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("title")
        image = ""
        try:
            try: 
                image = (getAiInfoFromMongo(name.lower())['Architucture(Image)']) 
            except KeyError:
                image = (getAiInfoFromMongo(name.capitalize())['Architucture(Image)'])
        except KeyError:
                image = (getAiInfoFromMongo(name.upper())['Architucture(Image)'])
        dispatcher.utter_message(template="utter_architecture_of_ai_component", image=image)
        return []