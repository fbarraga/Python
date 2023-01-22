import requests
from plyer import notification
from apscheduler.schedulers.blocking import BlockingScheduler
import json
# import pytz

def get_data_from_brightdata():

    headers = {
        'Authorization': 'Bearer 6a302705-a7da-462d-b801-f9f5ce7c1a57',
        'Content-Type': 'application/json'
    }

    response=requests.get("https://api.brightdata.com/dca/dataset?id=j_lc534zsd10y7bcu5f0",headers=headers)
    return response
    
def send_notification():         
    prices = []
    data = get_data_from_brightdata()
    
    datos = json.dumps(data.json())
    
   # print(datos)
    for obj in data.json():
        if obj['price']<300:
            print("El producte: {} te un preu de {}. Pots consultar-ho en el link: {}".format(obj['title'],obj['price'],obj['url']))
            notification.notify(
                title='Price Alert',
                message='The price is under 300!->',
                #app_icon='icon.png',
                timeout=100
            )


send_notification()
#scheduler= BlockingScheduler()
#tz=pytz.timezone('US/Eastern')

#scheduler.add_job(send_notification,'cron',minute='*/1')
#scheduler.start()