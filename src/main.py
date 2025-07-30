# This is the main program. Run this in order to find
# the correlation between Apple Watch and PhysTrax
# heart rate data. 
# 
# It takes an input of 2 .csv files. Format it like so: 
# python3 run_correlation.py -a [apple_data].csv -p [phystrax_data].csv -o [output-name]

import argparse
import process.process_apple as pa
import process.process_bangle as pb
import os.path
import sys

def get_args(): 
    # Add command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apple_data", required=True, 
                        help="The path to the .csv file containing the Apple Watch heart rate & timestamp data.")
    parser.add_argument("-p", "--phystrax_data", required=True, 
                        help="The path to the .csv containing the PhysTrax heart rate & timestamp data. ")
    parser.add_argument("-o", "--output_directory", "--output_folder", required=True,
                        help="The path to the folder which the processed .csv's and correlation figures should be placed.")

    # Parse the command line arguments
    args = parser.parse_args()
    return args

def check(filename): 
    if not os.path.exists(filename): 
        print("Error: file " + filename + " does not exist!")
        sys.exit(1)

def main(): 
    # Parse the args
    arguments = get_args()
    apple = arguments.apple_data
    bangle = arguments.phystrax_data
    output_directory = arguments.output_directory

    # Check that the input files exist 
    check(apple)
    check(bangle)

    # Standardize the formatting of each for later comparison
    processed_apple_csv = pa.process(apple, output_directory) # Returns a filename
    processed_bangle_csv = pb.process(bangle, output_directory) # Returns a filename

    # Run correlation statistics. Create correlation graphic. Save to output directory

    # Print summary

    # Exit
    sys.exit(0)

if __name__ == "__main__":
    main()