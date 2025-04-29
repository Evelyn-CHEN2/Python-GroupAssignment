# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

import database

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"TrackMyBites"), pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.WelcomePanel = WelcomePanel(self)
        self.MainPanel = MainPanel(self)
        bSizer13.Add(self.WelcomePanel, 1, wx.EXPAND)
        bSizer13.Add(self.MainPanel, 1, wx.EXPAND)
        self.MainPanel.Hide()

        self.SetSizer( bSizer13 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.WelcomePanel.goalNameField1.Bind( wx.EVT_CHOICE, self.OnNutrient1Selected )
        self.WelcomePanel.goalNameField2.Bind( wx.EVT_CHOICE, self.OnNutrient2Selected )
        self.WelcomePanel.goalNameField3.Bind( wx.EVT_CHOICE, self.OnNutrient3Selected )
        self.WelcomePanel.goalSubmitButton.Bind( wx.EVT_BUTTON, self.OnSubmitButtonClicked )

        # Connect Events
        self.MainPanel.nutritionNameField.Bind( wx.EVT_CHOICE, self.OnNutrientSelected )
        self.MainPanel.nutritionLevelField.Bind( wx.EVT_CHOICE, self.OnLevelSelected )
        self.MainPanel.searchButton.Bind( wx.EVT_BUTTON, self.OnSearchButtonClicked )
        self.MainPanel.amountField.Bind( wx.EVT_TEXT_ENTER, self.OnFoodAmountChanged )
        self.MainPanel.eatButton.Bind( wx.EVT_BUTTON, self.OnEatButtonClicked )
        self.MainPanel.resetButton.Bind( wx.EVT_BUTTON, self.OnResetButtonClicked )
        self.MainPanel.chartTypeField.Bind( wx.EVT_CHOICE, self.OnChartTypeSelected )
        self.MainPanel.searchList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnFoodItemSelected )

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def OnNutrient1Selected( self, event ):
        event.Skip()

    def OnNutrient2Selected( self, event ):
        event.Skip()

    def OnNutrient3Selected( self, event ):
        event.Skip()

    def OnSubmitButtonClicked( self, event ):
        event.Skip()

    def OnNutrientSelected( self, event ):
        event.Skip()

    def OnLevelSelected( self, event ):
        event.Skip()

    def OnSearchButtonClicked( self, event ):
        event.Skip()

    def OnFoodAmountChanged( self, event ):
        event.Skip()

    def OnEatButtonClicked( self, event ):
        event.Skip()

    def OnResetButtonClicked( self, event ):
        event.Skip()

    def OnFoodItemSelected( self, event ):
        event.Skip()


###########################################################################
## Class WelcomePanel
###########################################################################

