
import pandas as pd
from datetime import datetime
df = pd.read_csv('chicago.csv')


def user_d():
    valid = ['yes', "no"]
    i = 0
    while i < df.count():
        x = input("yes or no")
        while x in valid:
            if x == 'yes':
                print(df.iloc[i:i+5])
                i += 5
                x = input("yes or no")
            elif x == "no":
                break
            elif x not in valid:
                print("invalid input")
                x = input("yes or no")
    else:
        print("data finished")
        return df


user_d(df)
