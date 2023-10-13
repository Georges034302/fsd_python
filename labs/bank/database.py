import pickle

# Customer objects are stored as binary in the file
file = 'customers.data'

class Database:    

    @staticmethod
    def save(data):
        with open(file,'wb') as handler:
            pickle.dump(data,handler)
        handler.close()
        
    @staticmethod
    def read():
        with open(file,'rb') as handler:
            data = pickle.load(handler)
        handler.close()
        return data 