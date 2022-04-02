
def main():
    pass

def extract_data():
    unclean = open('male.csv', 'r')


    cleaned = open(f'male_cleaned_data.json', 'w')

    lines = unclean.readlines()
    for line in lines:
        cleaned.writelines()



if __name__ == '__main__':
    main()
