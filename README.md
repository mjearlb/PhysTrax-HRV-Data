# PhysTrax-HRV-Data

The files contained in "old" are from Summer 2024. I was experimenting with tracking HRV using the Bangle JS's PPG sensor. I am now shifting focus to work on scripts to confirm the reliability of the existing heart rate tracker on the Bangle JS using PhysTrax correlation with Apple Watch data. 

To run the new program: 
Use the command:
'''
./venv/bin/python ./src/main.py -a example_data/8:14:25/apple.csv -p example_data/8:14:25/phystrax.csv -out example_data -o -4
'''
Note that this provides a path to some example data, which the offset applied to the Apple data is -4 hours. It is unknown why Apple requires this. 