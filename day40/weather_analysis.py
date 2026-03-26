#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

weather_data = pd.read_csv('file:///C:/users/pc/downloads/nyc_temperature.csv')

# Preview
print(weather_data.head())
print(weather_data.shape)

print(weather_data.info())
print(weather_data.describe())

# Missing values
print(weather_data.isnull().sum())

# Convert date column
weather_data['date'] = pd.to_datetime(weather_data['date'])

# Extract time features
weather_data['year'] = weather_data['date'].dt.year
weather_data['month'] = weather_data['date'].dt.month

print("Max Temp:", weather_data['tavg'].max())
print("Min Temp:", weather_data['tavg'].min())
print("Mean Temp:", weather_data['tavg'].mean())
print("Std Dev:", weather_data['tavg'].std())


plt.figure(figsize=(10,5))
plt.plot(weather_data['date'], weather_data['tavg'])
plt.title("Temperature Trend Over Time (NYC)")
plt.xlabel("Date")
plt.ylabel("Average Temperature")
plt.xticks(rotation=45)
plt.show()


monthly_avg = weather_data.groupby('month')['tavg'].mean()

plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar')
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.show()


hottest_day = weather_data.loc[weather_data['tavg'].idxmax()]
coldest_day = weather_data.loc[weather_data['tavg'].idxmin()]

print("Hottest Day:\n", hottest_day)
print("\nColdest Day:\n", coldest_day)


plt.figure(figsize=(8,5))
sns.histplot(weather_data['tavg'], kde=True)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.show()


corr = weather_data.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

monthly_std = weather_data.groupby('month')['tavg'].std()

plt.figure(figsize=(8,5))
monthly_std.plot(kind='bar')
plt.title("Monthly Temperature Variability (Std Dev)")
plt.xlabel("Month")
plt.ylabel("Std Dev")
plt.show()

