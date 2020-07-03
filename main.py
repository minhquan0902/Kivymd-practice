from kivymd.app import MDApp
from part2.farmersmapview import FarmersMapView
import _sqlite3


class MainApp(MDApp):
    connection = None
    cursor = None

    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = _sqlite3.connect('markets.db')
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu

    pass


MainApp().run()
