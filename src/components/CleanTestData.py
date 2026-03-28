import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.DataClean import clean_data


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'E-commerce_test.csv')
    df = clean_data(file_path)
    save_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned_test.csv')
    df.to_csv(save_file_path, index=False)