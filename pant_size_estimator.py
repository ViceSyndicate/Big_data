import pandas as pd
import models.data as models

def get_df(gender):
    if gender == 'm':
        gender = 'male'
    if gender == 'f':
        gender = 'female'

    df = pd.read_csv(f"C:/School/BigData/Big_Data/{gender}.csv")
    df = df[['buttockcircumference', 'waistcircumference']]
    df['buttockcircumference'] = df['buttockcircumference'].multiply(0.1)
    df['waistcircumference'] = df['waistcircumference'].multiply(0.1)
    df.rename(columns={'buttockcircumference': 'hipcircumference', 'waistcircumference': 'waistcircumference'},
              inplace=True)
    return df


def set_sizes_and_distances(df, user_waist, user_hip):
    people = []

    for row in df.itertuples():
        hipcircumference = row[1]
        waistcircumference = row[2]
        person = models.Female_Pants(hipcircumference, waistcircumference)
        people.append(person)

    everyones_size = []
    for person in people:
        everyones_size.append(person.size)

    df['Size'] = everyones_size

    deltas = []
    for person in people:
        waist_diff = 0.0
        hip_diff = 0.0

        # if checks to make sure we always get positive values
        if person.waistbreadth > user_waist:
            waist_diff = person.waistbreadth - user_waist
        else:
            waist_diff = user_waist - person.waistbreadth

        if person.hipwidth > user_hip:
            hip_diff = person.hipwidth - user_hip
        else:
            hip_diff = user_hip - person.hipwidth

        waist_diff = waist_diff * waist_diff
        hip_diff = hip_diff * hip_diff

        delta = waist_diff + hip_diff
        # delta = math.sqrt(delta)
        deltas.append(delta)

    df['deltapoint'] = deltas
    df = df.sort_values(by='deltapoint')
    return df


def get_k_nearest_neighbour(df, k):
    neighbors = df.head(k)
    neighbour_list = []

    for row in neighbors.itertuples():
        neighbour = []
        size = row[3]
        distance = row[4]
        neighbour.append(size)
        neighbour.append(distance)
        neighbour_list.append(neighbour)

    list_of_sizes = []
    for size in neighbour_list:
        list_of_sizes.append(size[0])

    most_common_size = max(set(list_of_sizes), key=list_of_sizes.count)
    print('Recommended  Size: ' + most_common_size)


def main():
    print('This script tries to estimate your pant size.')
    user_hip = input('Enter your hip circumference')
    user_waist = input('Enter your waist circumference')
    user_hip = float(user_hip)
    user_waist = float(user_waist)

    gender = input('M/F?')

    df = get_df(gender)
    df = set_sizes_and_distances(df, user_waist, user_hip)
    k = input('how many do you want to compare with?')
    k = int(k)
    get_k_nearest_neighbour(df, k)


if __name__ == '__main__':
    main()
