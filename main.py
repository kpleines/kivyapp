from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

KV = """

#:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton
# The root widget is a Screen containing a vertical BoxLayout.
Screen:
    BoxLayout:
        orientation: "vertical"

        # --------------------------
        # Top Menubar using MDTopAppBar
        # --------------------------
        MDTopAppBar:
            type: "small"
 
            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "menu"
                    on_release: app.top_appbar_action()

                MDTopAppBarTitle:
                    text: "AppBar Center-aligned"
                    pos_hint: {"center_x": .5}
                MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "account-circle-outline"
                    on_release: app.top_appbar_action()

        # --------------------------
        # Middle: Scrollable Table Area
        # --------------------------
        ScrollView:
            do_scroll_x: False  # Vertical scrolling only
            MDGridLayout:
                id: table_grid
                cols: 3            # Three columns for our table
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True
                # --- Header Row --- (Bold text)
                MDLabel:
                    text: "Column 1"
                    halign: "center"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                MDLabel:
                    text: "Column 2"
                    halign: "center"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                MDLabel:
                    text: "Column 3"
                    halign: "center"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                # --- Data Rows ---\n                # Row 1\n                MDLabel:\n                    text: "Row1, Col1"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1\n                MDLabel:\n                    text: "Row1, Col2"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1\n                MDLabel:\n                    text: "Row1, Col3"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1\n                # Row 2\n                MDLabel:\n                    text: "Row2, Col1"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1\n                MDLabel:\n                    text: "Row2, Col2"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1\n                MDLabel:\n                    text: "Row2, Col3"\n                    halign: "center"\n                    theme_text_color: "Custom"\n                    text_color: 1, 1, 1, 1

        # --------------------------
        # Bottom Status Bar using MDToolbar
        # --------------------------
        MDBottomAppBar:
            
            action_items:
                [
                MDActionBottomAppBarButton(icon="gmail", on_release=app.gmail_action),
                MDActionBottomAppBarButton(icon="label-outline", on_release=app.label_action),
                MDActionBottomAppBarButton(icon="bookmark", on_release=app.bookmark_action),
                ]

            MDFabBottomAppBarButton:
                id: fab_button
                icon: "plus"
                on_release: app.change_actions_items()
"""

class MyApp(MDApp):
    def menu_callback(self, menu_name):
        # This callback is triggered when a menu item is pressed.
        print("Menu item pressed:", menu_name)
        # Update the status label on the main screen
        self.root.ids.status_label.text = f"Menu item pressed: {menu_name}"

    def top_appbar_action(self):
        print("Top app bar action pressed")
        #self.root.ids.status_label.text = "Top app bar action pressed!"

    def change_actions_items(self):
        # This function is triggered when the bottom FAB is pressed.
        print("Bottom app bar action pressed")
        #self.root.ids.status_label.text = "Bottom app bar action pressed!"
    def gmail_action(self, *args):
        print("Gmail button pressed")
        # Add your event-handling code here

    def label_action(self, *args):
        print("Label button pressed")
        # Add your event-handling code here

    def bookmark_action(self, *args):
        self.load_data()
        print("Bookmark button pressed")
        # Add your event-handling code here
        
    def load_data(self):
        # Get the GridLayout from the KV file by its id
        grid = self.root.ids.table_grid
        # Clear any existing widgets (previous data)
        grid.clear_widgets()

        # Define the headers for your table
        headers = ["ID", "name", "vorname", "geburtstag"]

        # Add the header row
        for header in headers:
            label = MDLabel(
                text=header,
                halign="center",
                bold=True,
                size_hint_y=None,
                height=40,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)  # white text
            )
            grid.add_widget(label)

        # Sample data rows; replace this list with your actual data.
        data = [
            {"ID": "1", "name": "Alice", "vorname": "Smith", "geburtstag": "1990-01-01"},
            {"ID": "2", "name": "Bob", "vorname": "Jones", "geburtstag": "1985-05-12"},
        ]

        # Add data rows. This loops over each row in your data and adds a cell for each header.
        for row in data:
            for header in headers:
                cell = MDLabel(
                    text=str(row.get(header, "")),
                    halign="center",
                    size_hint_y=None,
                    height=30,
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)  # white text
                )
                grid.add_widget(cell)


    def build(self):
        # Set primary theme color to Aliceblue (RGBA: [0.941, 0.973, 1, 1])
        self.theme_cls.primary_color = [0.941, 0.973, 1, 1]
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

MyApp().run()
