import pandas as pd
import os

print(type(os.getcwd()))

# read the csv
test_df = pd.read_csv('C:/Users/Gradebook/Desktop/Project/Test.csv')
print(test_df)
