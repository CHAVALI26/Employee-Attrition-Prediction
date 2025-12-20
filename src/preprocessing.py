import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

class DataPreprocessor:
  def __init__(self):
    self.target_column = "Attrition"
    self.numeric_features = ["Age", "MonthlyIncome", "YearAtCompany", "JobSatisaction"]
    self.categorical_features = ["JobRole", "OverTime"]
    self.preprocessor = None
  
  def build_pipeline(self):
    """Create Preprocessing pipeline"""
    numeric_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")),
                                       ("scaler", StandardScaler())
                                      ])
    categorical_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")),
                                           ("scaler", OneHotEncoder(handle_unknown="ignore"))
                                          ])
    self.preprocessor = ColumnTransformer(
    transformers=[("num", numeric_pipeline, self.numeric_features),
    ("cat", categorical_pipeline, self.categorical_features)]
    )

  def preprocess(self, df: pd.Dataframe):
      """Clean and transform data"""
      if self.preprocessor is None:
        self.build_pipeline()
      # Separate feature and target
      X = df.drop(colmns=[self.target_column])
      y = df[self.target_column].map({"Yes": 1, "No": 0})

      # fit & transform features
      X_transformed = self.preprocessor.fit_transform(X)

      # Get Features
      feature_names = ( self.numeric_features +
      list(self.preprocessor.named_transformers_["cat"]
          .named_steps["encoder"]
          .get_feature_names_out(self.categorical_features)
          )
                      )
      #Convert to Dataframe
      X_df = pd.DataFrame(X_transformed.toarray(), columns=feature_names)
      processed_df= X_df.copy()
      processed_df["Attrition"] = y.values
      processed_df.to_csv("data/processed/hr_attrition_processed.csv", index=False)
      return processed_df
