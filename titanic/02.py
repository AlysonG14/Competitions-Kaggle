import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv('titanic/gender_submission.csv')
df.tail()

df = df.drop_duplicates()

df.isnull().sum()

df['Survived'] = df['Survived'].astype(bool)

df['Survived'] = df['Survived'].replace({'True': 'Yes',
                                         'False': 'No'})

df.head(20)
df.info()
df.columns

Passengers = []

def search_passengers():
    for i in range(3):
        input_passenger = int(input("Enter the number's {} passenger".format(i + 1)))
        Passengers.append(input_passenger)
        print(Passengers)


    print(f"Passenger's added: {Passengers}")    

    try:
        print(df.loc[Passengers])
        only_true = df[(df['Survived'] == True)]
        only_false = df[(df['Survived'] == False)]
        print('SURVIVED: {}'.format(only_true))
        print('-------------------------------------------')
        print('NOT SURVIVED: ',only_false)
    except KeyError:
        print("These number's {} not found!".format(Passengers))

search_passengers()   

# FILTERING

# SURVIVED

survived = df[df['Survived'] == True]
#survived.head()
print(survived.to_string())

# NOT SURVIVED

not_survived = df[df['Survived'] == False]
#not_survived.head()
print(not_survived.to_string())

# start selection to GET number's 900 to 1000

number = df.loc[8:108]
print(number.to_string())