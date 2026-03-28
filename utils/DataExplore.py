import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.load_data import read_data

def data_overview(path):
    """
    This function prints overview of dataset such 
    as information, shape, statistics 
    """
    try:
        print("reading data...")
        df = read_data(path)
        print("\nfirst few rows")
        print(df.head())
        print("\n Shape = ", df.shape)
        print("\n Info: \n", df.info())
        print("\n Statistics : \n", df.describe())
        print("\n Null values each feature: \n", df.isnull().sum())
        print("\n total null values = ", df.isnull().sum().sum())
        print("\n total duplicated values = ", df.duplicated().sum())

    except Exception as e:
        print(f"error: {e}")
     
if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'E-commerce_train.csv')
    data_overview(file_path)