
# Webpages that I used for help
#
# https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
# https://stackoverflow.com/questions/6557553/get-month-name-from-number
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month_name.html
# https://stackoverflow.com/questions/7479777/difference-between-python-datetime-vs-time-modules
# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
# https://kite.com/python/answers/how-to-add-commas-to-a-number-in-python
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-32.php


import time
import math
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

CITIES = ['Chicago', 'New York', 'Washington']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

HOURS_DESC = ['Midnight - 1 AM', '1 AM - 2 AM', '2 AM - 3 AM', '3 AM - 4 AM', '4 AM - 5 AM', '5 AM - 6 AM',
        '6 AM - 7 AM', '7 AM - 8 AM', '8 AM - 9 AM', '9 AM - 10 AM', '10 AM - 11 AM', '11 AM - Noon',
        'Noon - 1 PM', '1 PM - 2 PM', '2 PM - 3 PM', '3 PM - 4 PM', '4 PM - 5 PM', '5 PM - 6 PM',
        '6 PM - 7 PM', '7 PM - 8 PM', '8 PM - 9 PM', '9 PM - 10 PM', '10 PM - 11 PM', '11 PM - Midnight']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city do you want to select?  (Chicago, New York or Washington) \n> ').lower()
       if city.title() in CITIES:
            city = city.title()
            break
       else:
        # Let them try again if they enter invalid data
            print('\nThe city you entered is not valid.  Please try again. \n')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month do you want to select? \n (Please input either "all" or January, Febuary, March, April, May or June) \n').lower()
        if month.title() in MONTHS:
            month = month.title()
            break
        else:
        # Let them try again if they enter invalid data
            print('\nThe month you entered is not valid.  Please try again. \n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day do you want to select? \n (Please input either "all" or Monday, Tuesday... Sunday.) \n').lower()
        if day.title() in DAYS:
            day = day.title()
            break
        else:
        # Let them try again if they enter invalid data
            print('\nThe day you entered is not valid.  Please try again. \n')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data to Pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to a datetime Data Type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Use 'Start Time' to create a 'Month' column
    df['month'] = df['Start Time'].dt.month_name()

    # Use 'Start Time' to create a 'Day' column
    df['day'] = df['Start Time'].dt.day_name()

    # Use 'Start Time' to create ah 'Hour' column
    df['hour'] = df['Start Time'].dt.hour

    # If month is not 'All', then filter by months
    if month != 'All':
        df = df[ df['month'] == month ]

    # If day is not 'All', then filter by day
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[ df['day'] == day ]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Mode returns an array, which can have multiple values if there are multiple modes, so I'm taking the first value in the array
    most_common_month = df['month'].mode()[0]
    print("The common month is: " + most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("The most common day of the week is:  " + most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is:  " + str(most_common_start_hour) + '  (' + HOURS_DESC[most_common_start_hour] +')')

    print("\nThis took " + "{:.4f}".format(time.time() - start_time) + " seconds.")
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:  " + most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df1 = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    print("The most frequent combination of start station and end station trip is " + df1.mode()[0])


    print("\nThis took " + "{:.4f}".format(time.time() - start_time) + " seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # print ("Total Travel Time is " + "{:,}".format(total_travel_time) + " seconds")

    # Calculate days, hours, minutes & seconds
    travel_days = math.floor(total_travel_time/(24*60*60))
    travel_hours = ( total_travel_time/(60*60) ) % 24
    travel_minutes = ( total_travel_time/60 ) % 60
    travel_seconds = total_travel_time % 60

    print ("Total Travel Time is " + "{:,.0f}".format(travel_days) + " days, "
          + "{:.0f}".format(travel_hours) + " hours, "
          + "{:.0f}".format(travel_minutes) + " minutes and "
          + "{:.0f}".format(travel_seconds) + " seconds")

    # TO DO: display mean travel time
    mean_travel_time = int(round(df['Trip Duration'].mean()))

    travel_minutes = math.floor(mean_travel_time/60)
    travel_seconds = mean_travel_time % 60

    print ("Mean Travel Time is " + "{:,.0f}".format(travel_minutes) + " minutes and "
          + "{:.0f}".format(travel_seconds) + " seconds")

    print("\nThis took " + "{:.4f}".format(time.time() - start_time) + " seconds.")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:")
    user_type_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_type_counts):
        print("   {}: {:,.0f}".format(user_type_counts.index[index], user_count))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nCounts of gender:")
        gender_counts = df['Gender'].value_counts()
        for index, gender_count in enumerate(gender_counts):
            print("   {}: {:,.0f}".format(gender_counts.index[index], gender_count))
    else:
        print('\nNo data available for gender.')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nEarliest year of birth:  {:.0f}".format(df['Birth Year'].min()))
        print("Most recent year of birth:  {:.0f}".format(df['Birth Year'].max()))
        print("Most common year of birth:  {:.0f}".format(df['Birth Year'].mode()[0]))
    else:
        print('\nNo data available for year of birth.\n')


    print("\nThis took " + "{:.4f}".format(time.time() - start_time) + " seconds.")
    print('-'*40)



def view_data(df):
    """Prints rows of data."""

    # Drop columns that are not in the original data
    df = df.drop(columns=['month','day','hour'])

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data.lower() == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to see 5 more rows of data continue? Enter yes or no\n ").lower()
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #  Added this view_data function by Adam, to keep code organized.
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
