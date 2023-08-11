# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from rasa_sdk.executor import CollectingDispatcher
import asyncio
import threading




class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         user_id = tracker.sender_id
         dispatcher.utter_message(text=f"Your ID is: {user_id} ")
         print(user_id)
         return[SlotSet("usr_ID", user_id)]


from database_connectivity import Data_Update
from extractor_custom_model import extract_entities
from calorie_calculator import calories_calc

class ActionSubmit(Action):
  def name(self) -> Text: 
        
    return "action_submit"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    user_ID = tracker.get_slot("usr_ID")
    food = tracker.get_slot("food_choice")
    quantity =  tracker.get_slot("quantity")
    calories =  tracker.get_slot("calories")
    protein =  tracker.get_slot("protein")
    carbs = tracker.get_slot("carbs")
    fat = tracker.get_slot("fat")
    sugar = tracker.get_slot("sugar")
    sodium = tracker.get_slot("sodium")
    Data_Update(user_ID,food, quantity, calories, protein ,carbs, fat, sugar, sodium)
    
    return[]

from correct_matcher import matcher, calorie_match, protein_match, carbohydrate_match, fat_match, sugar_match, sodium_match
from extractor_custom_model import extract_entities
import pandas as pd
from fuzzywuzzy import process
import csv

class ActionMatchFood(Action):
  def name(self) -> Text: 
        
    return "action_match_food"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    food = tracker.get_slot("food")
    food_list = [food]
    print(food)
    print(food_list)
    foods , food_quantities = extract_entities(food_list)
    print(foods, '~', food_quantities)
    message = "Which one of these food items did you mean?"
    
    for food_item in foods:      
      matches = matcher(food_item)
      print(matches)
      print(str(matches[0][0]))
      #Get the top 3 matches

      # Check if the highest match has a 90 or higher confidence
      if matches[0][1] >= 91:
        # Send a message to the user with the match
        return [SlotSet("buttons_used", False),SlotSet("food_choice", matches[0][0]), SlotSet("quantity", food_quantities[0])]

      # If the highest match doesn't have a 90 or higher confidence, present the top 3 matches as buttons
      else:
        buttons = []
        for match in matches:
          buttons.append({"title": match[0], "payload": match[0]})

        # Send a message to the user with the buttons
        message = f"Sorry, I couldn't find an exact match for '{food}'. Which of these is the closest?"
        dispatcher.utter_message(text=message, buttons=buttons)
      
        return [SlotSet("buttons_used", True),SlotSet("quantity", food_quantities[0])]


class ActionFood_Set(Action):
  def name(self) -> Text: 
        
    return "action_food_set"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    choice = str((tracker.latest_message)['text'])
    return [SlotSet("food_choice",choice)]


      
class ActionMatchSelectionCalories(Action):
  def name(self) -> Text: 
        
    return "action_match_selection_calories"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    selected_match = tracker.get_slot("food_choice")
    quantity = tracker.get_slot("quantity")
    calories = calorie_match(str(selected_match), str(tracker.get_slot('quantity')))
    protein =  protein_match(str(selected_match), str(tracker.get_slot('quantity')))
    carbs = carbohydrate_match(str(selected_match), str(tracker.get_slot('quantity')))
    fat = fat_match(str(selected_match), str(tracker.get_slot('quantity')))
    sugar = sugar_match(str(selected_match), str(tracker.get_slot('quantity')))
    sodium = sodium_match(str(selected_match), str(tracker.get_slot('quantity')))
    dispatcher.utter_message(text=f"{quantity} of {selected_match} has {calories} calories.")
    return [SlotSet("calories",calories),SlotSet("protein",protein),SlotSet("carbs",carbs),SlotSet("fat",fat),SlotSet("sugar",sugar),SlotSet("sodium",sodium),]

class ActionResetAllSlots(Action):
    
  def name(self):
      return "action_reset_all_slots"

  def run(self, dispatcher, tracker, domain):
      
      user_id = tracker.sender_id
      return[AllSlotsReset(),SlotSet("usr_ID", user_id)]



from scheduler import Scheduled_Message
from threading import Thread

          
class ActionScheduledReminder(Action):
  def name(self) -> Text: 
        
    return "action_scheduled_reminder"
  
  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    background_process = Thread(target = Scheduled_Message,name = 'Scheduler', args = (0,3), daemon=True)
    background_process.start()
    
    return []

class ActionRestartCustom(Action):
  """ This is restarts the conversation to allow multiple intent triggering"""
  def name(self):
      return "action_restart_custom"
    
  def run(self, dispatcher, tracker, domain):
      return [Restarted(),SlotSet("usr_ID", tracker.sender_id) ]
    
    


