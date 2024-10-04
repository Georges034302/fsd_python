import csv 
import pandas as pd

def grade(mark):
    if mark >= 85:
        grade = "HD"
    elif mark >= 75:
        grade ="D"
    elif mark >= 65:
        grade = "C"
    elif mark >= 50:
        grade = "P"
    else:
        grade = "Z"
    return grade

# read method 1: using csv module
def read_from_csv(file):
    with open(file,'r') as handler:
        csv_object = csv.reader(handler)
        for row in csv_object:
            print(row)
            
# write method 1 using csv module                    
def write_to_csv(file,id,name,mark,grade):
    with open(file,'a',newline='') as handler:
        csv_writer = csv.writer(handler)
        row = [id,name,mark,grade]
        csv_writer.writerow(row)

def read_pandas(file):
    data = pd.read_csv(file)
    print(data)