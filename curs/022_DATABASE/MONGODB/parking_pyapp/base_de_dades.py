# Execute before
# pip install pymongo
# dnspython-2.2.1 pymongo-4.3.2

# db.createUser( { user: "adminbdd", pwd: "12345678", roles:["dbAdmin"] })

import pymongo

def establir_connexio():
   # Connexió a un MongoDB on Premise
   # conn = pymongo.MongoClient(host="localhost",  port=27017,
   #                             username="adminbdd",
   #                             password="12345678")

    # Connexió a MongoDB Atlas
    conn = pymongo.MongoClient("mongodb+srv://adminbdd:12345678@cluster0.bokx6yz.mongodb.net/?retryWrites=true&w=majority")
    db=conn.get_database('parking')
    records = db.atopic
    print(records.count_documents({}))
   
   
   
    #conn  = pymongo.MongoClient(host="localhost",  port=27017)
    return conn

def seleccionar_bdd(conn):  
    conn_bdd = conn["parking"]
    
    
    return conn_bdd

def tancar_connexio(conn):  
    conn.close()

conn = establir_connexio()
print(seleccionar_bdd (conn))