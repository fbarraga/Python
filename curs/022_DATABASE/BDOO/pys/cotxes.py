from tinydb import TinyDB, Query

dades_cotxes = TinyDB('cbdd.json')
dades_cotxes.insert_multiple([
 {'marca': 'renault', 'model': 'clio', 'tipus_motor': 'diesel', 'any': 2013},
 {'marca': 'seat', 'model': 'ibiza', 'tipus_motor': 'diesel', 'any': 1998},
 {'marca': 'renault', 'model': 'megane', 'tipus_motor': 'gasolina', 'any': 2005},
 {'marca': 'toyota', 'model': 'verso', 'tipus_motor': 'hibrid', 'any': 2016},
 {'marca': 'renault', 'model': 'twingo', 'tipus_motor': 'gasolina', 'any': 2012},
 {'marca': 'toyota', 'model': 'prius', 'tipus_motor': 'hibrid', 'any': 2020},
 {'marca': 'opel', 'model': 'corsa', 'tipus_motor': 'diesel', 'any': 2006},
 {'marca': 'peugeot', 'model': '207', 'tipus_motor': 'gasolina', 'any': 2009}])
num_cotxes = len(dades_cotxes)
q_num_gasolina = dades_cotxes.count(Query().tipus_motor == 'gasolina')
q_num_diesel = dades_cotxes.count(Query().tipus_motor == 'diesel')
q_num_hibrid = dades_cotxes.count(Query().tipus_motor == 'hibrid')
print(f"Número total de cotxes: {num_cotxes}")
print(f"Gasolina: {q_num_gasolina} Diesel: {q_num_diesel} Híbrid: {q_num_hibrid}")
print()
q_no_diesel = dades_cotxes.search(Query().tipus_motor != 'diesel')
print("Cotxes no diesel anteriors al 2010")
for c in q_no_diesel:
 marca = c.get('marca')
 model = c.get('model')
 anny = c.get('any')
 if anny < 2010:
    print(f"\t{marca.title()} {model.title()} ({anny})")
print()
dades_cotxes.close()