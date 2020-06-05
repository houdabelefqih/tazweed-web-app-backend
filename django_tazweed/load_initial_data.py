from .tazweed_app.models import Seller, Client, Shop, Slot, Appointment
from datetime import datetime

shop1 = Shop(name="Garage hub", address="90 Fifth St", start_hour=8, end_hour=17)
shop2=Shop(name="Garagy", address="90 Fifth St", start_hour=6, end_hour=12)
shop3= Shop(name="Carz", address="44 avenue", start_hour=9, end_hour=15)

shop1.save()
shop2.save()
shop3.save()


client1 = Client(name="Badr client", username="badr", password="pass", 
phone="0987654321", email="badr@gmail.com")
client2 = Client(name="Yasmine client", username="yasmine", password="pass2", 
phone="0987655321", email="yasmine@gmail.com")
client3 = Client(name="Aya client", username="aya", password="pass3", 
phone="0987629876", email="aya@gmail.com")

seller1= Seller(name="Hakim Seller", username="hakim", password="pass55", 
phone="091234561", email="hakim@gmail.com", shop=shop1)
seller2= Seller(name="Maryam Seller", username="maryam", password="pass95", 
phone="091234001", email="maryam@gmail.com", shop=shop2)
seller3=Seller(name="Ismail Seller", username="ismail", password="pass005", 
phone="099999001", email="ismail@gmail.com", shop=shop3)

slot1= Slot(datetime= datetime(2020, 5, 6, 12), duration = 2)
slot2=Slot(datetime= datetime(2020, 5, 7, 9), duration = 3)
slot3=Slot(datetime= datetime(2020, 5, 7, 3), duration = 2)

seller1.available_slots.append(slot1)
seller1.available_slots.append(slot2)
seller1.available_slots.append(slot3)

seller1.save()

slot4= Slot(datetime= datetime(2020, 5, 6, 6), duration = 2)
seller2.available_slots.append(slot4)

seller2.save()

slot5= Slot(datetime= datetime(2020, 5, 6, 10), duration = 1)
seller3.available_slots.append(slot5)



