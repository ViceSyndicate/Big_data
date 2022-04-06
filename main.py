import pandas as pd
import math
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class Size:
    xs = "XSMALL"
    s = "SMALL"
    m = "MEDIUM"
    l = "LARGE"
    xl = "XLARGE"
    xxl = "XXLARGE"
    xxxl = "XXXLARGE"


class Person:
    def __init__(self, weight, height, *args):
        self.weight = weight
        self.height = height

        #self.chestbreadth = args.chestbreadth
        #self.waistbreadth = args.waistbreadth
        #self.hipbreadth = args.hipbreadth

        self.size = Size.xs if (height <= 169) & (weight <= 55) else Size.s if (height <= 178) & (weight <= 65) else Size.m if (height <= 182) & (weight <= 75) else Size.l if (height <= 186) & (weight <= 85) else Size.xl if (height <= 190) & (weight <= 90) else Size.xxl if (height <= 194) & (weight <= 95) else Size.xxxl


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
        person = Person(weight, height)
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


def calculate_users_shirt(df, cm, kg):
    weight_and_length = []

    for row in df.itertuples():
        length = row[1]
        weight = row[2]
        person = Person(weight, length)
        weight_and_length.append(person)

    kn_classifier = KNeighborsClassifier(n_neighbors=3)

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

    print("I think :" + str(prediction_size) + " Would fit you.")


def main():
    df = get_df()
    df = set_sizes_and_deltas(df)

    kg = input('Enter weight in Kg: ')
    cm = input('Enter length in Cm: ')

    calculate_users_shirt(df, kg, cm)


if __name__ == '__main__':
    main()
