from src.pipelines.Pipeline import create_pipeline
from sklearn.pipeline import Pipeline
import os

def create_model_pipeline(model):
    df = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed', 'X_train.csv')
    preprocessor = create_pipeline(file_path=df)

    model_pipline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])

    return model_pipline
