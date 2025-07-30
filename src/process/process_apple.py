# This file takes an input of Apple Watch heart rate data 
# in .csv format. 
# 
# It outputs a .csv in a standardized format to allow 
# correlation with PhysTrax data to be calculated. 

def process(file, output_directory): 
    print("Processing Apple data: " + file)

    # Save the new files to the output directory
    new_file = file # TEMPORARY

    return new_file