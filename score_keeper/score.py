import pandas as pd
import matplotlib.pyplot as plt


def filter_data(df: pd.DataFrame, subject: str=None, semester: str=None,
                date: str=None, grade: float=None) -> pd.DataFrame:
    """Filters data by a specific subject, semester, grade, or limit by date."""
    if subject:
        df = df[df['Subject'] == subject]
    if semester:
        df = df[df['Semester'] == semester]
    if date:
        df = df[pd.to_datetime(df['Date']) >= pd.to_datetime(date)]
    if grade:
        df = df[df['Grade'] == grade]
    return df

def calculate_average(df: pd.DataFrame, subject: str=None) -> float:
    """Calculates the average grade, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    return df['Grade'].mean()

def calculate_median(df: pd.DataFrame, subject: str=None) -> float:
    """Calculates the median grade, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    return df['Grade'].median()

def calculate_highestdf(df: pd.DataFrame, subject: str=None) -> float:
    """Finds the highest grade, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    return df['Grade'].max()

def calculate_lowest(df: pd.DataFrame, subject: str=None) -> float:
    """Finds the lowest grade, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    return df['Grade'].min()

def plot_gradesdf(df: pd.DataFrame, subject: str=None) -> int:
    """Plots grades over time, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Grade'], marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Grade')
    plt.title(f"Grades Over Time{' for ' + subject if subject else ''}")
    plt.show()
    return 0

def plot_distributiondf(df: pd.DataFrame, subject: str=None) -> int:
    """Plots a distribution of grades, optionally filtered by a specific subject."""
    if subject:
        df = df[df['Subject'] == subject]
    plt.figure(figsize=(8, 5))
    plt.hist(df['Grade'], bins=10, edgecolor='black')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.title(f"Grade Distribution{' for ' + subject if subject else ''}")
    plt.show()
    return 0
