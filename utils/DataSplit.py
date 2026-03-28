from sklearn.model_selection import train_test_split
import pandas as pd
from utils.load_data import read_data

def split(file_path):

    """
    This function splits train dataset into features and target variables.
    """
    # read dataset
    train = read_data(path=file_path)
    # prepare feature and labels
    y = train['sales_revenue']
    X = train.drop('sales_revenue', axis=1)
    # split data
    print("splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
    print("split complete.")
    print("shape of datasets: \n")
    print(f"X_train: {X_train.shape}\ny_train: {y_train.shape}\nX_test: {X_test.shape}\ny_test: {y_test.shape}")

    return X_train, X_test, y_train, y_test






