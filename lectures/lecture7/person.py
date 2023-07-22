import random as ran
import pprint as pp

def unique_ids(first,last,size):
    return list(set(ran.sample(range(first,last),size)))

def records(keys):
    names = {}
    for key in keys:
        names[key] = input("Name: ")
    return names

def create(names, key, value):
        names[key] = value

def read(names,ID):
    return names[ID]       

def update(names,key,value):
    names[key] = value

def delete(names,key):  
        del names[key]
        
def view(names):
    pp.pprint(names,width=20)