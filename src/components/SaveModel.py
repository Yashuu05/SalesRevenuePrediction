import os
import sys
import pandas as pd
import numpy as np
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.components.train import model_architecture
from utils.load_data import read_data

# get model pipeline
model_list = model_architecture()
xgb_model = model_list[-1]

# load training data
X_train_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed', 'X_train.csv')
y_train_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed', 'y_train.csv')

X_train = read_data(path=X_train_path)
y_train = read_data(path=y_train_path)

# Preprocess training data (replace infs and ravel target)
X_train = X_train.replace([np.inf, -np.inf], np.nan)
y_train = y_train.values.ravel()

# saving file path
save_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'xgb.pkl')

# fit and save the model
try:
    print("Fitting XGBoost model...")
    xgb_model.fit(X_train, y_train)
    joblib.dump(value=xgb_model, filename=save_file_path)
    print("Model saved successfully")
except Exception as e:
    print(f"Error: {e}")