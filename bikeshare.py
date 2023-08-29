import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input ("\n Would you like to see data for Chicago, New York City or Washington?\n").lower()
        if city.lower() not in ('chicago','new york city','washington'):
            print ("Sorry, Information is incorrect. Please try again")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ("\n Would you like to see data for January, February, March, April, May, June or all if you do not have any preference?\n").lower()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print ("Sorry, Information is incorrect. Please try again")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("\n Would you like to see data for  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all if you do not have any preference?\n").lower()
        if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print ("Sorry, Information is incorrect. Please try again")
        else:
            break
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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month =df['month'].mode()[0]
    print ("The most common month:", popular_month)

    # TO DO: display the most common day of week
    popular_day =df['day_of_week'].mode()[0]
    print ("The most common day of week:", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour =df['hour'].mode()[0]
    print ("The most common start hour:",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print ("The most commonly used start station: ",start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print ("The most commonly used end station: ",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station'])
    most_freq_trip_count = combination_station['Trip Duration'].count().max()
    most_freq_trip = combination_station['Trip Duration'].count().idxmax()

    print('Frequent trip: {}, {}'.format(most_freq_trip[0], most_freq_trip[1]))
    print('{0:30}{1} trips'.format(' ', most_freq_trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user type:",user_types)


    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print("Counts of gender:",gender_type)
    except KeyError:
        print("Gender is no data valid this month")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("Earliest Year is no data valid this month")
    #TO DO: Display most recent year of birth    
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost recent Year:', most_recent_year)
    except KeyError:
        print("Most recent Year is no data valid this month")
    #TO DO: Display most common year of birth    
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost common Year:', most_common_year)
    except KeyError:
        print("Most common Year is no data valid this month")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    valid_data=''
    counter=0
    while valid_data not in ('yes','no','y','n'):
        valid_data = input("Do you want to see 5 rows of data? \n Type: Yes(Y) or No(N)\n").lower()
        if valid_data =='yes' or valid_data =='y':
            print(df.head())
        elif valid_data not in ('yes','no','y','n'):
            print("\nSorry. I don't understand your input. Please try again")
   
    while valid_data =='yes' or valid_data=='y':
        counter +=5
        valid_data = input(" Do you want to see the next 5 rows of data? \n Type: Yes(Y) or No(N) \n").lower()
        if valid_data == "yes" or valid_data=='y':
             print(df[counter:counter + 5])
        elif valid_data != "yes" or valid_data !='y':
             break
print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes (y) or no (n).\n')
        if restart.lower() != 'yes' or restart.lower() !='y':
            break


if __name__ == "__main__":
	main()
