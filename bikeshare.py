import pyfiglet as pfg
from termcolor import colored as tc
import calendar as cal
import time as T
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.ticker as mticker
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
register_matplotlib_converters()
# to generate a list of months
d_month = cal.month_name[1:]+['All']
d_day = cal.day_name[:]+['All']
valid_entries = ['Yes', 'No']

CITY_DATA = {'chicago': 'chicago.csv',
             'newyork': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters() -> str:
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print(tc('Hello! Let\'s explore some US bike share data!'.title(), color='green'))
    city = input(
        "Would you like to see data for Chicago, New York, or Washington\n==>".title()).lower().strip().replace(" ", "")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print('please enter a valid city name'.title())
        city = input(
            "Would you like to see data for Chicago, New York, or Washington\n==>".title()).lower().strip().replace(" ", "")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Would you like to filter the data by month or day \nif not type all\nif yes please enter a month name (all, january, february, ... , june)\n==>".title()).title().strip().replace(" ", "")
        if month not in d_month:
            print("invalid input for months".title())
        else:

            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "please choose a day (all, monday, tuesday, ... sunday)\n".title()).title().strip().replace(" ", "")
        if day not in d_day:
            print("invalid input for days".title())
        else:
            res = tc(pfg.figlet_format(
                "Loading Data!", font="digital"), color='cyan')
            print(res)
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day) -> str:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    # adding month ,day,hour and route columns to the dataset
    df['month'] = df['Start Time'].dt.month_name()
    df['day_name'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    df['start_end'] = df['Start Station']+" to "+df['End Station']
    if month == "All":
        df = df
    else:
        df = df[df['month'] == month]
    if day == "All":
        df = df
    else:
        df = df[df['day_name'] == day]

    return df


def time_stats(df) -> pd.DataFrame:
    """Displays statistics on the most frequent times of travel."""

    print(tc('\nCalculating The Most Frequent Times of Travel...\n', color="cyan"))
    start_time = T.time()

    # display the most common month
    print(f'the most common month is {df.month.mode()[0]} .'.title())
    # display the most common day of week
    print(
        f'the most common day of the week is {df.day_name.mode()[0]} .'.title())
    # display the most common start hour
    print(f'the most common start hour is {df.start_hour.mode()[0]} .'.title())
    print(f"\nThis took {T.time() - start_time} seconds.".title())
    print('-'*40)


def station_stats(df) -> pd.DataFrame:
    """Displays statistics on the most popular stations and trip."""

    print(tc('\nCalculating The Most Popular Stations and Route...\n', color='cyan'))
    start_time = T.time()

    # display most commonly used start station
    print(
        f"the most commonly used start station is {df['Start Station'].mode()[0]}".title())
    # display most commonly used end station
    print(
        f"the most commonly used end station is {df['End Station'].mode()[0]}".title())
    # display most frequent combination of start station and end station trip
    print(
        tc(f"the most commonly used route is ({df['start_end'].mode()[0]}) this route repeated {df[df['start_end']==df['start_end'].mode()[0]]['start_end'].count()} times \nwith {round(((df[df['start_end']==df['start_end'].mode()[0]]['start_end'].count())/df['start_end'].count())*100,2)}% of total routs .".title(), color='yellow'))
    print(f"\nThis took {T.time() - start_time}seconds.".title())
    print('-'*40)


def trip_duration_stats(df) -> pd.DataFrame:
    """Displays statistics on the total and average trip duration."""

    print(tc('\nCalculating Trip Duration...\n'.title(), color='cyan'))
    start_time = T.time()

    # display total travel time
    print(
        f"total travel time for this city is ==> {round((df['Trip Duration'].sum())/3600,2)} hours".title())
    # display mean travel time
    print(
        f"the average travel time is ==> {round((df['Trip Duration'].mean()/60),2)} minutes ".title())
    print(f"\nThis took {T.time() - start_time} seconds.".title())
    print('-'*40)


def user_stats(df) -> pd.DataFrame:
    """Displays statistics on bikeshare users."""

    print(tc('\nCalculating User Stats...\n', color='cyan'))
    start_time = T.time()

    # Display counts of user types from User Type  col
    print(
        f"we have {len((df['User Type'].value_counts().to_dict()))} kind of users==> ".title())
    for x, y in (df['User Type'].value_counts().to_dict()).items():
        print(f"a {y} of {x}s".title())
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    # am gonna use Try statement because washington dont have a birth or gender cols
    print('-'*40)
    #df['Birth Year'] = df['Birth Year'].apply(int)

    print(tc("genders and ages distribution in this city is==>".title(), color='cyan'))
    print('-'*40)
    try:
        for x, y in (df['Gender'].value_counts().to_dict()).items():
            print(f"a {y} of {x}s".title())
        print('-'*40)
        print(tc("the age range for this city is ==>".title(), color='cyan'))
        print('-'*40)

        print(
            f"the most earliest year of birth is {int(df['Birth Year'].min())}".title())
        print(
            f"the most most recent year of birth is {int(df['Birth Year'].max())}".title())
        print(
            f"the most common year of birth is {int(df['Birth Year'].mode()[0])}".title())
        print('-'*40)
    except:
        print(tc(f"there is no data about gender or birth year in this city".title(), color='red'))
    print(f"\nThis took {T.time() - start_time} seconds.".title())
    print('-'*40)


i = 0  # this counter for showing user data


def ask_for_rows(df) -> pd.DataFrame:
    '''ths fun return 5 rows for user based on his input after asking...'''
    var = ['yes', 'no']
    x = str(
        input("Do you wanna see some rows from this city (yes,no)? ==>".title())).lower()
    if x not in var:
        print(tc("invalid input please enter (yes,no)".title(), color='red'))
        return ask_for_rows(df)
    else:
        if x in var:
            if x == "yes":
                global i
                if i > df.count()[0]:
                    print(tc('no more rows to show thank you'.title(), color='yellow'))
                    return
                print(
                    tc(f'here is some rows from row {i} to row {i+4}'.title(), color='cyan'))
                print(tc(df.iloc[i:i+5], color='green'))
                i += 5
                return ask_for_rows(df)


def main() -> str:
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_for_rows(df)

        restart = input(
            tc('\nWould you like to restart? Enter yes or no.\n', color='magenta'))
        if restart.lower() != 'yes':
            break
        else:
            global i
            i = 0


if __name__ == "__main__":
    main()
