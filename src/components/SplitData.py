import os
import sys
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.DataSplit import split

if __name__ == "__main__":
    # file path
    train = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'final_train.csv')

    # split dataset
    X_train, X_test, y_train, y_test = split(file_path=train)
    
    # saving file path
    X_train_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'X_train.csv')
    X_test_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'X_test.csv')
    y_train_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'y_train.csv')
    y_test_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'y_test.csv')
    
    # save datasets
    X_train.to_csv(X_train_path, index=False)
    X_test.to_csv(X_test_path, index=False)
    y_train.to_csv(y_train_path, index=False)
    y_test.to_csv(y_test_path, index=False)

    print("all the files are saved.")
