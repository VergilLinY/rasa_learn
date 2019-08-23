# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionDialogueCompletionDetect(Action):
    """
    用于判断是否收集到所有需要的信息，如果没有收集全就提问
    """
    def name(self) -> Text:
        return "action_dialogue_completion_detect"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")
        # TODO
        return []


class ActionVoiceprintVerification(Action):
    def name(self) -> Text:
        return "action_voiceprint_verification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Now loading voiceprint verification...")
        dispatcher.utter_message("Verification adopt")
        return []


# 记录是否在市区的事件
class ActionRecordInCity(Action):
    def name(self) -> Text:
        return "action_record_in_city"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_in_city", "in_city")]


class ActionRecordOutCity(Action):
    def name(self) -> Text:
        return "action_record_out_city"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_in_city", "out_city")]


# 记录工作是否变动的事件
class ActionRecordNoJobExchange(Action):
    def name(self) -> Text:
        return "action_record_no_job_exchange"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_job_exchange", "job_regular")]


class ActionRecordJobExchange(Action):
    def name(self) -> Text:
        return "action_record_job_exchange"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_job_exchange", "job_exchange")]


# 记录健康状况的事件
class ActionRecordHealth(Action):
    def name(self) -> Text:
        return "action_record_health"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_health_OK", "ok")]


class ActionRecordUnhealth(Action):
    def name(self) -> Text:
        return "action_record_unhealth"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("is_health_OK", "not_good")]


# 记录是否获批离市的事件
class ActionRecordLeaveApproval(Action):
    def name(self) -> Text:
        return "action_record_leave_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("leave_approval_status", "hold_approval")]


class ActionRecordNoLeaveApproval(Action):
    def name(self) -> Text:
        return "action_record_no_leave_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("leave_approval_status", "without_approval")]


# 检测是否已经申请离市
class ActionDetectiveApproval(Action):
    def name(self) -> Text:
        return "action_detective_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Now in ActionDetectiveApproval.//TODO")
        return []
