import pandas as pd
import math
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import models.data as models
import trim_data

# Predicts Male shirt size with kg & cm using sklearns K_nearesneighbour algorithm


def get_df():
    df = pd.read_csv('C:\School\BigData\Big_Data\male.csv', usecols=['stature', 'weightkg'])
    df.rename(columns={'weightkg': 'Kg', 'stature': 'Cm'}, inplace=True)
    df['Kg'] = df['Kg'].multiply(0.1)
    df['Cm'] = df['Cm'].multiply(0.1)
    return df


def set_sizes_and_deltas(df):
    people = []

    df['Size'] = ''
    for row in df.itertuples():
        height = row[1]
        weight = row[2]
        person = models.Male_Shirt(weight, height)
        people.append(person)

    everyones_size = []
    for person in people:
        everyones_size.append(person.size)

    df['Size'] = everyones_size
    df = calculate_deltas(df, people)
    return df


def calculate_deltas(df, people):

    deltas = []
    for person in people:
        a = person.height * person.height
        b = person.weight * person.weight
        c = a + b
        delta = round(math.sqrt(c), 3)
        deltas.append(delta)

    df['deltapoint'] = deltas
    return df


def calculate_users_shirt(df, cm, kg, k):
    weight_and_length = []

    for row in df.itertuples():
        length = row[1]
        weight = row[2]
        person = models.Male_Shirt(weight, length)
        weight_and_length.append(person)

    kn_classifier = KNeighborsClassifier(n_neighbors=int(k))

    values = []
    sizes = []

    for person in weight_and_length:
        kg_and_cm = [round(person.weight, 3), round(person.height, 3)]
        values.append(kg_and_cm)
        sizes.append(person.size)

    reshaped_measurements = np.array(values).reshape(-1, 2)
    kn_classifier.fit(reshaped_measurements, sizes)

    user_weight = [[cm, kg]]
    prediction_size = kn_classifier.predict(user_weight)

    probability = kn_classifier.predict_proba(user_weight)
    score = kn_classifier.score

    print("Reccomended Size: " + str(prediction_size))


def main():
    #trim_data.trim_data()
    df = get_df()
    df = set_sizes_and_deltas(df)

    kg = input('Enter weight in Kg: ')
    cm = input('Enter length in Cm: ')
    k = input('How many do you want to compare with?: ')

    calculate_users_shirt(df, kg, cm, k)


if __name__ == '__main__':
    main()
