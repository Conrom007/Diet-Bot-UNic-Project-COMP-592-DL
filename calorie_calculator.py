import openfoodfacts
import re

def calories_calc(foods,quantities):
    total_calories = 0
    for entry in range(len(foods)):
        
        calories_result = openfoodfacts.products.search(foods[entry])
        quantity = quantities[entry]
        if bool(re.search('[a-zA-Z ]',quantity)) == True:
            quantity = re.sub("[^0123456789\.]","",quantity)
            print(quantity)
            total_calories += (calories_result['products'][0].get('nutriments').get('energy-kcal_100g') * int(quantity)/100)
        else:
            total_calories += (calories_result['products'][0].get('nutriments').get('energy-kcal_100g') * int(quantity))
    total_calories = round(total_calories)
    return total_calories

           
foods = ['hambuger', 'ground beef']
quantities = ['1','150g']
#2print(calories_calc(foods,quantities))
#print(quantities[1])
#print(len(quantities))

#2for i in range(len(quantities)):
#2    print(quantities[i])
#2    print(re.search('[a-zA-Z ]',quantities[i]))
#2print(calories_calc(foods,quantities))
