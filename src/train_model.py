import pandas as pd
import joblib
import mlflow
import mlflow.xgboost

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

from src.feature_engineering import FeatureEngineer
from src.preprocessing import DataPreprocessor

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def train_xgboost():
    #1.load validated data
    df = load_data("data/validated/hr_attrition_validated.csv")

    #2.Feature engineering
    fe = FeatureEngineer()
    df = fe.engineer_features(df)
    
    #3.Preprocessing
    preprocessor = DataPreprocessor()
    processed_df = preprocessor.preprocess(df)
    
    X = processed_df.drop(columns=["Attrition"])
    y = processed_df["Attrition"]
    
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42 )
    
    # Model params
    params = {
    "n_estimators": 300,
    "max_depth": 6,
    "learning_rate": 0.05,
    "eval_metric": "auc",
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "random_state": 42,
    }

    # start MLflow run
    with mlflow.start_run(run_name="xgboost_attrition"):
        
        # Log parameters
        mlflow.log_params(params)
        
        model = XGBClassifier(**params)
        model.fit(X_train, y_train)

        # Evaluate
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        #Log metric
        mlflow.log_metric("roc_auc", roc_auc)

        print(f"ROC-AUC Score: {roc_auc:.4f}")

        # Save Model
        joblib.dump(model, "models/xgboost_attrition_model.pkl")
        joblib.dump(preprocessor, "models/preprocessor.pkl")

        # log artifacts to MLflow
        mlflow.log_artifact("models/xgboost_attrition_model.pkl")
        mlflow.log_artifact("models/preprocessor.pkl")

        print(" Model and preprocessor logged to MLflow.")

if __name__ == "__main__":
    train_xgboost()

