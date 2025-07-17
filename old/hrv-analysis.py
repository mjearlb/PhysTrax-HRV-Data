import neurokit2 as nk
import pandas as pd
import numpy as np

# Simulate PPG data
ppg = nk.ppg_simulate(duration=40, sampling_rate=500, heart_rate=75, random_state=42)

# print(ppg)

ppg_signals, info = nk.ppg_process(ppg, sampling_rate=500)

# ppg_real = nk.ppg_process()

# Read the PPG data from CSV
ppg = pd.read_csv("ppg_sensor_data.csv", header=None)


ppg = nk.ppg_simulate(duration=400, sampling_rate=100, heart_rate=75, random_state=42)
ppg = pd.read_csv("ppg_sensor_data.csv", header=None)
print(ppg)

ppg_cleaned = nk.ppg_clean(ppg, sampling_rate=100)
print(ppg_cleaned)

ppg_df, info = nk.ppg_process(ppg_cleaned, sampling_rate=100)
print(ppg_df)
print(info)

print(nk.hrv(info['PPG_Peaks'], sampling_rate=100))