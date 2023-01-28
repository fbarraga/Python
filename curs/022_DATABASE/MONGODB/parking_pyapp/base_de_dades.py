# Execute before
# pip install pymongo
# dnspython-2.2.1 pymongo-4.3.2

# db.createUser( { user: "adminbdd", pwd: "12345678", roles:["dbAdmin"] })

import pymongo

def establir_connexio():
   # conn = pymongo.MongoClient(host="localhost",  port=27017,
   #                             username="adminbdd",
   #                             password="12345678")

    conn = pymongo.MongoClient("mongodb+srv://adminbdd:tenD8RfCFs4fD5Mj@cluster0.c5vvpgj.mongodb.net/?retryWrites=true&w=majority")
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