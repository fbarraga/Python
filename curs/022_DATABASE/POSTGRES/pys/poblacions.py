def llista_poblacions(con):  
    cur = con.cursor()
    query = "SELECT DISTINCT poblacio FROM codi_postal ORDER BY poblacio;"  
    cur.execute(query)
    reg = cur.fetchall()

    res = []

    for fil in reg:  
        res.append(fil[0])
        cur.close()  
    return res
