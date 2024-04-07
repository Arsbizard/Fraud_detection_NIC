import pandas as pd


def explore_dataset(df):
    for col, values in df.items():
        num_uniques = values.nunique()
        print(f'{col}: {num_uniques} unique values')
        print(values.unique())
        print('\n')


dataset_df = pd.read_csv('train_identity.csv')
explore_dataset(dataset_df)
