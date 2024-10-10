from score_keeper.keeper import Keeper


def main():
    main_terminal()
    
def main_terminal():
    """
    Main function for the terminal interface.
    :return: 0
    """
    print('Welcome to the score keeper!')
    grades_keeper = Keeper()
    while True:
        print('What do you want to do?\n1. Enter score calulations mode\n2. Show grades\n3. Add grades\n4. Save grades to a file\n5. Load grades from a file\n6. Exit')
        choice = input('Enter your choice: ')
        match choice:
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
