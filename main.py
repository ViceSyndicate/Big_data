import pandas as pd

def main():
    weight = extract_weight()


def extract_weight():
    male_df = pd.read_csv('C:\School\BigData\Big_Data\male.csv')
    trimmed_male_data = male_df[['weightkg']]

    weight_list = []

    for row in trimmed_male_data.itertuples():
        weight_list.append(round(row[1]*0.1, 3))

    return weight_list


if __name__ == '__main__':
    main()
