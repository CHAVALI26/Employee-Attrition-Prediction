import pandas as pd

class DataValidationError(Exception)):
  pass

class DataValidator:
  def __init__(self):
    self.expected_schema={
      "Age": "int",
      "MonthlyIncome": "int",
      "JobRole": "object",
      "YearsAtCompany": "int",
      "OverTime": "object",
      "JobSatisfaction": "int",
      "Attrition": "object"
    }
    self.target_column = "Attrition"
    self.allowed_target_values = ["Yes","No"]
  def validate_schema(self, df: pd.DataFrame):
    """Check if required columns exist"""
    missing_columns = set(self.expected_schema.keys()) - self(df.columns)
    if missing_columns:
      raise DataValidationError{
      f"Missing reuired columns: {missing_columns}"
      }
  def validate_dtypes(self, df: pd.DataFrame):
    """Check data types"""
    for col,expected_type in self.expected_schema.items():
      actual_type = df[col].dtype
      if expected_type == "int" and not pd.api.types.is_integer_dtype(actual_type):
        raise DataValidationError(
          f"Column {col} expected int but got {actual_type}"
        )
        if expected_type == "object" and not pd.api.types.is_object_dtype(actual_type):
          raise DataValidationError(
          f"Column {col} expected object but got {actual_type}"
        )
  def validate_missing_values(self, df: pd.Dataframe):
    """Check for excessive missing values"""
    missing_ratio = df.isnull().mean()
    high_missing = missing_ratio[missing_ratio > 0.3]
    if not high_missing.empty:
      raise DataValidationError(
        f"Columns with >30% missing values: {high_missing.index.tolist()}"
      )
  def validate_value_ranges(self, df: pd.DataFrame):
    """Check numeric ranges"""
    if (df["Age"] <= 0).any() or (df["Age"] > 100).any():
      raise DataValidationError("Invalid values detected in Age")
    if (df["MonthlyIncome"] <= 0).any():
      raise DataValidationError("MonthlyIncome must be positive")
    if (df["YearsAtCompany"] < 0).any():
      raise DataValidationError("YearsAtCompany cannot be negative")
  def validate_target(self, df: pd.DataFrame):
    """Check target column validity"""
    if self.target_column not in df.columns:
      raise DataValidationError("Target column missing")
    invalid_targets = set(df[self.target_column].unique()) - set(self.allowed_target_values)
    if invalid_targets:
      raise DataValidationError(
        f"Invalid target values found: {invalid_targets}"
      )
  def run_all_checks(self, df: pd.DataFrame):
    """Run all validation checks"""
    self.validate_schema(df)
    self.validate_dtypes(df)
    self.validate_missing_values(df)
    self.validate_value_ranges(df)
    self.validate_target(df)
    print("Data validation process successfully completed")
          
    
