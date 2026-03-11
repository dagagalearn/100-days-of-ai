import pandas as pd
# Weekly temperature analysis.

temps = [24,23,20,26,30,24,21,22,23,28,20,21]
days = ["Mon1","Tue1","Wed1","Thu1","Fri1","Sat1","Sun1","Mon2","Tue2","Wed2","Thu2","Fri2"]

temp_series = pd.Series(temps, index=days)

# days when the temperature is greater than 25 
print("Hot days: T>25")
print(temp_series[temp_series > 25])

print("Cold days: T<=25")
print(temp_series[temp_series <= 25])

print("Weather data analysis:")
print("Average:", temp_series.mean())
print("Maximum:", temp_series.max())
print("Minimum:", temp_series.min())
print("Standard deviation:", round(temp_series.std(), 2))

print("Difference from previous day:")
print(temp_series.diff())
