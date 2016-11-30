import pickle

def DataBase():
    loginDB = {
        "1234": ["12344",10000],
        "1235": ["12355",10000],
        "1236": ["12366",10000]
    }
    f=file("database.pkl","w")
    pickle.dump(loginDB,f)
    f.close()

if __name__ == '__main__':
    DataBase()
    f=file("database.pkl")
    loginDB=pickle.load(f)
    f.close()
    # print type(loginDB)
    print loginDB["1234"][0]
