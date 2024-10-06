import pandas as pd
import numpy as np
import datetime


class Keeper:
    def __init__(self):
        self.data = pd.DataFrame({'Date': [], 'Semester': [], 'Subject': [], 'Grade': []})
        # self.current_data = self.data.copy(deep=True)
        self.current_data = list()

    def get_data_from_terminal_single(self):
        """
        Asks user for data via terminal. Gets semester, subject, grade and current date
        and save it in current data.
        :return: 0
        """
        date = datetime.datetime.now().date()
        semester = input('Current semester: ')
        subject = input('Subject: ')
        grade = input('Grade: ')
        self.current_data.append((date, semester, subject, grade))
        return 0

    def add_current_data(self):
        """
        Appends the current data to the main data storage
        :return: 0
        """
        self.data = pd.concat([self.data,
                               pd.DataFrame(self.current_data, columns=self.data.columns)])
        self.data.reset_index(inplace=True)
        return 0

    def show_current_data(self):
        """
        Prints current data variable in a friendly way.
        :return:
        """
        [print(f'Date: {i[0]}, Semester: {i[1]}, Subject: {i[2]}, Grade: {i[3]}') for i in self.current_data]
        return 0
