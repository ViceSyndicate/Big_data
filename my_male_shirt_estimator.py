# this script guesses the shirt size of males using my own K_nearestneighbours algorithm
import main as mainfuncs
import models.data
import math


def calculate_neighbours(df, my_weight, my_length):

    #create a list of everyones weight & length
    people = []
    df['Size'] = ''
    for row in df.itertuples():
        height = row[1]
        weight = row[2]
        person = models.data.Male_Shirt(weight, height)
        people.append(person)

    #set everyones shirt size
    everyones_size = []
    for person in people:
        everyones_size.append(person.size)
    df['Size'] = everyones_size

    deltas = []
    for person in people:
        height_diff = 0.0
        weight_diff = 0.0

        # if checks to make sure we always get positive values
        if person.height > my_length:
            height_diff = person.height - my_length
        else:
            height_diff = my_length - person.height

        if person.weight > my_weight:
            weight_diff = person.weight - my_length
        else:
            weight_diff = my_weight - person.weight

        height_diff = height_diff * height_diff
        weight_diff = weight_diff * weight_diff

        delta = height_diff + weight_diff
        delta = math.sqrt(delta)
        deltas.append(delta)

    df['deltapoint'] = deltas
    df = df.sort_values(by='deltapoint')
    return df


def main():
    df = mainfuncs.get_df()
    df = mainfuncs.set_sizes_and_deltas(df)

    my_weight = input('Enter weight in Kg: ')
    my_length = input('Enter length in Cm: ')
    k = input('How many do you want to compare with?: ')

    df = calculate_neighbours(df, float(my_weight), float(my_length))
    get_k_neighbours(df, k)


def get_k_neighbours(df, k):
    neighbors = df.head(int(k))
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
    print('Reccomended Size: ' + most_common_size)


if __name__ == '__main__':
    main()
