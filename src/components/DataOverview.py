import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.load_data import read_data
from utils.DataExplore import data_overview


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'E-commerce_train.csv')
    data_overview(file_path)