import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def generate_drift_report():
  # Reference data (training time)
  reference_df = pd.read_csv("data/processed/hr_attrition_fe.csv")
  # Simulated current data (new batch)
  current_df = reference_df.sample( frac=0.8,random_state=42).copy()
  # Create drift report
  report = Report( metric=[DataDriftPreset()])
  report.run( refernce_data=reference_df,current_data=current_df)
  # Save report
  report.save_html("monitoring/reports/data_drift_report.html")
  print("Drift report generated successfully.")

if __name__ == "__main__":
  generate_drift_report()
 
  
