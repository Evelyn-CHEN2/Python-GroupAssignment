import wx
import matplotlib.pyplot as plt
import database
import goals
import plt
from template_frame import MyFrame

class TrackMyBitesFrame(MyFrame):
    def __init__(self):
        """
        Initializes the frame and sets up the UI elements with data from the database.
        """
        super().__init__(None)

        # Initialize UI elements with data
        self.initialize_ui_elements()

        # Bind the close event to the OnClose method and layout the frame
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Show()
        self.Layout()

    def OnClose(self, event):
        """
        Closes the frame and exits the application when the close (X) button is clicked.
        """
        event.Skip()
        self.Destroy()
        wx.Exit()

    def OnNutrient1Selected(self, event):
        """
        Updates the static text for the first nutrient selection.
        Triggered when the user selects a nutrient from the first dropdown.
        """
        event.Skip()
        self.updateStaticText(self.WelcomePanel.goalUnitLabel1, self.WelcomePanel.goalNameField1.GetStringSelection())

    def OnNutrient2Selected(self, event):
        """
        Updates the static text for the second nutrient selection.
        Triggered when the user selects a nutrient from the second dropdown.
        """
        event.Skip()
        self.updateStaticText(self.WelcomePanel.goalUnitLabel2, self.WelcomePanel.goalNameField2.GetStringSelection())

    def OnNutrient3Selected(self, event):
        """
        Updates the static text for the third nutrient selection.
        Triggered when the user selects a nutrient from the third dropdown.
        """
        event.Skip()
        self.updateStaticText(self.WelcomePanel.goalUnitLabel3, self.WelcomePanel.goalNameField3.GetStringSelection())

    def OnSubmitButtonClicked(self, event):
        """
        Handles the form submission when the user sets their goals.
        Validates and sets the goals using the data from input fields. Displays an error
        message if validation fails.
        """
        event.Skip()
        
        message = goals.set_goals(self.get_goal_inputs())
        if (message):
            self.m_statusBar1.SetStatusText(message)
            return
        
        self.initialize_main_view()

    def OnNutrientSelected(self, event):
        """
        Updates the range filter min and max values for the selected nutrient.
        """
        event.Skip()
        self.updateRangeFilter()

    def OnLevelSelected(self, event):
        """
        Adjusts the min and max values of the range filter based on the selected nutrient level (Low, Mid, High).
        """
        event.Skip()
        if self.MainPanel.nutritionNameField.GetSelection() == -1:
            self.m_statusBar1.SetStatusText("Error: Please select a nutrient before applying level or range filters.")
            self.MainPanel.nutritionLevelField.SetSelection(-1)
            return
        self.updateRangeFilter()

    def OnSearchButtonClicked(self, event):
        """
        Executes the food search based on user input and updates the results table.
        """
        event.Skip()
        rangeFilteredNutrient = None
        min, max = None, None
        excludedNutrient = None

        foodItemName = self.MainPanel.foodNameSearchField.GetValue().strip()

        # if a nutrient is selected for filtering by range
        if self.MainPanel.nutritionNameField.GetSelection() != -1:
            rangeFilteredNutrient = self.getNutritionName()
            min, max = self.range_filter.getValue()

        # if a nutrient is selected for exclusion
        if self.MainPanel.exclusionFilterField.GetSelection() != -1:
            excludedNutrient = self.MainPanel.exclusionFilterField.GetString(self.MainPanel.exclusionFilterField.GetSelection())

        # perform the search with food name, range filter, and exclusion filter
        results = database.db_search(foodItemName, rangeFilteredNutrient, (min, max), excludedNutrient)

        self.MainPanel.searchList.DeleteAllItems()

        # if results are found
        if not results.empty:
            for index, row in results.iterrows():
                self.MainPanel.searchList.InsertItem(index, row['food'])
            self.MainPanel.listHeader.SetLabel(f"Search Results: {len(results)}")
        else:
            self.MainPanel.listHeader.SetLabel("No results found.")
            self.m_statusBar1.SetStatusText("No food items match the search criteria.")

    def OnFoodItemSelected(self, event):
        """
        Handles the event when a food item is selected from the list.
        Updates the labels and progress bars with the estimated intake for the selected food item.
        """
        selectedIndex = event.GetIndex()
        selectedFood = self.MainPanel.searchList.GetItemText(selectedIndex)

        amount = float(self.MainPanel.amountField.GetValue())
        message = goals.validate_amount_input(amount)
        if (message):
            self.m_statusBar1.SetStatusText(message)
            return
        goals.calculate_estimated_intake(selectedFood, amount)
        self.updateProgressBars()
        selectedChartType = self.MainPanel.chartTypeField.GetStringSelection()
        self.drawChart(selectedChartType, selectedFood)

    def OnFoodAmountChanged(self, event):
        """
        Updates the estimated intake when the user changes the food amount.
        Displays an error message if the amount input is invalid.
        """
        event.Skip()
        selectedIndex = self.MainPanel.searchList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
        if selectedIndex == -1:
            self.m_statusBar1.SetStatusText("Error: Please select one food item.")
            return
        
        selectedFood = self.MainPanel.searchList.GetItemText(selectedIndex)        
        amount = float(self.MainPanel.amountField.GetValue())
        message = goals.validate_amount_input(amount)
        if (message):
            self.m_statusBar1.SetStatusText(message)
            return
        goals.calculate_estimated_intake(selectedFood, amount)
        self.updateProgressBars()

    def OnEatButtonClicked(self, event):
        """
        Updates the actual intake based on the estimated intake and resets the estimated values.
        """
        event.Skip()
        goals.update_actual_intake()
        self.updateProgressBars()

    def OnResetButtonClicked(self, event):
        """
        Resets the current intake values for all nutrients.
        """
        event.Skip()
        goals.reset_current_intake()
        goals.reset_estimated_intake()
        self.updateProgressBars()
    
    def OnChartTypeSelected(self, event):
        """
        Updates the displayed chart based on the selected chart type.
        """
        event.Skip()
        selectedChartType = self.MainPanel.chartTypeField.GetStringSelection()
        selectedIndex = self.MainPanel.searchList.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
        selectedFood = self.MainPanel.searchList.GetItemText(selectedIndex)
        self.drawChart(selectedChartType, selectedFood)



    def initialize_ui_elements(self):
        """
        Retrieves data from the database and sets up the UI elements.
        """
        # Retrieve the list of nutrient categories from the database
        m_choiceChoices = database.get_nutrient_categories()

        # Set the data for the different fields
        self.WelcomePanel.goalNameField1.SetItems(m_choiceChoices)
        self.WelcomePanel.goalNameField1.SetSelection(-1)
        self.WelcomePanel.goalNameField2.SetItems(m_choiceChoices)
        self.WelcomePanel.goalNameField2.SetSelection(-1)
        self.WelcomePanel.goalNameField3.SetItems(m_choiceChoices)
        self.WelcomePanel.goalNameField3.SetSelection(-1)
        self.MainPanel.nutritionNameField.SetItems(m_choiceChoices)
        self.MainPanel.nutritionNameField.SetSelection(-1)
        self.MainPanel.nutritionLevelField.SetItems(["Low", "Mid", "High"])
        self.MainPanel.nutritionLevelField.SetSelection(-1)
        self.MainPanel.exclusionFilterField.SetItems(m_choiceChoices)
        self.MainPanel.exclusionFilterField.SetSelection(-1)
        self.MainPanel.chartTypeField.SetItems(["Bar", "Pie"])
        self.MainPanel.searchList.InsertColumn(0, 'Food', width=300)
    
    def initialize_main_view(self):
        """
        Initializes the main view by updating filters, showing/hiding panels,
        and adjusting the frame size.
        """
        self.createRangeFilter()
        self.updateProgressBars()
        self.WelcomePanel.Hide()
        self.MainPanel.Show()
        self.SetSize((1200, 800))
        self.Center()
        self.Layout()

    def get_goal_inputs(self):
        """
        Retrieves the goal inputs from the WelcomePanel fields.
        Returns a list of (goalName, goalValue) tuples.
        """
        inputs = []
        if self.WelcomePanel.goalNameField1.GetSelection() != -1:
            inputs.append((self.WelcomePanel.goalNameField1.GetString(self.WelcomePanel.goalNameField1.GetSelection()),
                        self.WelcomePanel.goalValueField1.GetValue()))
        if self.WelcomePanel.goalNameField2.GetSelection() != -1:
            inputs.append((self.WelcomePanel.goalNameField2.GetString(self.WelcomePanel.goalNameField2.GetSelection()),
                        self.WelcomePanel.goalValueField2.GetValue()))
        if self.WelcomePanel.goalNameField3.GetSelection() != -1:
            inputs.append((self.WelcomePanel.goalNameField3.GetString(self.WelcomePanel.goalNameField3.GetSelection()),
                        self.WelcomePanel.goalValueField3.GetValue()))
        return inputs

    def updateStaticText(self, component, nutrient):
        """
        Updates the static text component with the appropriate unit (kcal, g or mg) 
        based on the selected nutrient.
        """
        component.SetLabel(database.get_unit(nutrient))


    def createRangeFilter(self):
        """
        Creates the range filter slider.
        """
        min = database.get_min_value()
        max = database.get_max_value()
        self.range_filter = plt.RangeFilter(self.MainPanel.nutritionRangePanel, min, max)

    
    def updateRangeFilter(self):
        """
        Updates the range filter slider based on the current state.
        """
        nutrient = self.getNutritionName()
        min = database.get_min_value(nutrient)
        max = database.get_max_value(nutrient)

        level = self.getLevel()
        current_min, current_max = database.calculate_nutrient_limits(nutrient, level)

        self.range_filter.update_slider_range(min, max, current_min, current_max)

    
    def updateProgressBars(self):
        """
        Updates the progress bars for current intake and expected intake.
        If the current intake exceeds the goal, the bar is colored red; otherwise, it is black.
        """
        user_goals = goals.get_user_goals()
        current_intakes = goals.get_current_intake()
        estimated_intakes = goals.get_estimated_intake()
        keys = list(user_goals.keys())

        panels = [self.MainPanel.goalPanel1, self.MainPanel.goalPanel2, self.MainPanel.goalPanel3]
        labels = [(self.MainPanel.goalName1, self.MainPanel.goalValue1),
                  (self.MainPanel.goalName2, self.MainPanel.goalValue2),
                  (self.MainPanel.goalName3, self.MainPanel.goalValue3)]

        for i, nutrient in enumerate(keys):
            user_goal = user_goals[nutrient]
            current_intake = current_intakes[nutrient]
            estimated_intake = estimated_intakes[nutrient]

            plt.progression_bar(panels[i], current_intake, estimated_intake, user_goal)
            labels[i][0].SetLabel(nutrient)
            labels[i][1].SetLabel(f"{current_intake + estimated_intake:.2f} / {user_goal} {database.get_unit(nutrient)}")
            if goals.is_estimated_intake_exceeded(nutrient):
                labels[i][1].SetForegroundColour(wx.RED)
            else:
                labels[i][1].SetForegroundColour(wx.BLACK)

    def updateChart(self, food):
        """
        Draws the chart (default Bar) based on the selected food item.
        """
        chart_type = self.MainPanel.chartTypeField.GetStringSelection()
        self.drawChart(chart_type, food)

    def drawChart(self, chartType, food):
        """
        Draws the selected chart type (Bar or Pie) for the given food item.
        """
        # clear the chart panel before drawing a new chart
        for child in self.MainPanel.chartPanel.GetChildren():
            child.Destroy()
        # create chart according to chart type
        top_nutrients = database.get_nutritional_info(food)
        plt.plot_chart(self.MainPanel.chartPanel, chartType, list(top_nutrients.keys()), list(top_nutrients.values()))
        # Refresh and layout the panel to reflect the new chart
        self.MainPanel.chartPanel.Layout()
        self.MainPanel.chartPanel.Refresh()


    def getNutritionName(self):
        if self.MainPanel.nutritionNameField.GetSelection() == -1:
            return None
        return self.MainPanel.nutritionNameField.GetString(self.MainPanel.nutritionNameField.GetSelection())
    
    def getLevel(self):
        if self.MainPanel.nutritionLevelField.GetSelection() == -1:
            return None
        return self.MainPanel.nutritionLevelField.GetString(self.MainPanel.nutritionLevelField.GetSelection())
            

if __name__ == "__main__":
    app = wx.App()
    frame = TrackMyBitesFrame()
    app.MainLoop()
