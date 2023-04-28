import datetime


def llistar(conn_bdd):
    print(conn_bdd)
    documents_places = conn_bdd["places"].find()
    llista_places = []
    for doc in documents_places:
        element_llista = f"{doc['planta']} {doc['id']}{doc['grandaria']}"
 
        llista_places.append(element_llista)
    return llista_places

def estat(conn_bdd):
    documents_places = conn_bdd["places"].find()

    estat_places = []

    for doc in documents_places:  
        valor_id = doc['id']
        if doc['ocupada'] == "si": 
            valor_estat = "ocupada"
        if doc['ocupada'] == "no": 
            valor_estat = "disponible"  
            element_llista = f"{valor_id}	{valor_estat}"  
            estat_places.append(element_llista)
    return estat_places  

def entrada(conn_bdd,m,p):
    ll = p.zfill(2)
    conn_bdd["places"].update_one({"id":ll},{"$set":{"ocupada":"si"}})  
    data_hora_ara = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detall_historial = {"moment": data_hora_ara, "matricula": m, "moviment": "entrar", "lloc": ll}  
    conn_bdd["historial"].insert_one(detall_historial)

def sortida(conn_bdd,p):  
    ll = p.zfill(2)
    llista_historial = list(conn_bdd["historial"].find({'lloc': ll}))  
    darrer_element = llista_historial[-1]
    m = darrer_element['matricula']
    conn_bdd["places"].update_one({"id":ll},{"$set":{"ocupada":"no"}})  
    data_hora_ara = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detall_historial = {"moment": data_hora_ara, "matricula": m, "moviment": "sortir", "lloc": ll}  
    conn_bdd["historial"].insert_one(detall_historial)

