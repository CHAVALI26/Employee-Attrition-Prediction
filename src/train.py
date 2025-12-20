import pandas as pd
from src.data_validation import DataValidator

# from src.preprocessing import DataPreprocessor
# from src.feature_engineering import FeatureEngineer

def main():
  raw_path = "data/raw/hr_attrition_raw.csv"
  df = pd.read_csv(raw_path)
  
  """Validation"""
  validator = DataValidator()
  validator.run_all_checks(df)
  validated_path = "data/validated/hr_attrition_validated.csv"
  df.to_csv(validated_path, index=False)
  print("validated data saved successfully")

  """Preprocessing"""
  """
  df= pd.read_csv("data/validated/hr_attrition_validated.csv")
  preprocessor = DataPreprocessor()
  processed_df = preprocessor.preprocess(df)
  processed_df.to_csv("data/processed/hr_attrition_processed.csv", index=False)
  """

  """Feature Engineering"""
  """
  df = pd.read_csv("data/validated/hr_attrition_validated.csv")
  fe = FeatureEngineer()
  df_fe = fe.engineer_features(df)
  df_fe.to_csv("data/featured/hr_attrition_featured.csv", index=False)
  print("Feature engineering completed") 
  """
 
if __name__ == "__main__":
  main()
  
