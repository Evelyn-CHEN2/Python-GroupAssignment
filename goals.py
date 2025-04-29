from database import get_nutrient_value

# MIN and MAX values for validation
MIN_GOAL_VALUE = 0
MAX_GOAL_VALUE = 1000
MIN_AMOUNT_VALUE = 0
MAX_AMOUNT_VALUE = 500

temp_user_goals = []

# Dictionary to store user goals, current intake and estimated intake
user_goals = {}
current_intake = {}
estimated_intake = {}

def validate_goal_input(nutrient, value):
    """
    Validates the user's goal input for a specific nutrient.
    
    Parameters:
        nutrient (str): The name of the nutrient.
        value (int): The goal value set by the user.
    
    Returns:
        (bool, str): A tuple containing whether the input is valid and an error message (if any).
    """
    if nutrient == "":
        return True, ""

    if nutrient in temp_user_goals:
        return False, "Error: You cannot select the same nutrient category more than once."
        
    try:
        value = int(value)
    except:
        return False, "Error: The goal must be a numeric integer."
        
    if value < MIN_GOAL_VALUE or value > MAX_GOAL_VALUE:
        return False, f"Error: The goal must be between {MIN_GOAL_VALUE} and {MAX_GOAL_VALUE}."
        
    return True, ""

def set_goals(inputs):
    """
    Sets the user's nutritional goals based on input.

    Parameters:
        inputs (list of tuples): Each tuple contains a nutrient and a goal value.
    
    Returns:
        str or None: Returns an error message if validation fails, or None if successful.
    """

    # validation
    global temp_user_goals
    temp_user_goals = []
    for nutrient, goal in inputs:
        success, message = validate_goal_input(nutrient, goal)
        temp_user_goals.append(nutrient)
        if not(success):
            return message  # Return the error message if validation fails

    # setting
    for nutrient, goal in inputs:
        user_goals[nutrient] = int(goal)
        current_intake[nutrient] = 0    # Initialize current intake for each nutrient
        estimated_intake[nutrient] = 0  # Initialize estimated intake for each nutrient
    
    return None  # Return None to indicate success
        
def validate_amount_input(amount):
    """
    Validates the amount input.
    
    Parameters:
        amount (int): The amount value set by the user.
    
    Returns:
        str: An error message (if any).
    """
    try:
        amount = int(amount)
    except:
        return "Error: The amount must be a numeric integer."
    
    if amount < MIN_AMOUNT_VALUE or amount > MAX_AMOUNT_VALUE:
        return f"Error: The amount must be between {MIN_AMOUNT_VALUE} and {MAX_AMOUNT_VALUE}."
    
    return ""

def calculate_estimated_intake(food, amount):
    """
    Calculates the estimated nutrient intake based on the selected food and amount.

    Parameters:
    food (str): The selected food item for which the nutrient intake is calculated.
    amount (int or float): The amount of food in grams.
    """
    for nutrient in user_goals:
        nutrient_value = get_nutrient_value(food, nutrient)
        estimated_intake[nutrient] = round(nutrient_value * amount / 100, 2)
    return estimated_intake

def update_actual_intake():
    """
    Updates the progress toward the user's nutritional goals by confirming the estimated intake 
    and resetting the estimated values after the update.
    """
    for nutrient in user_goals:
         # Add the estimated intake to the current intake
        current_intake[nutrient] += estimated_intake[nutrient]
        # Reset the estimated values to 0 after updating the current intake
        estimated_intake[nutrient] = 0

def reset_current_intake():
    """
    Resets the current intake values for all nutrients.
    """
    for nutrient in user_goals:
        current_intake[nutrient] = 0

def reset_estimated_intake():
    """
    Resets the current intake values for all nutrients.
    """
    for nutrient in user_goals:
        estimated_intake[nutrient] = 0

def get_current_intake():
    return current_intake

def get_user_goals():
    return user_goals

def get_estimated_intake():
    return estimated_intake

def is_estimated_intake_exceeded(nutrient):
    total_estimated_intake = estimated_intake[nutrient] + current_intake[nutrient]
    # Set True if the total intake exceeds the goal, False otherwise
    return total_estimated_intake > user_goals[nutrient]
