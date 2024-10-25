import pickle
from pathlib import Path

class Database:

    @staticmethod
    def save(data):
        with open('customers.data','+bw') as handler:
            pickle.dump(data,handler)
        handler.close()
        
    @staticmethod
    def read():
        file
        with open('customers.data','+br') as handler:
            data = pickle.load(handler)
        handler.close()
        return data 