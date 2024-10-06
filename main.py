from keeper.keeper import Keeper


def main():
    print(f'Hi')
    grades_keeper = Keeper()
    while input('Do you want to add the next grade? If so, enter 1.\n') == '1':
        grades_keeper.get_data_from_terminal_single()
        print('You entered the following data:')
        grades_keeper.show_current_data()
    grades_keeper.add_current_data()
    print('Finished')


if __name__ == '__main__':
    main()
