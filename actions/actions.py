from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.interfaces import ActionExecutionRejection
from rasa_sdk.types import DomainDict


#**************************************************Welcome greet to user*******************************************

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        dispatcher.utter_message(response="utter_options")
        return []
    
#**************************************************Welcome greet to user*******************************************

#**************************************************4 usecases of application*******************************************

class ActionComplaint(Action):
    def name(self) -> Text:
        return "action_complaint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_complaint")
        return []

class ActionTrackComplaint(Action):
    def name(self) -> Text:
        return "action_track_complaint"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_track_complaint")
        return []

class ActionSuggestion(Action):
    def name(self) -> Text:
        return "action_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_suggestion")
        return []

class ActionApplyService(Action):
    def name(self) -> Text:
        return "action_apply_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_apply_service")
        return []

#**************************************************4 usecases of application*******************************************


#**************************************************Raise a complaint form*******************************************

# class ComplaintForm(Action):
#     def name(self) -> Text:
#         return "complaint_form"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_ask_username")
#         return []

# class ActionSubmitComplaint(Action):
#     def name(self) -> Text:
#         return "action_submit_complaint"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> List[Dict[Text, Any]]:
#         username = tracker.get_slot("username")
#         email = tracker.get_slot("email")
#         location = tracker.get_slot("location")
#         complaint_details = tracker.get_slot("complaint_details")
#         attachments = tracker.get_slot("attachments")

#         # Perform necessary actions with the collected complaint information
#         print(username,'\n',email,'\n',location,'\n',complaint_details,'\n',attachments)

#         dispatcher.utter_message(template="utter_complaint_submission_confirmation")
#         return []

# class ActionFallback(Action):
#     def name(self) -> Text:
#         return "action_fallback"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_fallback")
#         return []

#**************************************************Raise a complaint form*******************************************
