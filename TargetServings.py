'''
Given an array of objects representing ingredients (each with a name and amount per serving), 
and a target number of servings, write a function to calculate the required amount of each 
ingredient for the target servings.
'''
ingredients = [
  {'name': 'flour', 'amount': 200 }, # 200g per
  {'name': 'sugar', 'amount': 100 }, # 100g per
  {'name': 'eggs', 'amount': 2 }     # 2 eggs per
]
target_servings = 3

def calculate_ingredients(ingredients, target_servings):
    return [{'name': i['name'], 'amount': i['amount'] * target_servings} for i in ingredients]

print(calculate_ingredients(ingredients, target_servings))