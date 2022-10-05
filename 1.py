import calendar as cal
m = cal.month_name[1:]+['All']
print(m)
d = cal.day_name[:]+['All']
print(d)
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!'.title())
    city = input(
        "Choose a city you wanna ask about (chicago, new york city, washington)".title()).lower()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print('please enter a valid city name'.title())
        city = input(
            "Choose a city you wanna ask about (chicago, new york city, washington)\n".title()).lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "please enter a month name (all, january, february, ... , june)\n".title()).title().strip()
        if month not in d_month:
            print("invalid input for months".title())
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "please choose a day (all, monday, tuesday, ... sunday)\n".title()).title().strip()
        if day not in d_day:
            print("invalid input for days".title())
        else:
            break

    print('-'*40)
    return city, month, day
get_filters()

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
    df=pd.read_csv(CITY_DATA[city])
    return df
load_data()