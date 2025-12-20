import pandas as pd
import numpy as np

class FeatureEngineer:
  def __init__(self):
    pass

  def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Income normalized by tenure
    df["IncomePerYear"] = df["MonthlyIncome"] / (df["YearsAtCompany"] + 1)

    # 2. Promotion rate (avoid division by zero)
    if "YearsSinceLastPromotion" in df.columns:
      df["PromotionRate"] = ( df["YearsAtCompany"] / (df["YearsSinceLastPromotion"]+1))
    
    # 3. Tenure buckets
    df["TenreBucket"] = pd.cut( df["YearsAtCompany"], bins=[-1,2,5,10,np.inf], labels=["0-2", "3-5", "6-10", "10+"])
    # 4.Satisfaction composite score
    satisfaction_cols = [ col for col in df.columns
                         if col in ["JobSatisfaction", "EnvironmentSatisfaction", "WorkLifeBalance"]]
    
    if satisfaction_cols:
      df["SatisfactionScore"] = df[satisfaction_cols].mean(axis=1)
    
    #5. Binary overtime flag
    df["OverTimeFlag"] = df["OverTime"].map({"Yes": 1,"No": 0})
    df.to_csv("data/featured/hr_attrition_featured.csv", index=False)
    return df