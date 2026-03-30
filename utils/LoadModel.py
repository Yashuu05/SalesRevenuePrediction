import joblib

def load_model(file_path):
    """
    This function returns saved model weigths.
    """
    try:
        model = joblib.load(filename=file_path)
        print("model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error: {e}")