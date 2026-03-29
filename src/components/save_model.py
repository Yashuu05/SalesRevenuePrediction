import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.components.train import model_architecture
import joblib

# get model pipeline
model_list = model_architecture()
xgb_model = model_list[-1]
# saving file path
save_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'xgb.pkl')
# save the model
try:
    joblib.dump(value=xgb_model, filename=save_file_path)
    print("Model saved scuccessfully")
except Exception as e:
    print(f"Error: {e}")