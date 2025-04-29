import pytest
import pandas as pd
from unittest.mock import patch
from database import (get_nutrient_categories,
                      db_search,
                      get_nutritional_info,
                      get_nutrient_value,
                      get_all_food,
                      get_unit,
                      calculate_nutrient_limits, df, get_min_value, get_max_value)
from goals import (
                   set_goals,
                   get_current_intake,
                   get_user_goals,
                   get_estimated_intake,
                   reset_current_intake,
                   validate_goal_input,
                    validate_amount_input, calculate_estimated_intake,
                   user_goals , reset_estimated_intake,
                   estimated_intake,
                   current_intake,

                   is_estimated_intake_exceeded,
                   update_actual_intake, MIN_AMOUNT_VALUE, MAX_AMOUNT_VALUE)


#from Database.py
def test_get_nutrient_value():
    food= "cream cheese"
    nutrient= "Protein"
    result= get_nutrient_value(food,nutrient)
    assert isinstance(result,float), "The nutrient value should be a float"
    assert result>= 0, "Nutrient cant be a negative number"
    assert round(result,2)== result, "Nutrient should be rounded to 2 decimal places"


def test_get_nutrient_value_invalid():
    # non-existent food item should still raise IndexError
    with pytest.raises(IndexError) as exc_info:
        get_nutrient_value("nonexistent food", "Protein")
    assert "index 0 is out of bounds" in str(exc_info.value)
    # non-existent nutrient should raise KeyError
    with pytest.raises(KeyError) as exc_info:
        get_nutrient_value("cream cheese", "Nonexistent Nutrient")
    assert str(exc_info.value) == "'Nonexistent Nutrient'"


#from Goals.py
def test_get_min_value():
    nutrient= "Magnesium"
    result =get_min_value(nutrient)
    assert isinstance(result,float), "Min value must be a float"
    assert result >=0,"Minimum value cant be negative"


#from Goals.py
def test_get_max_value():
    nutrient ="Phosphorus"
    result =get_max_value(nutrient)
    assert isinstance(result,float), "Max value must be a float"
    assert result >=0,"Max value cant be negative"

def test_get_min_value_invalid():
    with pytest.raises(KeyError):
        get_min_value("InvalidNutrient")

def test_get_max_value_invalid():
    with pytest.raises(KeyError):
        get_max_value("InvalidNutrient")

#from Goals.py
def test_set_goals_and_get_current_intake():
    inputs= [("Sodium",50),("Zinc",200)]
    set_goals(inputs)

    current_intake =get_current_intake()
    assert isinstance(current_intake,dict), "Current intake should be a dictionary word"
    assert "Sodium" in current_intake, "Current intake should include Sodium"
    assert current_intake["Sodium"] ==0, "Initial current intake should be 0"
    assert "Zinc" in current_intake, "Current intake should include Zinc "
    assert current_intake["Zinc"] ==0, "Initial current intake for Zinc should be 0"

#from database.py
def test_get_nutrient_categories():
    categories =get_nutrient_categories()
    assert isinstance(categories, pd.Index),"Nutrient categories should return a pandas Index"
    assert len(categories) > 0,"Nutrient categories should not be empty"

def test_get_nutrient_categories_empty_dataset():
    with patch('database.df', pd.DataFrame()):
        categories = get_nutrient_categories()
        assert isinstance(categories, pd.Index), "Nutrient categories should return a pandas Index"
        assert len(categories) == 0, "Nutrient categories should be empty when the dataset is empty"


#from database.py
def test_get_all_food():
    all_food = get_all_food()
    assert isinstance(all_food,pd.Series), "All food items should return from dataset in pandas"
    assert not all_food.empty,"All food items should not be empty"

#from Goals.py
def test_get_nutritional_info():
    food = "chicken spread"
    nutritional_info = get_nutritional_info(food)
    assert isinstance(nutritional_info, dict),"Returned value should be a dictionary"
    assert nutritional_info,"Nutritional info should not be empty"

def test_get_nutritional_info_invalid_food():
    with pytest.raises(IndexError):
        get_nutritional_info("invalid food")

def test_validate_goal_input_empty_nutrient():
    result, message = validate_goal_input("", 50)
    assert result == True, "Empty nutrient should be valid"
    assert message == "", "No error message should be returned for empty nutrient"

