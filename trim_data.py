import pandas as pd


def trim_data():
    male_df = pd.read_csv('C:/School/BigData/Big_Data/male.csv')
    male_trimmed_data = male_df[
        ['stature', 'weightkg', 'chestbreadth', 'waistbreadth', 'hipbreadth', 'waistcircumference', 'crotchheight',
         'footlength', 'Ethnicity']]

    female_df = pd.read_csv("C:/School/BigData/Big_Data/female.csv")
    female_trimmed_data = female_df[
        ['stature', 'weightkg', 'chestbreadth', 'waistbreadth', 'hipbreadth', 'waistcircumference', 'crotchheight',
         'footlength', 'Ethnicity']]

    male_trimmed_data.to_csv('clean_male')
    female_trimmed_data.to_csv('clean_female')
