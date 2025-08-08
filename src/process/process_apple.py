# This file takes an input of Apple Watch heart rate data 
# in .csv format. 
# 
# It outputs a .csv in a standardized format to allow 
# correlation with PhysTrax data to be calculated. 

import pandas as pd
import os
import numpy as np

def process(file, output_directory): 
    print("Processing Apple data: " + file)

    # Open the input file and read the raw Apple heart rate 
    # data as a pandas dataframe. 
    df = pd.read_csv(file, skiprows=1) # Must skip the first row since that is an extra header row
    
    # Extract the desired data from the input csv file (timestamps & 
    # heart rate only). 
    # 
    # The timestamps require further adjustments before they can be 
    # further processed. Also note that startDate == endDate for Apple 
    # heart rate measurements, so either can be used. 
    heart_rate_bpm = df['value'] # Needs no further adjustments
    timestamp_list = df['startDate'].tolist() 
    timestamps_normalized = pd.to_datetime(arg=timestamp_list, errors="raise", yearfirst=True)

    # Average the data. 
    # 
    # For every minute included in the data, any readings within that minute
    # must be averaged for easy comparison later. 

    # Create a temporary dataframe to store the normalized timestamps & 
    # heart rate data in. 
    temp = pd.DataFrame({
        'timestamp': timestamps_normalized,
        'bpm': heart_rate_bpm
    })

    # Round each timestamp down to the nearest minute
    temp['minute'] = temp['timestamp'].dt.floor('min')

    # Compute average of the BPM data within each minute
    processed_data = temp.groupby('minute')['bpm'].mean().reset_index()

    # Rename the columns
    processed_data.columns = ['Timestamp', 'Heart Rate (BPM)']

    # Save the new processed data to the output directory
    processed_file = os.path.join(output_directory, 'apple.csv')
    processed_data.to_csv(processed_file, index=False)

    return processed_file