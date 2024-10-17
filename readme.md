# ScoreKeeper
ScoreKeeper is a terminal-based application for managing and analyzing student grades. It allows users to enter, view,
filter, and save grades, as well as perform various statistical analyses and visualizations.
Additionally, a Streamlit interface provides a more interactive way to manage grades.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/ScoreKeeper.git
    cd ScoreKeeper
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Terminal Interface
1. **Run the main script:**
    ```sh
    python main.py
    ```
2. **Follow the on-screen instructions to navigate through the menu options.**

### Streamlit Interface
1. **Run the Streamlit script:**
    ```sh
    streamlit run main_streamlit.py
    ```
2. **Open the provided URL in a web browser to access the Streamlit interface.**

## Features

- **Enter Score Calculations Mode:** Filter and analyze grades based on various criteria.
- **Show Grades:** Display all stored grades.
- **Add Grades:** Manually input new grades.
- **Save Grades to a File:** Save the current grades to a CSV file.
- **Load Grades from a File:** Load grades from a CSV file.
- **Exit:** Exit the application.
- **Streamlit Interface:** An interactive web interface for managing grades.

## File Structure

```
data/
    grades.csv
main.py
main_streamlit.py
requirements.txt
score_keeper/
    __init__.py
    keeper.py
    score.py
tests/
    test_filter_data.py
    test_terminal.py
```
- **data/grades.csv**: Contains the stored grades data.
- **main.py**: Entry point for the application.
- **score_keeper/keeper.py**: Contains the `Keeper` class for managing grades.
- **score_keeper/score.py**: Contains functions for filtering and analyzing grades.
- **tests/**: Contains unit tests for the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---