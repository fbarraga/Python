def llista_persones(con):  
    cur = con.cursor()
    query = "SELECT dni, nom, cognoms FROM persona ORDER BY Cognoms;"
    cur.execute(query)  
    reg = cur.fetchall()
    res = []

    for fil in reg:
        dades = fil[0] + ' ' + fil[2] + ', ' + fil[1]  
        res.append(dades)
        cur.close()  
        return res

def llista_persones_patro_cog(con, pat):  
    cur = con.cursor()
    query = f"SELECT dni, nom, cognoms FROM persona WHERE cognoms like '%{pat}%' ORDER BY Cognoms"
    cur.execute(query)  
    reg = cur.fetchall()
    res = []

    for fil in reg:
        dades = fil[0] + ' ' + fil[2] + ', ' + fil[1]  
        res.append(dades)
        cur.close()  
        
        return res

def llista_tel_per(con, d):  
    cur = con.cursor()
    query = f"SELECT numero FROM telefon WHERE id_persona = '{d}'"
    cur.execute(query)  
    reg = cur.fetchall()
    res = []

    for fil in reg:  
        res.append(fil[0])
        cur.close()  
        return res
