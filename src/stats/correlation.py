# This file takes input of 2 .csv files in the 
# format of: 
# | Heart Rate (BPM) | Timestamp (YYYY:MM:DD:HH:MM:SS) |
# 
# It then run correlation statistics on the 2 files. 

# This is the wrapper function that will be called 
# from the main program. 
def get_correlation(data1, data2): 
    data1, data2 = check_alignment(data1, data2)

# check_alignment makes sure that the timestamps of the 
# 2 datasets have at least some overlap. 
def check_alignment(data1, data2): 
    if False: 
        return None, None
    else:
        data1, data2 = trim_timestamps(data1, data2)
        return data1, data2
    
# trim_timestamps removes any data from each set that 
# does not correspond to data from the other set. 
def trim_timestamps(data1, data2): 
    return data1, data2