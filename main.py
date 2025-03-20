from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

class MyApp(MDApp):
    menu = None

    def build(self):
        self.theme_cls.primary_palette = "Aliceblue"
        return Builder.load_file("main.kv")

    def open_menu(self):
        # Define dropdown menu items
        menu_items = [
            {
                "text": "File",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="File": self.menu_callback(x),
            },
            {
                "text": "Konfiguration",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Konfiguration": self.menu_callback(x),
            },
            {
                "text": "Table",
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Table": self.menu_callback(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.top_app_bar,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def menu_callback(self, menu_name):
        self.menu.dismiss()
        if menu_name == "File":
            self.root.ids.file_dialog.open()
        elif menu_name == "Konfiguration":
            self.root.ids.konfiguration_dialog.open()
        elif menu_name == "Table":
            self.root.ids.table_dialog.open()

MyApp().run()
