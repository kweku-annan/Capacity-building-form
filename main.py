from kivy.config import Config

# Config.set('graphics', 'resizable', False)
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

# TODO 1: Search for how you can set a default title for the app.

Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size


class StartWindow(BoxLayout, Screen):
    pass


class MainWindow(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clear(self):
        self.ids.participant_name.text = ""
        self.ids.contact.text = ""
        self.ids.email.text = ""
        self.ids.location.text = ""

    def save_data(self):
        """The purpose of this function is to collect all the entries in the TextInput and save it in a CSV and xlsx
        files under their respective headers.
        """
        name = self.ids.participant_name.text
        contact = self.ids.contact.text
        email = self.ids.email.text
        location = self.ids.location.text

        # print(f"{name}'s contact is {contact}, email is {email} and stays at {location}")
        first_name = name.split(" ")[0]
        surname = ""
        if len(name.split(" ")) - 1 > 0:
            surname = name.split(" ")[1]

        # Creating the file and its entries.

        file_name = "test_file"
        file_path = f"data/{file_name}"  # Setting the file name

        data_dict = {
            "First Name": [first_name.title()],
            "Surname": [surname.title()],
            "Contact": [contact],
            "Email": [email],
            "Location": [location.title()],
        }
        data = pd.DataFrame(data_dict, index=None)
        # print(data.head())

        with open(file_path, "a") as file:
            data.to_csv(f"{file}.csv", mode='a', header=file.tell() == 0)

        self.clear()
        # if os.path.isfile(f"{file_path}.xlsx") is False or os.path.isfile(f"{file_name}.csv") is False:
        # data.to_excel(f"{file_path}.xlsx") data.to_csv(f"{file_path}.csv") elif os.path.isfile(f"{file_path}.xlsx")
        # is True or os.path.isfile(f"{file_path}.csv") is True: data.to_csv(f"{file_path}.csv", mode='a',
        # header=False) with pd.ExcelWriter(path=f"{file_path}", engine="openpyxl", mode="a",
        # if_sheet_exists="overlay") as writer: data.to_excel(writer, sheet_name=f"{file_name}")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')


class DataCollectionApp(App):
    def build(self):
        self.title = "Data Collector"
        # return MainWindow()
        return kv


if __name__ == "__main__":
    DataCollectionApp().run()
