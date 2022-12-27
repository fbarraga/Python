import datetime

ara = datetime.datetime.now()
print(ara)
print(ara.strftime("%y%m%d_%H%M%S"))
print(f"{ara.day}/{ara.month}/{ara.year}")
print(f"{ara.hour}:{ara.minute}:{ara.second}")

