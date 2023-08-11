
import pandas as pd
from fuzzywuzzy import process
import re

def matcher(query):
    #set number of matches
    n = 3
    # Load CSV file into a pandas dataframe
    df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')

    # Get list of all names
    choices = list(df['name'])

    # Find the 3 closest matches to the query
    matched_food_names = process.extract(query, choices, limit = n)
    """
    #check if item with over 90 match confidence exists
    confidence_90_counter = 0
    for food in matched_food_names: 
      if food[1] > 90:
        confidence_90_counter += 1
      else:
        confidence_90_counter += 0
    #if match with confidence > 90 exists return it else return top 3 matches
      if confidence_90_counter > 0:
        return matched_food_names[0]
      else:
        return [(match) for match in matched_food_names]"""
    return matched_food_names

matcher('chicken sandwich')



def calorie_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]

  serving = int(re.sub('\D', '', serving_with_unit))
  quantity = int(re.sub('\D', '', quantity))

  calories = (quantity / serving) * df['calories'].iloc[0]
  return(calories)

def protein_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]
  macro_with_unit = df['protein'].iloc[0]
  print(macro_with_unit)

  serving = float(re.sub('[^\d.]', '', serving_with_unit))
  quantity = float(re.sub('[^\d.]', '', quantity))
  macro = float(re.sub('[^\d.]', '', macro_with_unit))
  print(macro)
  protein = (quantity / serving) * macro
  return(protein)
 
def carbohydrate_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]
  macro_with_unit = df['carbohydrate'].iloc[0]

  serving = float(re.sub('[^\d.]', '', serving_with_unit))
  quantity = float(re.sub('[^\d.]', '', quantity))
  macro = float(re.sub('[^\d.]', '', macro_with_unit))

  carbohydrates = (quantity / serving) * macro
  return(carbohydrates)     
 
def fat_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]
  macro_with_unit = df['total_fat'].iloc[0]

  serving = float(re.sub('[^\d.]', '', serving_with_unit))
  quantity = float(re.sub('[^\d.]', '', quantity))
  macro = float(re.sub('[^\d.]', '', macro_with_unit))

  fat = (quantity / serving) * macro
  return(fat)    
 
def sugar_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]
  macro_with_unit = df['sugars'].iloc[0]

  serving = float(re.sub('[^\d.]', '', serving_with_unit))
  quantity = float(re.sub('[^\d.]', '', quantity))
  macro = float(re.sub('[^\d.]', '', macro_with_unit))

  sugar = (quantity / serving) * macro
  return(sugar)    
 
def sodium_match(input, quantity):
  df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')
  df = df.loc[df['name'] == input]
  serving_with_unit = df['serving_size'].iloc[0]
  macro_with_unit = df['sodium'].iloc[0]

  serving = float(re.sub('[^\d.]', '', serving_with_unit))
  quantity = float(re.sub('[^\d.]', '', quantity))
  macro = float(re.sub('[^\d.]', '', macro_with_unit))

  sodium = (quantity / serving) * macro
  return(sodium)    




"""
def matcher_1(query):
    #set number of matches
    n = 1
    # Load CSV file into a pandas dataframe
    df = pd.read_csv('/content/nutrition - nutrition (1).csv')

    # Get list of all names
    choices = list(df['name'])

    # Find the 3 closest matches to the query
    matched_food_names = process.extract(query, choices, limit = n)

    #check if item with over 90 match confidence exists
    confidence_90_counter = 0
    for food in matched_food_names: 
      if food[1] > 90:
        confidence_90_counter += 1
      else:
        confidence_90_counter += 0
    #if match with confidence > 90 exists return it else return top 3 matches
      if confidence_90_counter > 0:
        return matched_food_names[0]
      else:
        return [(match) for match in matched_food_names]
    
def matcher_3(query):
    #set number of matches
    n = 3
    # Load CSV file into a pandas dataframe
    df = pd.read_csv('/Users/conrom007/Documents/Rasa Projects/Food Tracking Agent (RASA)/nutrition - nutrition (1).csv')

    # Get list of all names
    choices = list(df['name'])

    # Find the 3 closest matches to the query
    matched_food_names = process.extract(query, choices, limit = n)

    #check if item with over 90 match confidence exists
    confidence_90_counter = 0
    for food in matched_food_names: 
      if food[1] > 90:
        confidence_90_counter += 1
      else:
        confidence_90_counter += 0
    #if match with confidence > 90 exists return it else return top 3 matches
      if confidence_90_counter > 0:
        return matched_food_names[0]
      else:
        return [(match) for match in matched_food_names]
  """