class WelcomePanel ( wx.Panel ):

    

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        welcomeSizer = wx.BoxSizer( wx.VERTICAL )

        self.welcomePanelTitle = wx.StaticText( self, wx.ID_ANY, _(u"TrackMyBites"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.welcomePanelTitle.Wrap( -1 )

        self.welcomePanelTitle.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.welcomePanelTitle.SetForegroundColour( wx.Colour( 0, 102, 204 ) )

        welcomeSizer.Add( self.welcomePanelTitle, 0, wx.ALIGN_CENTER|wx.TOP, 20 )

        self.guideText = wx.StaticText( self, wx.ID_ANY, _(u"Welcome to TrackMyBites where you will be able to track the nutritional value\nof your food intake. Let’s start by entering in your target nutrition values"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.guideText.Wrap( -1 )

        welcomeSizer.Add( self.guideText, 0, wx.ALIGN_CENTER|wx.ALL, 20 )

        self.separator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        welcomeSizer.Add( self.separator, 0, wx.BOTTOM|wx.EXPAND, 20 )

        goalInputSizer = wx.FlexGridSizer( 3, 5, 0, 0 )
        goalInputSizer.AddGrowableCol( 1 )
        goalInputSizer.AddGrowableRow( 0 )
        goalInputSizer.AddGrowableRow( 1 )
        goalInputSizer.AddGrowableRow( 2 )
        goalInputSizer.SetFlexibleDirection( wx.BOTH )
        goalInputSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.goalNameLabel1 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalNameLabel1.Wrap( -1 )

        goalInputSizer.Add( self.goalNameLabel1, 0, wx.ALL, 5 )

        goalNameField1Choices = []
        self.goalNameField1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, goalNameField1Choices, 0 )
        self.goalNameField1.SetSelection( 0 )
        goalInputSizer.Add( self.goalNameField1, 0, wx.ALL, 5 )

        self.goalValueLabel1 = wx.StaticText( self, wx.ID_ANY, _(u"Target Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalValueLabel1.Wrap( -1 )

        goalInputSizer.Add( self.goalValueLabel1, 0, wx.ALL, 5 )

        self.goalValueField1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        goalInputSizer.Add( self.goalValueField1, 0, wx.ALL, 5 )

        self.goalUnitLabel1 = wx.StaticText( self, wx.ID_ANY, _(u"g"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalUnitLabel1.Wrap( -1 )

        goalInputSizer.Add( self.goalUnitLabel1, 0, wx.ALL, 5 )

        self.goalNameLabel2 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalNameLabel2.Wrap( -1 )

        goalInputSizer.Add( self.goalNameLabel2, 0, wx.ALL, 5 )

        goalNameField2Choices = []
        self.goalNameField2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, goalNameField2Choices, 0 )
        self.goalNameField2.SetSelection( 0 )
        goalInputSizer.Add( self.goalNameField2, 0, wx.ALL, 5 )

        self.goalValueLabel2 = wx.StaticText( self, wx.ID_ANY, _(u"Target Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalValueLabel2.Wrap( -1 )

        goalInputSizer.Add( self.goalValueLabel2, 0, wx.ALL, 5 )

        self.goalValueField2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        goalInputSizer.Add( self.goalValueField2, 0, wx.ALL, 5 )

        self.goalUnitLabel2 = wx.StaticText( self, wx.ID_ANY, _(u"g"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalUnitLabel2.Wrap( -1 )

        goalInputSizer.Add( self.goalUnitLabel2, 0, wx.ALL, 5 )

        self.goalNameLabel3 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalNameLabel3.Wrap( -1 )

        goalInputSizer.Add( self.goalNameLabel3, 0, wx.ALL, 5 )

        goalNameField3Choices = []
        self.goalNameField3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, goalNameField3Choices, 0 )
        self.goalNameField3.SetSelection( 0 )
        goalInputSizer.Add( self.goalNameField3, 0, wx.ALL, 5 )

        self.goalValueLabel3 = wx.StaticText( self, wx.ID_ANY, _(u"Target Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalValueLabel3.Wrap( -1 )

        goalInputSizer.Add( self.goalValueLabel3, 0, wx.ALL, 5 )

        self.goalValueField3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        goalInputSizer.Add( self.goalValueField3, 0, wx.ALL, 5 )

        self.goalUnitLabel3 = wx.StaticText( self, wx.ID_ANY, _(u"g"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalUnitLabel3.Wrap( -1 )

        goalInputSizer.Add( self.goalUnitLabel3, 0, wx.ALL, 5 )


        welcomeSizer.Add( goalInputSizer, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 100 )

        self.goalSubmitButton = wx.Button( self, wx.ID_ANY, _(u"Submit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goalSubmitButton.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.goalSubmitButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.goalSubmitButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        welcomeSizer.Add( self.goalSubmitButton, 0, wx.ALIGN_CENTER|wx.BOTTOM, 20 )


        self.SetSizer( welcomeSizer )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        mainSizer = wx.BoxSizer( wx.VERTICAL )

        self.mainPanelTitle = wx.StaticText( self, wx.ID_ANY, _(u"TrackMyBites"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.mainPanelTitle.Wrap( -1 )

        self.mainPanelTitle.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.mainPanelTitle.SetForegroundColour( wx.Colour( 0, 102, 204 ) )

        mainSizer.Add( self.mainPanelTitle, 0, wx.ALIGN_CENTER|wx.ALL, 20 )

        self.titleSeparator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        mainSizer.Add( self.titleSeparator, 0, wx.ALIGN_TOP|wx.BOTTOM|wx.EXPAND, 15 )

        mainContentSizer = wx.BoxSizer( wx.HORIZONTAL )

        filterSizer = wx.BoxSizer( wx.VERTICAL )

        self.filterHeader = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Fact Search Tool"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filterHeader.Wrap( -1 )

        self.filterHeader.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.filterHeader.SetForegroundColour( wx.Colour( 0, 102, 204 ) )

        filterSizer.Add( self.filterHeader, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

        self.foodNameLabel = wx.StaticText( self, wx.ID_ANY, _(u"Food Name Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.foodNameLabel.Wrap( -1 )

        self.foodNameLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.foodNameLabel.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

        filterSizer.Add( self.foodNameLabel, 0, wx.LEFT|wx.TOP, 10 )

        self.foodNameSearchField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.foodNameSearchField.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterSizer.Add( self.foodNameSearchField, 0, wx.ALL|wx.EXPAND, 5 )

        self.nutritionNameLabel = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nutritionNameLabel.Wrap( -1 )

        self.nutritionNameLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.nutritionNameLabel.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

        filterSizer.Add( self.nutritionNameLabel, 0, wx.LEFT|wx.TOP, 10 )

        nutritionNameFieldChoices = []
        self.nutritionNameField = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), nutritionNameFieldChoices, 0 )
        self.nutritionNameField.SetSelection( 0 )
        self.nutritionNameField.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterSizer.Add( self.nutritionNameField, 0, wx.ALL|wx.EXPAND, 5 )

        self.nutritionLevelLabel = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nutritionLevelLabel.Wrap( -1 )

        self.nutritionLevelLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.nutritionLevelLabel.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

        filterSizer.Add( self.nutritionLevelLabel, 0, wx.LEFT|wx.TOP, 10 )

        nutritionLevelFieldChoices = []
        self.nutritionLevelField = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), nutritionLevelFieldChoices, 0 )
        self.nutritionLevelField.SetSelection( 0 )
        self.nutritionLevelField.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterSizer.Add( self.nutritionLevelField, 0, wx.ALL|wx.EXPAND, 5 )

        self.nutritionRangeLabel = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nutritionRangeLabel.Wrap( -1 )

        self.nutritionRangeLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.nutritionRangeLabel.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

        filterSizer.Add( self.nutritionRangeLabel, 0, wx.LEFT|wx.TOP, 10 )

        self.nutritionRangePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,80 ), wx.TAB_TRAVERSAL )
        filterSizer.Add( self.nutritionRangePanel, 0, wx.EXPAND |wx.ALL, 5 )

        self.exclusionFilterLabel = wx.StaticText( self, wx.ID_ANY, _(u"Exclusion Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.exclusionFilterLabel.Wrap( -1 )

        self.exclusionFilterLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.exclusionFilterLabel.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

        filterSizer.Add( self.exclusionFilterLabel, 0, wx.LEFT|wx.TOP, 10 )

        exclusionFilterFieldChoices = []
        self.exclusionFilterField = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), exclusionFilterFieldChoices, 0 )
        self.exclusionFilterField.SetSelection( 0 )
        self.exclusionFilterField.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterSizer.Add( self.exclusionFilterField, 0, wx.ALL|wx.EXPAND, 5 )


        filterSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.searchButton = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.searchButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.searchButton.SetMinSize( wx.Size( 100,30 ) )

        filterSizer.Add( self.searchButton, 0, wx.ALL|wx.EXPAND, 10 )


        mainContentSizer.Add( filterSizer, 1, wx.ALL|wx.EXPAND, 10 )

        self.filterResultSeparator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        mainContentSizer.Add( self.filterResultSeparator, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 15 )

        resultSizer = wx.BoxSizer( wx.VERTICAL )

        progressSizer = wx.BoxSizer( wx.VERTICAL )

        self.barHeader = wx.StaticText( self, wx.ID_ANY, _(u"Progress Bars"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.barHeader.Wrap( -1 )

        self.barHeader.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.barHeader.SetForegroundColour( wx.Colour( 0, 102, 204 ) )

        progressSizer.Add( self.barHeader, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        barSizer = wx.FlexGridSizer( 3, 3, 0, 0 )
        barSizer.AddGrowableCol( 1 )
        barSizer.AddGrowableRow( 0 )
        barSizer.AddGrowableRow( 1 )
        barSizer.AddGrowableRow( 2 )
        barSizer.SetFlexibleDirection( wx.BOTH )
        barSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.goalName1 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Name"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_MIDDLE )
        self.goalName1.Wrap( -1 )

        barSizer.Add( self.goalName1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.goalPanel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        barSizer.Add( self.goalPanel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.goalValue1 = wx.StaticText( self, wx.ID_ANY, _(u"0 / 0 g"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
        self.goalValue1.Wrap( -1 )

        barSizer.Add( self.goalValue1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.goalName2 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Name"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_MIDDLE )
        self.goalName2.Wrap( -1 )

        barSizer.Add( self.goalName2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.goalPanel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        barSizer.Add( self.goalPanel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.goalValue2 = wx.StaticText( self, wx.ID_ANY, _(u"0 / 0 g"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
        self.goalValue2.Wrap( -1 )

        barSizer.Add( self.goalValue2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.goalName3 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Name"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_MIDDLE )
        self.goalName3.Wrap( -1 )

        barSizer.Add( self.goalName3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.goalPanel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        barSizer.Add( self.goalPanel3, 1, wx.ALL|wx.EXPAND, 5 )

        self.goalValue3 = wx.StaticText( self, wx.ID_ANY, _(u"0 / 0 g"), wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
        self.goalValue3.Wrap( -1 )

        barSizer.Add( self.goalValue3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        progressSizer.Add( barSizer, 3, wx.ALL|wx.EXPAND, 5 )

        barInputSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.amountLabel = wx.StaticText( self, wx.ID_ANY, _(u"Amount"), wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.amountLabel.Wrap( -1 )

        barInputSizer.Add( self.amountLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.amountField = wx.TextCtrl( self, wx.ID_ANY, _(u"100"), wx.DefaultPosition, wx.Size( -1,20 ), wx.TE_PROCESS_ENTER )
        barInputSizer.Add( self.amountField, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.amountUnitLabel = wx.StaticText( self, wx.ID_ANY, _(u"g"), wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.amountUnitLabel.Wrap( -1 )

        barInputSizer.Add( self.amountUnitLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        barInputSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.eatButton = wx.Button( self, wx.ID_ANY, _(u"Eat"), wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.eatButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        barInputSizer.Add( self.eatButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.resetButton = wx.Button( self, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.resetButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        barInputSizer.Add( self.resetButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        progressSizer.Add( barInputSizer, 1, wx.ALL|wx.EXPAND, 5 )


        resultSizer.Add( progressSizer, 1, wx.EXPAND, 5 )

        self.barGraphSeparator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        resultSizer.Add( self.barGraphSeparator, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 10 )

        listGraphSizer = wx.FlexGridSizer( 2, 2, 5, 5 )
        listGraphSizer.AddGrowableCol( 1 )
        listGraphSizer.AddGrowableRow( 1 )
        listGraphSizer.SetFlexibleDirection( wx.BOTH )
        listGraphSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.listHeader = wx.StaticText( self, wx.ID_ANY, _(u"Search Results"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.listHeader.Wrap( -1 )

        self.listHeader.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.listHeader.SetForegroundColour( wx.Colour( 0, 102, 204 ) )

        listGraphSizer.Add( self.listHeader, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        chartTypeFieldChoices = []
        self.chartTypeField = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chartTypeFieldChoices, 0 )
        self.chartTypeField.SetSelection( 0 )
        listGraphSizer.Add( self.chartTypeField, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.searchList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        listGraphSizer.Add( self.searchList, 1, wx.ALL|wx.EXPAND, 5 )

        self.chartPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        listGraphSizer.Add( self.chartPanel, 1, wx.EXPAND |wx.ALL, 5 )


        resultSizer.Add( listGraphSizer, 2, wx.EXPAND, 5 )


        mainContentSizer.Add( resultSizer, 3, wx.ALL|wx.EXPAND, 10 )


        mainSizer.Add( mainContentSizer, 1, wx.EXPAND, 5 )


        self.SetSizer( mainSizer )
        self.Layout()


        self.SetSizer( mainSizer )
        self.Layout()

    def __del__( self ):
        pass

