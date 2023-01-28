import datetime

def llistar(conn_bdd):
    documents_historial = conn_bdd["historial"].find()

    llista_historial = []

    for doc in documents_historial:
        element_llista = f"{doc['moment']} {doc['matricula']} {doc['moviment']} {doc['lloc']}"  
        llista_historial.append(element_llista)
    return llista_historial  

def preu_a_pagar(conn_bdd, p):
    ll = p.zfill(2)
    llista_historial = list(conn_bdd["historial"].find({'lloc': ll}))  
    penultim_element = llista_historial[-2]
    darrer_element = llista_historial[-1]

    mat = penultim_element['matricula']

    t_entrada = datetime.datetime.strptime(penultim_element['moment'], "%Y-%m-%d %H:%M:%S")  
    t_sortida = datetime.datetime.strptime(darrer_element['moment'], "%Y-%m-%d %H:%M:%S")  
    minuts = (t_sortida - t_entrada).total_seconds() / 60

    llista_preus = list(conn_bdd["preus_minut"].find())  
    darrer_preu = llista_preus[-1]
    preu = darrer_preu['preu']
    res = round(float(preu) * float(minuts),2)  
    return res
