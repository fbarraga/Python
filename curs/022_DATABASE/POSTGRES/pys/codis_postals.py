
def llista_cp(con):  
    cur = con.cursor()
    query = "SELECT num, poblacio FROM codi_postal ORDER BY num;"  
    cur.execute(query)
    reg = cur.fetchall()

    res = []


    for fil in reg:
        dades = fil[0] + ' ' + fil[1]  
        res.append(dades)
        cur.close()  
    return res

def afegir_cp(con, c, p):  
    cur = con.cursor()
    query = f"INSERT INTO codi_postal VALUES ('{c}','{p}');"  
    cur.execute(query)
    con.commit()  
    cur.close()
