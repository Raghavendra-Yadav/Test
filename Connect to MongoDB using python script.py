# Connecting to MongoDB using python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://graghavendrayadav:Raghu@cluster0.gwjlwmk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    '''for db_name in client.list_database_names():
        print(db_name)*/''' #once sucessfully established connection
except Exception as e:
    print(e)

# End