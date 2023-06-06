from typing import Any, Text, Dict, List, Union
from rasa_sdk import Tracker, FormValidationAction, Action
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

# class ActionComplaint(Action):
#     def name(self) -> Text:
#         return "action_complaint"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_complaint")
#         return []

# class ActionTrackComplaint(Action):
#     def name(self) -> Text:
#         return "action_track_complaint"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_track_complaint")
#         return []

# class ActionSuggestion(Action):
#     def name(self) -> Text:
#         return "action_suggestion"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_suggestion")
#         return []

# class ActionApplyService(Action):
#     def name(self) -> Text:
#         return "action_apply_service"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(response="utter_apply_service")
#         return []

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

#****************************************RAISE_COMPLAINT****************************************************
class ValidateComplaintForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_raise_complaint_form"

    def validate_r_username(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your user name is {slot_value}.")
        return {"r_username": slot_value}
    
    def validate_r_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your email is {slot_value}.")
        return {"r_email": slot_value}
    

    def validate_r_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your location is {slot_value}.")
        return {"r_location": slot_value}

    def validate_r_complaint_details(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint details is {slot_value}.")
        return {"r_complaint_details": slot_value}
    
    def validate_r_attachments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your attachments is {slot_value}.")
        return {"r_attachments": slot_value}
    
class ActionClearComplaintSlots(Action):
    def name(self) -> Text:
        return "action_clear_complaint_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["r_username", "r_email", "r_location", "r_complaint_details", "r_attachments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
#****************************************RAISE_COMPLAINT****************************************************    

#****************************************TRACK COMPLAINT******************************************************   
class ValidateTrackComplaintForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_track_complaint_form"
    
    def validate_t_complaint_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint number is {slot_value}.")
        return {"t_complaint_number": slot_value}
    
    def validate_t_comments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your comment is {slot_value}.")
        return {"t_comments": slot_value}

class ActionClearTrackSlots(Action):
    def name(self) -> Text:
        return "action_clear_track_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["t_complaint_number", "t_comments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
#****************************************TRACK COMPLAINT******************************************************

#****************************************SUGGESTIONS**********************************************************
class ValidateSuggestionForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_suggesstion_form"

    def validate_r_username(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your user name is {slot_value}.")
        return {"r_username": slot_value}
    
    def validate_r_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your email is {slot_value}.")
        return {"r_email": slot_value}
    

    def validate_r_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your location is {slot_value}.")
        return {"r_location": slot_value}

    def validate_s_suggestions(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint details is {slot_value}.")
        return {"s_suggestions": slot_value}
    
    def validate_s_attachments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your attachments is {slot_value}.")
        return {"s_attachments": slot_value}
    
class ActionClearSuggestionSlots(Action):
    def name(self) -> Text:
        return "action_clear_suggestions_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["r_username", "r_email", "r_location", "s_suggestions", "s_attachments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
#****************************************SUGGESTIONS**********************************************************