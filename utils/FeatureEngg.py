import pandas as pd
from utils.load_data import read_data

def perform_feature_engineering(file_path):

    """
    this function performs feature engineering on the cleaned dataset
    and returns new dataset
    """
    # read the dataset
    df = read_data(file_path)
    # convert `date` column into datetime
    df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
    # extract year, month. day and hour
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    # convert numeical hours into categorical
    def get_time_of_day(hour):
        if 6 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 18:
            return 'afternoon'
        elif 18 <= hour < 24:
            return 'evening'
        else:
            return 'night'
    df['time_of_day'] = df['hour'].apply(get_time_of_day)
    
    # display overview
    time_cols = ['year','month','day', 'hour','time_of_day']
    print("Overview of new columns:\n")
    print(df[time_cols].tail(10))

    # Feature engineering
    df['cost_per_impression'] = df['ad_spend'] / df['impressions']
    df['cost_per_click'] = df['ad_spend'] / (df['impressions'] * df['click_through_rate'])
    df['reach_per_spend'] = df['market_reach'] / df['ad_spend']
    df['value_ratio'] = df['customer_lifetime_value'] / df['price']

    # drop hour column
    df = df.drop(['hour','date'], axis=1)

    # print total columns
    cols = df.shape[1]
    print(f"total columns after feature engineering = {cols}")

    # print information of new dataset
    print("\n",df.info())

    # print null values
    total_null_values = df.isnull().sum().sum()
    print("\ntotal null values = ", total_null_values)

    # return the new dataset
    return df