"""
Programmer: Jeffrey Padfield
Description: Custom Kivy Widget to use matplotlib to display Pandas DataFrame.
Date: 08/07/2019
Version: 1
"""

import kivy
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty, NumericProperty, StringProperty, ListProperty

# import matplotlib and have it use matplotlib.backend_kivy for its system
import matplotlib

