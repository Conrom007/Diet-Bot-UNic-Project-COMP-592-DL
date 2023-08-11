from extractor_custom_model import extract_entities
from calorie_calculator import calories_calc

breakfast = ['250 ml milk', '120g oats']
lunch = ['120g ground beef, 330 ml original coca-cola']
dinner = ['1 cheeseburger']
snack = ['1 banana']
breakfast_list = []
lunch_list = []
dinner_list = []
snack_list = []
breakfast_list = list(breakfast)
lunch_list = lunch_list + lunch
dinner_list = dinner_list + dinner
snack_list = snack_list + snack
print(breakfast_list)
breakfast_foods , breakfast_quantities = extract_entities(breakfast_list)
lunch_foods , lunch_quantities = extract_entities(lunch_list)
dinner_foods , dinner_quantities = extract_entities(dinner_list)
snack_foods , snack_quantities = extract_entities(snack_list)

print(breakfast_foods)
print(breakfast_quantities)
print(lunch_foods)
print(lunch_quantities)

calories = calories_calc(breakfast_foods , breakfast_quantities) + calories_calc(lunch_foods , lunch_quantities) + calories_calc(dinner_foods , dinner_quantities) + calories_calc(snack_foods , snack_quantities)

print(calories)
print(lunch_quantities)