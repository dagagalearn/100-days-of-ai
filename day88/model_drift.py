import sqlite3
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

conn = sqlite3.connect("mlops_logs.db")

train_df = pd.DataFrame({
    "input_val": [10, 12, 11, 13, 12],
    "prediction": [20, 24, 22, 26, 24]
})
train_df.to_sql("reference", conn, if_exists="replace", index=False)

logs_df = pd.DataFrame({
    "input_val": [45, 52, 48, 60, 55],
    "prediction": [90, 104, 96, 120, 110]
})
logs_df.to_sql("production", conn, if_exists="replace", index=False)

reference = pd.read_sql("SELECT * FROM reference", conn)
current = pd.read_sql("SELECT * FROM production", conn)
conn.close()

drift_report = Report(metrics=[DataDriftPreset()])
drift_report.run(reference_data=reference, current_data=current)

drift_report.save_html("drift_report.html")
