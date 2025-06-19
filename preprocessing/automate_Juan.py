import pandas as pd
import numpy as np

INPUT_PATH = '..\raw-dataset\DiamondsPrices.csv'
OUTPUT_PATH = "data_clean.csv"

def load_data(path):
    df = pd.read_csv(path)
    return df

def drop_duplikat(df):
    df_clean=df.drop_duplicates()
    return df_clean

def outlier_handling(df, columns):
    df_cleaned=df.copy()
    for col in columns:
        if pd.api.types.is_numeric_dtype(df_cleaned[col]):
            Q1=df_cleaned[col].quantile(0.25)
            Q3=df_cleaned[col].quantile(0.75)
            IQR=Q3-Q1
            lower_bound=Q1- 1.5 * IQR
            upper_bound=Q3 + 1.5 * IQR
            df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & (df_cleaned[col] <= upper_bound)]

    df_cleaned = df_cleaned.reset_index(drop=True)
    return df_cleaned

def encode_clarity(df):
    clarity_encoding={
        "I1" : 0,
        "SI2" : 1,
        "SI1" : 2,
        "VS2" : 3,
        "VS1" : 4,
        "VVS2" : 5,
        "VVS1" : 6,
        "IF" : 7,
    }
    df_encoded=df.copy()
    df_encoded['clarity']=df_encoded['clarity'].replace(clarity_encoding)
    return df_encoded

def encode_color(df):
    color_encoding={
        "D" : 6,
        "E" : 5,
        "F" : 4,
        "G" : 3,
        "H" : 2,
        "I" : 1,
        "J" : 0,
    }
    df_encoded=df.copy()
    df_encoded['color']=df_encoded['color'].replace(color_encoding)
    return df_encoded

def encode_cut(df):
    cut_encoding={
        "Fair" : 0,
        "Good" : 1,
        "Very Good" : 2,
        "Premium" : 3,
        "Ideal" : 4,
    }

    df_encoded=df.copy()
    df_encoded['cut']=df_encoded['cut'].replace(cut_encoding)
    return df_encoded

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    df = load_data(INPUT_PATH)
    df = drop_duplikat(df)
    numeric_columns = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    df = outlier_handling(df, numeric_columns)
    df = encode_clarity(df)
    df = encode_color(df)
    df = encode_cut(df)
    save_data(df, OUTPUT_PATH)

if __name__ == "__main__":
    main()
