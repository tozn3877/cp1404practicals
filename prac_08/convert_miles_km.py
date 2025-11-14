"""
CP1404/CP5632 - Practical
Convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km_text = StringProperty("0.0")

    def build(self):
        """Build app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert_miles_to_km(self):
        """Handle conversion from miles to kilometres."""
        miles_text = self.root.ids.input_miles.text
        miles = float(miles_text)
        kilometres = miles * MILES_TO_KM
        self.output_km_text = str(kilometres)

    def increment_miles(self, change):
        """Increase or decrease the miles value."""
        miles_text = self.root.ids.input_miles.text
        if miles_text == "":
            miles = 0.0
        else:
            miles = float(miles_text)
        miles += change
        self.root.ids.input_miles.text = str(miles)


MilesToKilometresApp().run()