import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union
import plotext as pltxt


def filter_data(df: pd.DataFrame, semester: str=None, subject: str=None,
                date: str=None, grade: str=None) -> Union[pd.DataFrame, None]:
    """Filters data by a specific subject, semester, grade, or limit by date."""

    def validate_data(data: str) -> Union[tuple, None]:
        """Validates the input data."""
        data = [i.strip().replace(',', '.') for i in data.split(' ')]
        # try:
        if len(data) > 2:
            raise ValueError('Too many values.')

        elif len(data) == 1:
            if data[0].replace('.', '', 1).isdigit():
                data[0] = float(data[0])
            else:
                data[0] = pd.to_datetime(data[0], errors='raise')
            return tuple(data)

        else:
            greater_than = None
            if data[0].replace('.', '', 1).isdigit():
                data[0] = float(data[0])
            elif data[0] in '><':
                greater_than = True if data[0] == '>' else False
            elif pd.to_datetime(data[0], errors='raise') is not pd.NaT:
                data[0] = pd.to_datetime(data[0])
            else:
                raise ValueError('Invalid first value.')

            if data[1].replace('.', '', 1).isdigit():
                data[1] = float(data[1])
            elif data[1] in '><':
                if greater_than:
                    raise ValueError('Not enough numbers.')
                greater_than = True if data[1] == '<' else False
            elif pd.to_datetime(data[1], errors='raise') is not pd.NaT:
                data[1] = pd.to_datetime(data[1])

            if greater_than is not None:
                value = data[0] if data[0] not in ('>', '<') else data[1]
                return value, '+' if greater_than else '-'
            else:
                return min(data), max(data)

    def filter_df_column(df_main: pd.DataFrame, data: tuple, column_name: str) -> Union[pd.DataFrame, None]:
        """Filters a DataFrame by a specific column."""
        if len(data) == 1:
            df_main = df_main[df_main[column_name] == data[0]]
            return df_main
        elif len(data) == 2:
            if data[1] == '+' or data[1] == '-':
                if data[1] == '+':
                    df_main = df_main[df_main[column_name] > data[0]]
                else:
                    df_main = df_main[df_main[column_name] < data[0]]
            else:
                df_main = df_main[(df_main[column_name] >= data[0]) & (df_main[column_name] <= data[1])]
        else:
            raise ValueError('Invalid data.')
        return df_main
    if subject:
        try:
            subject_cleaned = [i.strip().lower() for i in subject.split(' ')]
            df = df[df['Subject'].str.lower().isin(subject_cleaned)]
        except Exception as e:
            print('Subject error\n', e)
    if semester:
        try:
            semester_cleaned = validate_data(semester)
            df = filter_df_column(df, semester_cleaned, 'Semester')
        except Exception as e:
            print('Semester error\n', e)
    if date:
        try:
            date_cleaned = validate_data(date)
            df = filter_df_column(df, date_cleaned, 'Date')
        except Exception as e:
            print('Date error\n', e)
    if grade:
        try:
            grade_cleaned = validate_data(grade)
            df = filter_df_column(df, grade_cleaned, 'Grade')
        except Exception as e:
            print('Grade error\n', e)
    return df

def show_info(df: pd.DataFrame) -> int:
    """Shows basic info about the DataFrame."""
    print(df.describe().loc[['count', 'mean', 'min', '25%', '50%', '75%', 'max']])
    return 0

def plot_grades_bar_distribution(df: pd.DataFrame, return_fig=False) -> Union[int, plt.Figure]:
    """Plots a bar distribution of grades with count labels above each bar."""
    grade_counts = df['Grade'].value_counts().reindex(np.arange(2, 5.5, 0.5), fill_value=0)

    if return_fig:
        # Use matplotlib for returning the figure to Streamlit
        fig, ax = plt.subplots(figsize=(14, 7))
        bars = ax.bar(np.arange(2, 5.5, 0.5), grade_counts.values, color='#4C72B0', alpha=0.8, edgecolor='black', width=0.4)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

        ax.set_xlabel('Grade', fontsize=12, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax.set_title('Grade Distribution', fontsize=15, fontweight='bold', color='#4C72B0')
        ax.set_xticks(np.arange(2, 5.5, 0.5))
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        return fig

    else:
        # Use plotext for terminal output
        pltxt.clear_figure()
        pltxt.title("Grade Distribution")
        pltxt.bar(grade_counts.index.astype(str), grade_counts.values, label="Frequency", color="blue")
        pltxt.xlabel("Grade")
        pltxt.ylabel("Frequency")
        pltxt.show()
        return 0

def plot_avg_grade_per_semester(df: pd.DataFrame, return_fig=False) -> Union[int, plt.Figure]:
    """Plots the average grade per semester with confidence intervals."""
    avg_grades = df.groupby('Semester')['Grade'].agg(['mean', 'std']).reset_index()

    if return_fig:
        # Use matplotlib for returning the figure to Streamlit
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.errorbar(avg_grades['Semester'], avg_grades['mean'], yerr=avg_grades['std'],
                    fmt='-o', color='#55A868', ecolor='gray', capsize=5, capthick=1, markersize=6)
        
        for i in range(len(avg_grades)):
            ax.text(avg_grades['Semester'][i], avg_grades['mean'][i] + 0.05,
                    f'{avg_grades["mean"][i]:.2f}', ha='center', va='bottom',
                    fontsize=10, fontweight='bold', color='black')

        ax.set_xlabel('Semester', fontsize=12, fontweight='bold')
        ax.set_xticks(avg_grades['Semester'].astype(int))
        ax.set_ylabel('Average Grade', fontsize=12, fontweight='bold')
        ax.set_yticks(ticks=np.arange(2, 5.5, 0.5))
        ax.set_title('Average Grade per Semester', fontsize=15, fontweight='bold', color='#55A868')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        return fig

    else:
        # Use plotext for terminal output
        pltxt.clear_figure()
        pltxt.title("Average Grade per Semester")
        pltxt.scatter(avg_grades['Semester'], avg_grades['mean'], label="Avg Grade", color="green")
        pltxt.plot(avg_grades['Semester'], avg_grades['mean'], color="green")
        pltxt.ylabel("Average Grade")
        pltxt.xlabel("Semester")
        pltxt.show()
        return 0

def close_plots() -> int:
    """Closes all open plots."""
    plt.close('all')
    return 0
