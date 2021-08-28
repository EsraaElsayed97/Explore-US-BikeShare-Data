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
    
    city_dict={'c':"chicago",'n':"new york city",'w':"washington"} #store cites with thier keys in dictionary.
    in_city_keys=['c','n','w'] #the domain of the cites'keys.
    
    # get user input for city (chicago, new york city, washington).  
    in_city=input('To view the available bikeshare data, kindly type:\n The letter (c) for\
    Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n  ').lower()
    
    while in_city not in in_city_keys:#Use a while loop to handle invalid inputs
        
        print('That\'s invalid input.') # tell the user that the input is not right.
        
         # Ask again with the same above code
        in_city=input('To view the available bikeshare data, kindly type:\n The letter (c) for\
    Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n  ').lower()
    #we define city as glabal to be able to check if it has (gender and birth year) or not
    global city 
    city=city_dict[in_city] #the city we will use in filter.
    
    ##
    month_dict={'1':"january",'2':"february",'3':"march",'4':"april",'5':"may",'6':"june",'0':"all"} #store months with their keys in dictionary.
    in_month_keys=['0','1','2','3','4','5','6'] #the domain of the months'keys.

    # get user input for month (all, january, february, ... , june)
    in_month=input('\n\nTo filter {}\'s data by a particular month, please type the month number or (0) for not filtering by month\
    :\n-The number (1) for January\n-The number (2) for February\n-The number (3) for March\n-The number (4) for April\n\
-The number (5) for May\n-The number (6) for June\n-The number (0) for All\n\n:'.format(city.title()))
    
    while in_month not in in_month_keys:#Use a while loop to handle invalid inputs
        
        print('That\'s invalid input.') # tell the user that the input is not right.
        
         # Ask again with the same above code
        in_month=input('\n\nTo filter {}\'s data by a particular month, please type the month number or (0) for not filtering by month\
    :\n-The number (1) for January\n-The number (2) for February\n-The number (3) for March\n-The number (4) for April\n\
-The number (5) for May\n-The number (6) for June\n-The number (0) for All\n\n:'.format(city.title()))
        
    month=month_dict[in_month] #the month we will use in filter.
    
    ##

    day_dict={'1':"monday",'2':"tuesday",'3':"wednesday",'4':"thursday",'5':"friday",'6':"saturday",'7':"sunday",'0':"all"} #store days with their keys in dictionary.
    in_day_keys=['0','1','2','3','4','5','6','7'] #the domain of the days'keys.
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    in_day=input('\n\nTo filter {}\'s data by a particular day, please type the day number or (0) for not filtering by day\
    :\n-The number (1) for monday\n-The number (2) for tuesday\n-The number (3) for wednesday\n-The number (4) for thursday\n\
-The number (5) for friday\n-The number (6) for saturday\n-The number (7) for sunday\n-The number (0) for All\n\n:'.format(city.title()))
    
    while in_day not in in_day_keys:#Use a while loop to handle invalid inputs
        
        print('That\'s invalid input.') # tell the user that the input is not right.
        
         # Ask again with the same above code
        in_day=input('\n\nTo filter {}\'s data by a particular day, please type the day number or (0) for not filtering by day\
    :\n-The number (1) for monday\n-The number (2) for tuesday\n-The number (3) for wednesday\n-The number (4) for thursday\n\
-The number (5) for friday\n-The number (6) for saturday\n-The number (7) for sunday\n-The number (0) for All\n\n:'.format(city.title()))
        
    day=day_dict[in_day] #the month we will use in filter.


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    # extract start hour from the Start Time column to create an hour column
    df['Start hour'] = df['Start Time'].dt.hour

    # display the most common month
    common_month = df['month'].mode()[0]

    print('most common month:', common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('most common day of week:', common_day_of_week)


    # display the most common start hour
    common_start_hour = df['Start hour'].mode()[0]

    print('most common start hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #create trip coulumn for the trip
    df['tirp']=df['Start Station']+"_"+df['End Station']
    

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('most commonly used start station:', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('most commonly used end station:', common_end_station)
    


    # display most frequent combination of start station and end station trip
    common_tirp = df['tirp'].mode()[0]

    print('most frequent combination of start station and end station trip:', common_tirp)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract hour from the End Time column to create an hour column ,we extract minutes and seacond to have more accurat time
    
    df['End hour'] = (df['End Time'].dt.hour)+((df['End Time'].dt.minute)/60)+((df['End Time'].dt.second)/3600)
    
    # extract start hour from the Start Time column to create an hour column
    df['Start hour'] = (df['Start Time'].dt.hour)+((df['Start Time'].dt.minute)/60)+((df['Start Time'].dt.second)/3600)
    
    #create duration coulumn for the trip in minutes
    df['duration']=(df['End hour']-df['Start hour'])*60

    # display total travel time in minutes
    total_travel_time=df['duration'].sum()    
    print('total travel time in minutes:', total_travel_time)


    # display mean travel time
    mean_travel_time=df['duration'].mean()    
    print('mean travel time in minutes:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    city_has=["chicago","new york city"] #the cities that have year of birth and gender

    # Display counts of user types
    
    count_subscriber=(df["User Type"]=="Subscriber").sum()
    count_customer=(df["User Type"]=="Customer").sum()
    
    print('it has {} Subscriber and {} Customer'.format(count_subscriber,count_customer))
    if city in city_has:
        
    
        # Display counts of gender
        count_female=(df["Gender"]=="Female").sum()#the number of female. 
        count_male=(df["Gender"]=="Male").sum()#the number of male.
        print('it has {} female and {} male'.format(count_female,count_male))


        # Display earliest, most recent, and most common year of birth
        earliest=df["Birth Year"].min()#the earliest year
        most_recent=df["Birth Year"].max()# the most recent year
        most_common=df["Birth Year"].mode()[0] # the most common year
        print('the earlies year of birth',earliest)
        print('the most recent year of birth',most_recent)
        print('the most common year of birth',most_common)
    else:
        print('washington does not have year of birth or gender columns')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    
    display_raw =input('May you want to have a look on more raw data? Type yes or no').lower()
    while display_raw == 'yes':
        
        
        
        try:
            
            
            # we will loop to print five rows
            file_name =CITY_DATA[city]
            for chunk in pd.read_csv(file_name, chunksize=5):
                
                print(chunk) 
                # repeating the question
                display_raw =input('May you want to have a look on more raw data? Type yes or no').lower()
                if display_raw != 'yes':
                    
                    print('Thank You')
                    break
                
           
        except KeyboardInterrupt:
            print('Thank you.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
