import pandas as pd
import numpy as np
import datetime
import os


class Keeper:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Date', 'Semester', 'Subject', 'Grade'])
        self.current_data = list()

    def get_data_from_terminal_single(self, grade_range: tuple=(2, 5)):
        """
        Asks user for data via terminal. Gets semester, subject, grade and current date
        and save it in current data.
        :return: 0
        """
        try:
            date = datetime.datetime.now().date()
            semester = input('Current semester: ')
            if not semester.isdigit() or not (1 <= int(semester) <= 14):
                raise ValueError('Invalid semester input. Must be a number between 1 and 14!')
            
            subject = input('Subject: ')
            if not subject.replace(' ', '').isalpha():
                raise ValueError('Invalid subject input. Must be a string!')
            
            grade = input('Grade: ').replace(',', '.')
            print(grade)
            if not (grade.replace('.', '', 1).isdigit()
                and grade_range[0] <= float(grade) <= grade_range[1]
                and float(grade) % 0.5 == 0):
                raise ValueError('Invalid grade input. Must be a number between 2 and 5 with a step of 0.5!')
            
            self.current_data.append((date, semester, subject, float(grade)))
        except ValueError as e:
            print(e)
        return 0
    
    def get_data_from_file(self, filename='grades.csv'):
        """
        Reads data from a csv file.
        :param filename: str
        :return: 0
        """
        try:
            self.data = pd.read_csv(os.path.join(os.getcwd(), 'data', filename))
        except FileNotFoundError:
            print('File not found.')
            return 1
        return 0

    def add_current_data(self):
        """
        Appends the current data to the main data storage
        :return: 0
        """
        current_data = pd.DataFrame(self.current_data, columns=['Date', 'Semester', 'Subject', 'Grade'])
        if self.data.empty:
            self.data = current_data
        else:
            self.data = pd.concat([self.data, current_data], ignore_index=True)
        return 0

    def show_current_data(self):
        """
        Prints current data variable in a friendly way.
        :return:
        """
        for i in self.current_data:
            print(f'Date: {i[0]}, Semester: {i[1]}, Subject: {i[2]}, Grade: {i[3]}')
        return 0
    
    def show_data(self):
        """
        Prints the data in a friendly way.
        :return: 0
        """
        print(self.data.to_string())
        return 0
    
    def save_data_to_file(self, filename='grades.csv'):
        """
        Saves the data to a csv file.
        :param filename: str
        :return: 0
        """
        self.data.to_csv(os.path.join(os.getcwd(), 'data', filename), index=False)
        return 0
