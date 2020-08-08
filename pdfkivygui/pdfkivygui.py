"""
Programmer: Jeffrey Padfield
Description: Custom Kivy Widget to use matplotlib to display Pandas DataFrame.
Date: 08/07/2019
Version: 1
"""

import os
import datetime
import random

import kivy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, ObjectProperty, NumericProperty, StringProperty, ListProperty

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from collections import OrderedDict

import numpy as np
import pandas as pd


# lets make sure matplotlib knows to use our kivy backend from https://github.com/kivy-garden/garden.matplotlib
matplotlib.use("module://pdfkivygui.garden.matplotlib.backend_kivy")


class Graph(BoxLayout):
    show_grid = BooleanProperty(True)
    x_label = StringProperty("Time")
    y_label = StringProperty("Dollars")

    """ Simple Graph for Pandas Dataframe. """
    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)
        self.figure, self.axes = plt.subplots()
        # if we have spacing lets use it.
        self.add_widget(self.figure.canvas)

    def draw(self, df):
        # Let's clear the axes before we draw as we may be updating the content.
        self.axes.clear()
        # Let's draw the x and y labels for the graph
        self.axes.set_xlabel(self.x_label)
        self.axes.set_ylabel(self.y_label)

        if self.show_grid:
            self.axes.grid()
        self.axes.plot(df.iloc[:, 1].values,
                       df.iloc[:, 0].values)


class HBarGraph(BoxLayout):
    show_grid = BooleanProperty(True)
    x_label = StringProperty("Time")
    y_label = StringProperty("Dollars")

    def __init__(self, **kwargs):
        super(HBarGraph, self).__init__(**kwargs)
        self.figure, self.axes = plt.subplots()
        self.add_widget(self.figure.canvas)

    def draw(self, df):
        # Let's clear the axes before we draw as we may be updating the content.
        self.axes.clear()
        # Let's draw the x and y labels for the graph
        self.axes.set_xlabel(self.x_label)
        self.axes.set_ylabel(self.y_label)

        if self.show_grid:
            self.axes.grid()

        self.axes.barh(df.iloc[:, 0], 1000, align='center')

