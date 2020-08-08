"""
Programmer: Jeffrey Padfield
Description: Custom Kivy Widget to use matplotlib to display Pandas DataFrame.
Date: 08/07/2019
Version: 1
"""

import os

import kivy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, ObjectProperty, NumericProperty, StringProperty, ListProperty

import matplotlib
import matplotlib.pyplot as plt

from collections import OrderedDict

import numpy as np
import pandas as pd


# lets make sure matplotlib knows to use our kivy backend from https://github.com/kivy-garden/garden.matplotlib
matplotlib.use("module://pdfkivygui.gard.matplotlib.backend_kivy")



