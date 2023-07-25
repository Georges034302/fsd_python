import os
import sys 
import random as ran
import student as s

def filepath():
    scriptpath = os.path.abspath(sys.argv[0])
    scriptdir = os.path.dirname(scriptpath)
    return scriptdir
    
def read():
    path = filepath()
    file = input("Read CSV File: ")
    s.read_from_csv(path+"\\"+file)
    s.read_pandas(path+"\\"+file)
    
def write():
    path = filepath()
    file = input("Write to CSV File: ")
    name = input("Name: ")
    mark = int(input("Mark: "))
    id = ran.randint(100000,999999)
    g = s.grade(mark)
    s.write_to_csv(path+"\\"+file,id,name,mark,g)
    
def run():
    choice = input("Choice(r/w/x): ")
    
    while choice != "x":
        match choice:
            case 'r': read()
            case 'w': write()
            case _ : print("Unknown choice!")
        choice = input("Choice(r/w/x): ")    
    
run()