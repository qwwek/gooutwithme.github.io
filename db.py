from pymongo import MongoClient


client = MongoClient('localhost',27017)
db_name = 'weather'
db = client[db_name]


def save_doc(coll_name, doc):
    collection = db[coll_name]
    collection.insert_one(doc)

# Can return: 1) JSON; 2) None
def get_data(coll_name, query):
    collection = db[coll_name]
    return collection.find_one(query)

def del_doc(coll_name, query):
    collection = db[coll_name]
    collection.delete_one(query)


if __name__ == '__main__':
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": "datetime.datetime.now(tz=datetime.timezone.utc),"
    }

    #save_doc(post)
    print(get_data('auth', {'author': 'Mike'}))
