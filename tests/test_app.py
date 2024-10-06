import unittest
from unittest.mock import patch
import datetime
from keeper.keeper import Keeper


class TestTerminalInput(unittest.TestCase):

    @patch('builtins.input',
           side_effect=['1', 'Maths', '5'])
    def test_date_present(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertIsInstance(keeper.current_data[0][0], datetime.datetime)
    @patch('builtins.input',
           side_effect=['1', 'Maths', '5'])
    def test_correct_semester(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        semester = '1'
        self.assertIn(keeper.current_data[0][1], semester)

    @patch('builtins.input',
           side_effect=['A', 'Maths', '5'])
    def test_incorrect_semester_letter(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        semester = '1'
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['0', 'Maths', '5'])
    def test_incorrect_semester_under_range(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['6540', 'Maths', '5'])
    def test_incorrect_semester_above_range(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['$', 'Maths', '5'])
    def test_incorrect_semester_symbol(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['', 'Maths', '5'])
    def test_incorrect_semester_empty(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '5'])
    def test_correct_subject(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        subject = 'Maths'
        self.assertEqual(keeper.current_data[0][2], subject)

    @patch('builtins.input',
           side_effect=['1', 'English Language', '5'])
    def test_correct_subject_two_words(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        subject = 'English Language'
        self.assertEqual(keeper.current_data[0][2], subject)

    @patch('builtins.input',
           side_effect=['1', '5', '5'])
    def test_incorrect_subject_digit_in(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', '$', '5'])
    def test_incorrect_subject_symbol(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', '', '5'])
    def test_incorrect_subject_no_input(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '5'])
    def test_correct_grade(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        grade = '5'
        self.assertEqual(keeper.current_data[0][3], grade)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '4.5'])
    def test_correct_grade_float(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        grade = '4.5'
        self.assertEqual(keeper.current_data[0][3], grade)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '0'])
    def test_incorrect_grade_below_range(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '-2'])
    def test_incorrect_grade_negative_value(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '7'])
    def test_incorrect_grade_above_range(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', 'P'])
    def test_incorrect_grade_letter(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '$'])
    def test_incorrect_grade_symbol(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '4.333'])
    def test_incorrect_grade_float(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', ' 4'])
    def test_incorrect_grade_length(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', ''])
    def test_incorrect_grade_no_input(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 0)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '5', '1', 'Maths', '5'])
    def test_many_inputs(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        keeper.get_data_from_terminal_single()
        self.assertEqual(len(keeper.current_data), 2)

    def test_shows(self):
        keeper = Keeper()
        raised = False
        try:
            keeper.show_current_data()
        except:
            raised = True
        self.assertFalse(raised)

    @patch('builtins.input',
           side_effect=['1', 'Maths', '5', '1', 'Maths', '5'])
    def test_data_concat(self, mock_input):
        keeper = Keeper()
        keeper.get_data_from_terminal_single()
        keeper.get_data_from_terminal_single()
        keeper.add_current_data()
        self.assertEqual(len(keeper.data), 2)


if __name__ == '__main__':
    unittest.main()
