# This file takes an input of PhysTrack heart rate data 
# in .csv format. 
# 
# It outputs a .csv in a standardized format to allow 
# correlation with Apple Watch data to be calculated. 

import pandas as pd
import os
import numpy as np

def process(file, output_directory, offset=0): 
    print("Processing PhysTrax data: " + file)

    # Open the input file and read the raw Apple heart rate 
    # data as a pandas dataframe. 
    df = pd.read_csv(file) # Don't skip first row for PhysTrax, that contains our column data
    
    # Extract the desired data from the input csv file (timestamps & 
    # heart rate only). 
    # 
    # The timestamps require further adjustments before they can be 
    # further processed. 
    heart_rate_bpm = df['Heart Rate(bpm)'] # Needs no further adjustments
    timestamp_list = df['Timestamp'].tolist() 
    timestamps_normalized = pd.to_datetime(timestamp_list, format="%b %d %Y %H:%M:%S.%f", errors="raise")

    # Add the offset
    timestamps_normalized = timestamps_normalized + pd.to_timedelta(offset, unit='h')

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
    processed_file = os.path.join(output_directory, 'bangle.csv')
    processed_data.to_csv(processed_file, index=False)

    return processed_file