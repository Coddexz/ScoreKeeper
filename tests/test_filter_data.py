import unittest
import pandas as pd
from score_keeper.score import filter_data

class TestFilterData(unittest.TestCase):

    def setUp(self):
        data = {
            'Semester': [1, 2, 1, 2],
            'Subject': ['Maths', 'Science', 'Maths', 'Science'],
            'Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']),
            'Grade': [5, 4.5, 3, 2]
        }
        self.df = pd.DataFrame(data)

    def test_semester_filter(self):
        result = filter_data(self.df, semester='1')
        self.assertEqual(len(result), 2)
        self.assertTrue((result['Semester'] == 1).all())

    def test_subject_filter(self):
        result = filter_data(self.df, subject='Maths')
        self.assertEqual(len(result), 2)
        self.assertTrue((result['Subject'] == 'Maths').all())

    def test_date_filter(self):
        result = filter_data(self.df, date='2023-01-01')
        self.assertEqual(len(result), 1)
        self.assertTrue((result['Date'] == pd.to_datetime('2023-01-01')).all())

    def test_grade_filter(self):
        result = filter_data(self.df, grade='5')
        self.assertEqual(len(result), 1)
        self.assertTrue((result['Grade'] == 5).all())

    def test_combined_filters(self):
        result = filter_data(self.df, semester='1', subject='Maths', date='2023-01-01', grade='5')
        self.assertEqual(len(result), 1)
        self.assertTrue((result['Semester'] == 1).all())
        self.assertTrue((result['Subject'] == 'Maths').all())
        self.assertTrue((result['Date'] == pd.to_datetime('2023-01-01')).all())
        self.assertTrue((result['Grade'] == 5).all())

    def test_combined_multi_filters(self):
        result = filter_data(self.df, semester='1 3', subject='Maths Science', date='2023-01-01 2023-03-01',
                             grade='2, 5')
        self.assertEqual(len(result), 3)

    def test_invalid_semester(self):
        result = filter_data(self.df, semester='3')
        self.assertEqual(len(result), 0)

    def test_invalid_subject(self):
        result = filter_data(self.df, subject='History')
        self.assertEqual(len(result), 0)

    def test_invalid_date(self):
        result = filter_data(self.df, date='2022-01-01')
        self.assertEqual(len(result), 0)

    def test_invalid_grade(self):
        result = filter_data(self.df, grade='6')
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()