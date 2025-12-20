import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


class DataPreprocessor:
    def __init__(self):
        self.target_column = "Attrition"

        self.numeric_features = [
            "Age",
            "MonthlyIncome",
            "YearsAtCompany",
            "JobSatisfaction"
        ]

        self.categorical_features = [
            "JobRole",
            "OverTime"
        ]

        self.preprocessor = None

    def build_pipeline(self):
        numeric_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        categorical_pipeline = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])

        self.preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_pipeline, self.numeric_features),
                ("cat", categorical_pipeline, self.categorical_features)
            ]
        )

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.preprocessor is None:
            self.build_pipeline()

        # Separate features and target
        X = df.drop(columns=[self.target_column])
        y = df[self.target_column].map({"Yes": 1, "No": 0})

        # Fit & transform
        X_transformed = self.preprocessor.fit_transform(X)

        # Feature names
        cat_feature_names = (
            self.preprocessor
            .named_transformers_["cat"]
            .named_steps["onehot"]
            .get_feature_names_out(self.categorical_features)
        )

        feature_names = self.numeric_features + list(cat_feature_names)

        processed_df = pd.DataFrame(X_transformed, columns=feature_names)
        processed_df[self.target_column] = y.values
        
        processed_df.to_csv("data/processed/hr_attrition_processed.csv", index=False)
        return processed_df


