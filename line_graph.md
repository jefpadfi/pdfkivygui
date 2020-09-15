# Line Graph of Pandas Dataframe Kivy GUI
I have made the library as easy as possible. It will take the supplied Pandas Dataframe and render it into a graph that 
kivy can display. For example a simple bar graph goes like this.

```
from kivy.app import App
from pdfkivygui.pdfkivygui import Graph
import pandas as pd


# Create a two lists with data you want to display.
test_time = ["8:00", "9:00", "10:30", "11:00", "12:00", "1:00", "2:00", "3:00", "4:00"]
test_dollars = [6.57, 105.92, 5.00, 9.55, 10.25, 11.55, 4.15, 2.36, .30]

# Combine the two lists into a dictionary
pandas_data = {"y": test_dollars, "x": test_time}
# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(pandas_data)

class Example(App):
    def build(self):
        # Initiate the BarGraph widget from the library
        graph_test = Graph()
        # Call the Draw event to have kivy draw the graph inside the view
        graph_test.draw(df)
        # Return the widget so it renders to screen
        return graph_test


if __name__ == "__main__":
    Example().run()
```