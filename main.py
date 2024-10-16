from score_keeper.keeper import Keeper
from score_keeper.score import *


def main():
    main_terminal()

def score_terminal(filters, df):
    filters_cleaned = [i.strip() if any(char.isalnum() for char in i) else None
                       for i in filters.split(sep=',')]
    if len(filters_cleaned) < 4:
        filters_cleaned.extend([None] * (4 - len(filters_cleaned)))
    elif len(filters_cleaned) > 4:
        print('Too many filters, terminating')
        return 1
    print(f'Semester={filters_cleaned[0]}, Subject={filters_cleaned[1]}, Date={filters_cleaned[2]}, '
          f'grade={filters_cleaned[3]}')
    df['Date'] = pd.to_datetime(df['Date'])
    df = filter_data(df, *filters_cleaned)
    while True:
        choice_score = input('What do you want to do?\n'
                '1. Show stats\n2. Plot grades distribution\n3. Plot avg per grade semester\n4. Show data\n5. Exit\n')
        close_plots()
        match choice_score:
            case '1':
                show_info(df)
            case '2':
                plot_grades_bar_distribution(df)
            case '3':
                plot_avg_grade_per_semester(df)
            case '4':
                print(df)
            case '5':
                break
            case _:
                print('Invalid choice. Please try again.')
    
def main_terminal():
    """
    Main function for the terminal interface.
    :return: 0
    """
    print('Welcome to the score keeper!')
    grades_keeper = Keeper()
    while True:
        print('What do you want to do?\n1. Enter score calculations mode\n2. Show grades\n3. Add grades\n'
              '4. Save grades to a file\n5. Load grades from a file\n6. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                filters = input(
                    "Please enter your filters (leave blank for 'all').\n"
                    "Options:\n"
                    "- Semester: e.g., '4' or '> 6' or 'between both including 4 and 6'\n"
                    "- Subject: e.g., 'Mathematics' or 'Physics Computer Science'\n"
                    "- Date of entry: format as '< YYYY-MM-DD', '> YYYY-MM-DD', 'between both including YYYY-MM-DD"
                    "and YYYY-MM-DD' or 'YYYY-MM-DD'\n"
                    "- Grade: specify the exact grade as a number\n\n"
                    "Example: 3 6,, 2023-01-01 2023-06-30, 5\n"
                    "Example 2: , Mathematics Computer Science\n"
                    "\nPlease enter filters: "
                )
                score_terminal(filters, grades_keeper.data)
            case '2':
                grades_keeper.show_data()
                print('Data shown.')
            case '3':
                while True:
                    grades_keeper.get_data_from_terminal_single()
                    print('You entered the following data:')
                    grades_keeper.show_current_data()
                    if input('Do you want to add the next grade? If so, press Enter. Otherwise, enter 0.\n'):
                        grades_keeper.add_current_data()
                        print('Data added.')
                        break
            case '4':
                grades_keeper.save_data_to_file()
                print('Data saved.')
            case '5':
                if grades_keeper.get_data_from_file() == 0:
                    print('Data loaded.')
            case'6':
                break
            case _:
                print('Invalid choice. Please try again.')
    print('Finished')
    return 0


if __name__ == '__main__':
    main()
