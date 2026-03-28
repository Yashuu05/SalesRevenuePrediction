import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.load_data import read_data

# read dataset
def clean_data(file_path):
    try:
        # load dataset
        df = read_data(path=file_path)
        
        # print columns 
        print("columns of data = \n", df.columns)
        # drop dates and id from train data
        print("dropping date and id from data")
        df = df.drop(['id','date'], axis=1)
        print("after dropping columns from data: \n", df.columns)

        # create columns of categorical and numerical data
        num_cols = []
        cat_cols = []
        for cols in df.columns:
            if df[cols].dtypes == "object":
                cat_cols.append(cols)
            else:
                num_cols.append(cols) 
        print("categorical cols = \n", cat_cols)
        print("numerical cols = \n", num_cols)
        print("\nnumber of categorical cols = ", len(cat_cols))
        print("\nnumber of numerical cols =", len(num_cols))

        region_corrections= {
            "Nort":"North",
            "north":"North",
            "NORTH":"North",
            "Norht":"North",
            "north ":"North"
        }
        df['region'] = df['region'].replace(region_corrections)
        print("after correct replacement: \n", df['region'].unique())

        channel_corrections= {
            'Social_Media':'Social Media',
            'Socail Media':'Social Media',
            'social Media':'Social Media',
            'SocialMedia':'Social Media',
            'social media':'Social Media'
        }
        df['channel'] = df['channel'].replace(channel_corrections)
        print("after correct replacement= \n", df['channel'].unique())

        # get null columns
        null_cols = []
        for cols in df.columns:
            if df[cols].isnull().sum() > 0:
                null_cols.append(cols)
        print("\nnull columns = ", null_cols)

        # fill null values with median values
        for cols in null_cols:
            df[cols] = df[cols].fillna(df[cols].median())
        print("after filling null values = \n", df.isnull().sum())

        

    except Exception as e:
        print(f"Error: {e}")
