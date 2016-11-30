# _*_coding:utf-8_*_
import pickle
def dump(database):
    f=file("database.pkl","w")
    pickle.dump(database,f)
    f.close()

def load():
    f=file("database.pkl")
    database=pickle.load(f)
    f.close()
    return database

if __name__ == '__main__':
    pass