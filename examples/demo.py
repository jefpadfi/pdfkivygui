from kivy.app import App
from pdfkivygui.pdfkivygui import Graph
from kivy.uix.label import Label
import pandas as pd


test_time = ["8:00", "9:00", "10:00", "11:00", "12:00", "1:00", "2:00", "3:00", "4:00"]
test_dollars = [6.57, 7.77, 5.00, 9.55, 10.25, 11.55, 4.15, 2.36, 12.30]

pandas_data = {"y": test_dollars, "x": test_time}

df = pd.DataFrame(pandas_data)


class Example(App):
    def build(self):
        graph_test = Graph()
        graph_test.redraw(df)
        return graph_test


if __name__ == "__main__":
    Example().run()

