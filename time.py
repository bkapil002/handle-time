import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
air_quality = pd.read_csv("titanic.csv")

# Rename the 'date.utc' column to 'datetime'
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

# Display the first few rows
print(air_quality.head())

# Convert 'datetime' to datetime type if not already done
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

# Calculate basic statistics
print(air_quality["value"].describe())

# Filter data for Paris
paris_data = air_quality[air_quality["city"] == "Paris"]

# Plot NO2 levels over time for Paris
plt.figure(figsize=(12, 6))
plt.plot(paris_data["datetime"], paris_data["value"])
plt.title("NO2 Levels in Paris Over Time")
plt.xlabel("Datetime")
plt.ylabel("NO2 Concentration (µg/m³)")
plt.xticks(rotation=45)
plt.show()