def test_validate_goal_input_duplicate_nutrient():
    duplicate_nutrient = "Sodium"
    result, message = validate_goal_input(duplicate_nutrient, 50)
    assert result == False, "Duplicate nutrient should return False"
    assert message == "Error: You cannot select the same nutrient category more than once."

#from Database.py
def test_db_search():
    result = db_search("cheese")
    assert not result.empty, "Expected to find some cheese-related food items"
    assert isinstance(result, pd.DataFrame), "Expected result to be a DataFrame"



#from Database.py
def test_db_search_excluding_nutrient():
    result = db_search("cheese", excluded_nutrient="Sugars")
    assert not result.empty, "Expected to find cheese with 0 grams of sugar"
    food_items = result['food'].values
    filtered_nutrient_data = df[df['food'].isin(food_items)]
    assert 'Sugars' in filtered_nutrient_data.columns, "Sugars column should exist in the dataset"
    assert all(filtered_nutrient_data['Sugars'] == 0), "All results should have 0 grams of sugar"

def test_db_search_invalid_nutrient():
    with pytest.raises(KeyError):
        result = db_search("cheese", range_filtered_nutrient="InvalidNutrient", range_values=(0, 100))



def test_calculate_nutrient_limits_none_level():
    nutrient = "Protein"
    min_value, max_value = calculate_nutrient_limits(nutrient, None)
    assert min_value == get_min_value(nutrient)
    assert max_value == get_max_value(nutrient)



def test_reset_current_intake():
    inputs = [("Vitamin B1", 50), ("Vitamin A", 100)]
    set_goals(inputs)
    current_intake = get_current_intake()
    current_intake["Vitamin B1"] = 30
    current_intake["Vitamin A"] = 60
    reset_current_intake()
    current_intake_after_reset = get_current_intake()
    assert all(
        value == 0 for value in current_intake_after_reset.values()), "All current intake values should be reset to 0"

def test_get_estimated_intake():
    # Set example goals and some estimated intake values
    inputs = [("Cholesterol", 50), ("Dietary Fiber", 100)]
    set_goals(inputs)

    # Simulate adding some estimated intake
    estimated_intake = get_estimated_intake()
    assert isinstance(estimated_intake, dict), "estimated_intake should be a dictionary"
    assert "Cholesterol" in estimated_intake, "Cholesterol should be in estimated intake"
    assert estimated_intake["Cholesterol"] == 0, "Initially, Cholesterol estimated intake should be 0"
    assert "Dietary Fiber" in estimated_intake, "Dietary Fiber should be in estimated intake"
    assert estimated_intake["Dietary Fiber"] == 0, "Initially, Dietary Fiber estimated intake should be 0"

def test_get_user_goals():
    #pass in some inputs for testing
    inputs = [("Carbohydrates", 50), ("Fats", 100)]
    set_goals(inputs)
    user_goals = get_user_goals()
    assert isinstance(user_goals, dict), "user_goals should be a dictionary"
    assert "Carbohydrates" in user_goals, "Carbohydrates should be in user_goals"
    assert user_goals["Carbohydrates"] == 50, "Carbohydrates goal should be 50"
    assert "Fats" in user_goals, "Fats should be in user_goals"
    assert user_goals["Fats"] == 100, "Fats goal should be 100"

#from Database.py
def test_get_nutrient_min_value():
    min_value = get_min_value()
    assert isinstance(min_value, float), "Minimum value should be a float"
#from Database.py
def test_get_nutrient_max_value():
    max_value = get_max_value()
    assert isinstance(max_value, float), "Maximum value should be a float"

#from Database.py
def test_get_unit():
    assert get_unit("Protein") == "g"
    assert get_unit("Fat") == "g"
    assert get_unit("Saturated Fats") == "g"
    assert get_unit("Sodium") == "g", "Sodium is currently categorized as 'g' in the function"
    assert get_unit("Caloric Value") == "kcal"
    assert get_unit("Unknown Nutrient") == "mg"


def test_calculate_nutrient_limits_low():
    min_val, max_val = calculate_nutrient_limits("Protein", "Low")
    assert min_val == 0
    assert max_val == get_max_value("Protein") * 0.33

def test_calculate_nutrient_limits_mid():
    min_val, max_val = calculate_nutrient_limits("Protein", "Mid")
    assert min_val == get_max_value("Protein") * 0.33
    assert max_val == get_max_value("Protein") * 0.66

