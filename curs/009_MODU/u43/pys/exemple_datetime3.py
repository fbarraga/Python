import datetime

avui = datetime.datetime.now()
dema = avui + datetime.timedelta(days=1)
passat = avui + datetime.timedelta(days=2)
print(f"avui: {avui}")
print(f"dema: {dema}")
print(f"passat: {passat}")