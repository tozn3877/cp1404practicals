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
        miles = self.get_miles()
        kilometres = miles * MILES_TO_KM
        self.output_km_text = str(kilometres)

    def increment_miles(self, change):
        """Increase or decrease the miles value."""
        miles = self.get_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)


    def get_miles(self):
        """Get miles value from the input, treating invalid input as 0."""
        miles_text = self.root.ids.input_miles.text
        try:
            miles = float(miles_text)
        except ValueError:
            miles = 0.0
        return miles

MilesToKilometresApp().run()