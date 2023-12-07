from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_remote):
    """Handles all the logic for the gui as well as for the remotes status
    Attributes:
        __status (str): the power state of the tv
        __muted (str): the muted state of the tv
        __volume (str): the volume level of the tv
        __channel (str): the channel number of the tv
        """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """Initializes the logic class and invokes methods as needed"""
        self.__status: str = self.file_read("power")
        self.__muted: str = self.file_read("mute")
        self.__volume: str = self.file_read("volume")
        self.__channel: str = self.file_read("channel")
        super().__init__()
        self.setupUi(self)
        self.update(self.file_read(all_values=True))

        self.power_button.clicked.connect(lambda: self.power())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.channe_up_button.clicked.connect(lambda: self.channel_up())
        self.channe_down_button.clicked.connect(lambda: self.channel_down())

    def power(self):
        """Switches the television between on and off"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: str = dictionary['power']
        if current_state == 'true':
            dictionary['power']: str = 'false'
        else:
            dictionary['power']: str = 'true'
        self.update(dictionary)
        self.file_write(dictionary)

    def volume_up(self):
        """Increases the televisions volume by one until
         the televisions maximum volume is reached"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: int = int(dictionary['volume'])
        if current_state < self.MAX_VOLUME:
            current_state += 1
            dictionary['volume']: str = str(current_state)
            self.file_write(dictionary)
            self.update(dictionary)
        else:
            pass

    def volume_down(self):
        """Decreases the televisions volume by one until
                 the televisions minimum volume is reached"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: int = int(dictionary['volume'])
        if current_state > self.MIN_VOLUME:
            current_state -= 1
            dictionary['volume']: str = str(current_state)
            self.file_write(dictionary)
            self.update(dictionary)
        else:
            pass

    def mute(self):
        """Switches the television between muted and not muted"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: str = dictionary['mute']
        if current_state == 'true':
            dictionary['mute']: str = 'false'
        else:
            dictionary['mute']: str = 'true'
        self.update(dictionary)
        self.file_write(dictionary)

    def channel_up(self):
        """Increases the televisions channel by one until
         the televisions maximum channel is reached"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: int = int(dictionary['channel'])
        if current_state < self.MAX_CHANNEL:
            current_state += 1
            dictionary['channel']: str = str(current_state)
            self.file_write(dictionary)
            self.update(dictionary)
        else:
            pass

    def channel_down(self):
        """Decreases the televisions channel by one until
                 the televisions minimum channel is reached"""
        dictionary: dict = self.file_read(all_values=True)
        current_state: int = int(dictionary['channel'])
        if current_state > self.MIN_CHANNEL:
            current_state -= 1
            dictionary['channel']: str = str(current_state)
            self.file_write(dictionary)
            self.update(dictionary)
        else:
            pass

    def update(self, dictionary):
        """Updates the televisions status on the GUI
        :param dictionary: (dict): a dictionary containing the televisions current status information
        """
        if dictionary['mute'] == 'true':
            volume: str = '0'
        else:
            volume: str = dictionary['volume']
        self.tv_status.setText(f"Power: {dictionary['power']}\nVolume: {volume}\nChannel: {dictionary['channel']}\nMuted: {dictionary['mute']}")

    def file_write(self, dictionary: dict):
        """Writes the televisions status information to a csv file to be stored
        :param dictionary: (dict): a dictionary containing the televisions current status information
            """
        with open('file.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile)
            for key, value in dictionary.items():
                content.writerow((key, value))
        csvfile.close()

    def file_read(self, value_type: str = None, all_values: bool = False):
        """Reads the televisions stored status information from a csv file
        :param value_type: (str): a string containing the requested status type to
        be returned. ie: "power"
        :param all_values: (bool): a bool that is by default False. If the parameter
        is passed as true the function will return the
        :return: dictionary of either a specific status or all status
        """
        with open('file.csv', 'r') as in_file:
            csv_reader = csv.reader(in_file, delimiter=',')
            dictionary: dict = {rows[0]: rows[1] for rows in csv_reader}
        if not all_values:
            return dictionary[value_type]
        else:
            return dictionary


