import pandas as pd
from datetime import datetime
df = pd.read_csv('chicago.csv')

i = 0


def ask():
    var = ['yes', 'no']
    x = str(input("you wanna see some rows? ==>"))
    if x not in var:
        print("invalid input")
        return ask()
    else:
        if x in var:
            print(f'thank you')
            if x == "yes":
                print('you want some data')
                global i
                print(df.iloc[i:i+5])
                i += 5
                return ask()


def data():
    print(df.iloc[i:i+5])


def show_d(x):
    x
    if x == "yes":
        data()
        x
        if x == "no":
            print('thank you')
        elif x == "yes":
            i += 5
            return show_d()


ask()
