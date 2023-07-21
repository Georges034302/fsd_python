import person

def exist(data, key):
    for id in data.keys():
        if id == key:
            return True
    return False

def records():
    data = {}
    first = int(input("first = "))
    last = int(input("last = "))
    n = int(input("size = "))
    keys = person.unique_ids(first,last,n)
    data = person.records(keys)
    return data

data = records() # data set

def create():
    key = int(input("key = "))    
    if not(exist(data,key)):
        value = input("value = ")
        person.create(data,key,value)
    else:
        print("There is a record associated with ", key)

def read():
    key = int(input("key = "))
    if exist(data,key):
        print(f"{key} --> {data[key]}")
    else:
        print("No record associated with ", key)
        
def update():      
    key = int(input("key = "))    
    if exist(data,key):
        value = input("value = ")
        person.update(data, key, value)  
    else:
        print("No record associated with ", key)

      
    
def delete():
    key = int(input("key = "))
    if exist(data,key):
        person.delete(data,key) 
    else:
        print("No record associated with ", key) 
   
def view():
    person.view(data)
        
def menu():
    choice = input("Choice(c/r/u/d/v/x): ")
    while choice != "x":
        match choice:
            case 'c': create()
            case 'r': read()
            case 'u': update()
            case 'd': delete()
            case 'v': view()
            case _ : print("Unknown choice!")
        choice = input("Choice(c/r/u/d/v/x): ")
menu()