def test_calculate_nutrient_limits_high():
    min_val, max_val = calculate_nutrient_limits("Protein", "High")
    assert min_val == get_max_value("Protein") * 0.66
    assert max_val == get_max_value("Protein")

def test_calculate_nutrient_limits_invalid_level():
    with pytest.raises(UnboundLocalError) as exc_info:
        calculate_nutrient_limits("Protein", "Invalid")
    assert "cannot access local variable 'min' where it is not associated with a value" in str(exc_info.value)

#goals.py
def test_validate_goal_input_non_integer():
    success, message = validate_goal_input("Protein", "invalid")
    assert not success
    assert message == "Error: The goal must be a numeric integer."

#goals.py
def test_validate_goal_input_out_of_range():
    success, message = validate_goal_input("Protein", 1200)
    assert not success
    assert message == "Error: The goal must be between 0 and 1000."

def test_set_goals_validation_failure():
    inputs = [("Protein", "invalid")]
    result = set_goals(inputs)
    assert result == "Error: The goal must be a numeric integer."




def test_update_actual_intake():
    user_goals["Protein"] = 50
    estimated_intake["Protein"] = 20
    current_intake["Protein"] = 10
    update_actual_intake()
    assert current_intake["Protein"] == 30
    assert estimated_intake["Protein"] == 0

def test_is_estimated_intake_exceeded_true():
    user_goals["Protein"] = 50
    estimated_intake["Protein"] = 40
    current_intake["Protein"] = 20
    result = is_estimated_intake_exceeded("Protein")
    assert result is True

def test_is_estimated_intake_exceeded_false():
    user_goals["Protein"] = 50
    estimated_intake["Protein"] = 20
    current_intake["Protein"] = 10
    result = is_estimated_intake_exceeded("Protein")
    assert result is False


def test_calculate_estimated_intake():
    test_user_goals = {"Protein": 50, "Carbohydrates": 100}
    test_estimated_intake = {}
    with patch('goals.user_goals', test_user_goals), patch('goals.estimated_intake', test_estimated_intake):
        with patch('goals.get_nutrient_value') as mock_get_nutrient_value:
            # Mock the nutrient values
            mock_get_nutrient_value.side_effect = lambda food, nutrient: 10 if nutrient == "Protein" else 20

            # Call the function
            result = calculate_estimated_intake("Chicken", 150)
            assert result["Protein"] == round(10 * 150 / 100, 2), "Protein calculation is incorrect"
            assert result["Carbohydrates"] == round(20 * 150 / 100, 2), "Carbohydrates calculation is incorrect"

            # Verify
            assert "Protein" in result
            assert "Carbohydrates" in result
            assert len(result) == 2, "Result should only contain 'Protein' and 'Carbohydrates'"


def test_calculate_nutrient_limits_level_none():
    # Test the scenario where 'level' is None to trigger the missing branch
    nutrient = "Protein"
    min_value, max_value = calculate_nutrient_limits(nutrient, None)
    assert min_value == get_min_value(nutrient)
    assert max_value == get_max_value(nutrient)

def test_validate_amount_input_non_numeric():
    result = validate_amount_input("abc")  # Non-numeric input
    assert result == "Error: The amount must be a numeric integer."


def test_validate_amount_input_out_of_range():
    result = validate_amount_input(-1)
    assert result == f"Error: The amount must be between {MIN_AMOUNT_VALUE} and {MAX_AMOUNT_VALUE}."
    result = validate_amount_input(1001)
    assert result == f"Error: The amount must be between {MIN_AMOUNT_VALUE} and {MAX_AMOUNT_VALUE}."
def test_validate_amount_input_valid():
    result = validate_amount_input(100)  # Valid input within the range
    assert result == ""

######

def test_reset_estimated_intake():
    mock_user_goals = {"Protein": 50, "Carbohydrates": 100}
    mock_estimated_intake = {"Protein": 25, "Carbohydrates": 40}

    with patch('goals.user_goals', mock_user_goals), \
            patch('goals.estimated_intake', mock_estimated_intake):
        reset_estimated_intake()

        for nutrient in mock_user_goals:
            assert mock_estimated_intake[
                       nutrient] == 0, f"Estimated intake for {nutrient} was not reset correctly, found {mock_estimated_intake[nutrient]}"