import pandas as pd

df = pd.read_csv(r'./data/Food_Nutrition_Dataset.csv')

def get_nutrient_categories():
  return df.columns[1:]

def get_min_value(nutrient=None):
  if nutrient:
    return round(min(df[nutrient]), 2)
  else:
    numeric_df = df.iloc[:, 1:]
    value = numeric_df.values.min()
    return value

def get_max_value(nutrient=None):
  if nutrient:
    return round(max(df[nutrient]), 2)
  else:
    numeric_df = df.iloc[:, 1:]
    value = numeric_df.values.max()
    return value

def db_search(food_item_name, range_filtered_nutrient = None, range_values= None, excluded_nutrient= None):
    food_item_name = food_item_name.lower()  # Convert to lowercase for case-insensitive matching
    filtered_df = df[df['food'].str.lower().str.contains(food_item_name)]

    if range_filtered_nutrient and range_values:
        min_val, max_val = range_values
        filtered_df = filtered_df[(filtered_df[range_filtered_nutrient] >= min_val) & (filtered_df[range_filtered_nutrient] <= max_val)]

    if excluded_nutrient:
        filtered_df = filtered_df[filtered_df[excluded_nutrient] == 0]

    return filtered_df[['food']].drop_duplicates()


def get_nutritional_info(food):
  # return (df['food'] == food)
  filtered_df = df[df['food'] == food]
  nutritional_info = filtered_df.iloc[0].drop('food').to_dict()
  top_nutrients = dict(list(nutritional_info.items())[:5])
  return top_nutrients

def get_nutrient_value(food, nutrient):
  value = df.loc[df['food'] == food, nutrient].values[0]
  return round(float(value), 2)

def get_all_food():
   return (df['food'])

def get_unit(nutrient):
    """
    Returns the unit for a given nutrient (g for grams or mg for milligrams).
    
    Parameters:
        nutrient (str): The name of the nutrient.
    
    Returns:
        str: The unit (g or mg).
    """
    nutrients_in_grams = {"Fat", "Saturated Fats", "Monounsaturated Fats", "Polyunsasturated Fats",
                          "Carbohydrates", "Sugars", "Protein", "Dietary Fiber", "Sodium", "Water"}
    
    if nutrient == "Caloric Value":
      return "kcal"
    elif nutrient in nutrients_in_grams:
      return "g"
    else:
      return "mg"

def calculate_nutrient_limits(nutrient, level):
  highest = get_max_value(nutrient)
  if level == "Low":
      min = 0
      max = highest * 0.33
  elif level == "Mid":
      min = highest * 0.33
      max = highest * 0.66
  elif level == "High":
      min = highest * 0.66
      max = highest
  elif level == None:
     min = get_min_value(nutrient)
     max = highest

    
  return min, max
