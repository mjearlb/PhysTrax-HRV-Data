# This file takes input of 2 .csv files in the 
# format of: 
# | Heart Rate (BPM) | Timestamp (YYYY:MM:DD:HH:MM:SS) |
# 
# It then run correlation statistics on the 2 files. 

import pandas as pd

# This is the wrapper function that will be called 
# from the main program. 
def get_correlation(file1, file2): 
    # Read the files into pandas dataframes
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Make sure the 2 datasets align
    data1, data2 = check_alignment(df1, df2)
    
    # Data does not align
    if data1 is None and data2 is None: 
        return None

    # Combine the trimmed and aligned data into 1 dataframe 
    combined_df = pd.merge(
        data1, 
        data2, 
        on='Timestamp', 
        how='inner',  # keep only timestamps present in both datasets
        suffixes=('_Apple', '_Bangle')
    )

    # Return the correlation statistics
    corr_matrix = combined_df[['Heart Rate (BPM)_Apple', 'Heart Rate (BPM)_Bangle']].corr()
    print(corr_matrix)

    # Or just get the scalar correlation coefficient:
    corr_value = corr_matrix.loc['Heart Rate (BPM)_Apple', 'Heart Rate (BPM)_Bangle']
    print(f"Correlation coefficient: {corr_value:.4f}")

# check_alignment makes sure that the timestamps of the 
# 2 datasets have at least some overlap. If they don't, 
# they return False. 
def check_alignment(data1, data2): 
    merged = pd.merge(data1, data2, on="Timestamp", how="inner")
    if merged.empty: # No common timestamps found
        print("Error: No overlapping timestamps found between the two datasets.")
        return None, None
    else:
        # Trim the data to only the overlapping points
        data1, data2 = trim_timestamps(data1, data2)
        return data1, data2
    
# trim_timestamps removes any data from each set that 
# does not correspond to data from the other set. 
def trim_timestamps(data1, data2): 
    # Find all overlapping timestamps
    overlapping_timestamps = pd.Series(list(set(data1["Timestamp"]) & set(data2["Timestamp"])))

    # Find the first and last overlapping timestamp
    start = overlapping_timestamps.min()
    end = overlapping_timestamps.max()

    # Remove any data before and any data after
    data1_trimmed = data1[(data1["Timestamp"] >= start) & (data1["Timestamp"] <= end)].copy()
    data2_trimmed = data2[(data2["Timestamp"] >= start) & (data2["Timestamp"] <= end)].copy()

    return data1_trimmed, data2_trimmed
