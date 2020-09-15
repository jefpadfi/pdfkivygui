from kivy.app import App
from pdfkivygui.pdfkivygui import Graph, BarGraph
from kivy.uix.label import Label
import pandas as pd


test_time = ["8:00", "9:00", "10:30", "11:00", "12:00", "1:00", "2:00", "3:00", "4:00"]
test_dollars = [6.57, 105.92, 5.00, 9.55, 10.25, 11.55, 4.15, 2.36, .30]

pandas_data = {"y": test_dollars, "x": test_time}

df = pd.DataFrame(pandas_data)


class Example(App):
    def build(self):
        graph_test = Graph()
        graph_test.draw(df)

        # bar_test = BarGraph()
        # bar_test.x_tick_labels = test_time

        graph_test.draw(df)

        return graph_test


if __name__ == "__main__":
    Example().run()

