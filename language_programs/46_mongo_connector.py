import pymongo
from random import randint

def get_db(db_name):
    client = pymongo.MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_data(db, query,projection):
    # For local use
    return db.states.find(query,projection)

def find_query():
    query = {"name" : "andhra"}
    return query

def add_state(db,state):
    temp = randint(100,1000)
    db.states.insert({"name" : state,"variable":temp})

def get_state(db):
    return db.state.find()

if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    '''
    states = ['andhra','karnataka','kelera']
    for state in states:
        add_state(db,state)
    print(get_state(db))
    '''

    
    #Read operation
    query = find_query()
    projection = {"_id":1,"name":1,"variable":1}
    results = find_data(db, query, projection)

    import pprint
    for data in results:
        pprint.pprint(data)
    

    
