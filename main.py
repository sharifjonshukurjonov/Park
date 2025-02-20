import uuid
import json


class Park:
    def __init__(self, name, information):
        self.name = name
        self. information = information
        self.visitors_count = 0


class Atraksion:
    def __init__(self):
        self.info = []

    def add_atraksion(self, name, information):
        atraksion = {
            "Name": name,
            "Information": information,
            "Id": uuid.uuid4()
        }
        self.info.append(atraksion)

    def remove_atraksion(self, atraksion_id):
        for atraksion in self.info:
            if atraksion["Id"] == atraksion_id:
                self.info.remove(atraksion)
                return f"{atraksion_id} ID raqamli atraksion o'chirildi!"
        return f"{atraksion_id} ID raqamli atraksion topilmadi!"

    def get_id(self, name):
        for atraksion in self.info:
            if atraksion["Name"] == name:
                return atraksion["Id"]
        return None

    def info_atraksions(self):
        return self.info

# a = Atraksion()
# a.add_atraksion("U", "A")
# a.add_atraksion("A","U")
# print(a.info_atraksions())
# print(a.get_id("U"))
# a.remove_atraksion("0fc0461f-9759-4cba-a61a-9768569b119d")
# print(a.info_atraksions())


class Shops:
    def __init__(self):
        self.info = []

    def add_shop(self, name, information):
        shop = {
            "Name": name,
            "Information": information,
            "Id": uuid.uuid4()
        }
        self.info.append(shop)

    def remove_shop(self, shop_id):
        for shop in self.info:
            if shop["Id"] == shop_id:
                self.info.remove(shop)
                return f"{shop_id} ID raqamli do‘kon o‘chirildi!"
        return f"{shop_id} ID raqamli do‘kon topilmadi!"

    def get_id(self, name):
        for shop in self.info:
            if shop["Name"] == name:
                return shop["Id"]
        return f"{name} isimli do'kon topilmadi!"

    def info_shops(self):
        return self.info

# m = Shops()
# m.add_shop("Supermarket", "Katta oziq-ovqat do‘koni")
# m.add_shop("ElectroMart", "Elektronika do‘koni")
# print(m.info_shops())


class Parking:
    def __init__(self, num_station, num_car):
        self.num_station = num_station
        self.num_car = num_car
        self.car = []
        self.pay_for_hour = 1000
        self.playce = [
            "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
            "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
            "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"
        ]

    def parking_car(self, num_car, hours):
        for num in self.playce:
            if num not in [car["Playce"] for car in self.car]:
                total_price = hours * self.pay_for_hour
                car = {
                    "Car nomer": num_car,
                    "Playce": num,
                    "Hours": hours,
                    "Total price": total_price
                }
                self.car.append(car)
                return f"Mashina {num_car} joylashdi {num}-joyga. To‘lov: {total_price} so‘m"
        return "Bo‘sh joy yo‘q!"

    def pay_for_car(self, num_car):
        for car in self.car:
            if car["Car nomer"] == num_car:
                total_price = car["Total price"]
                self.car.remove(car)
                return f"Mashina {num_car} parkovkadan chiqdi. To‘lov: {total_price} so‘m"
        return "Mashina topilmadi!"


# parking = Parking(3, 5)
# print(parking.parking_car("123XYZ", 3))
# print(parking.pay_for_car("123XYZ"))

class Visitors(Park):
    def __init__(self, name, information):
        super().__init__(name, information)
        self.onehour = 5000

    def enter_park(self):
        self.visitors_count += 1
        return f"{self.name} parkga kirdi."

    def pay(self, hours):
        total = self.onehour * hours
        return f"{self.name} {hours} soat uchun {total} so‘m to‘ladi."

    def all_visitors(self):
        return self.visitors_count


class Hotel:
    def __init__(self):
        self.hotel_prices = {
            "3 yulduz": 100000,
            "4 yulduz": 200000,
            "5 yulduz": 300000
        }
        self.registered_visitors = set()

    def enter_hotel(self, visitor_id, visitor_list):
        if visitor_id in visitor_list:
            self.registered_visitors.add(visitor_id)
            return f"ID {visitor_id} bilan mehmonxonaga kirdi."
        return "Bu ID parkda mavjud emas."

    def pay_hotel(self, visitor_id, stars):
        if visitor_id in self.registered_visitors:
            price = self.hotel_prices.get(stars, "Noto‘g‘ri yulduz darajasi")
            return f"ID {visitor_id} {stars} uchun {price} so‘m to‘ladi."
        return "Bu foydalanuvchi mehmonxonada emas."





def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


filename = "park_data.json"
park_data = load_data(filename)
if not park_data:
    park_data = {"visitors": [], "atraksions": [], "shops": [], "parking": [], "hotel": []}
    save_data(filename, park_data)

while True:
    print("\n--- PARK MANAGEMENT SYSTEM ---")
    print("1. Parkga tashrif buyurish")
    print("2. Atraksion qo‘shish")
    print("3. Atraksion o‘chirish")
    print("4. Do‘kon qo‘shish")
    print("5. Do‘kon o‘chirish")
    print("6. Parking joyiga mashina qo‘yish")
    print("7. Mashinani parkingdan chiqarish")
    print("8. Mehmonxonaga joylashish")
    print("9. Mehmonxonadan chiqish")
    print("10. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        name = input("Ismingizni kiriting: ")
        visitor = {"name": name, "role": "Mehmon"}
        park_data["visitors"].append(visitor)
        print(f"{name} parkga kirdi.")
        save_data(filename, park_data)

    elif choice == "2":
        name = input("Atraksion nomi: ")
        info = input("Atraksion haqida ma’lumot: ")
        atraksion = {"name": name, "info": info}
        park_data["atraksions"].append(atraksion)
        print(f"{name} atraksioni qo‘shildi.")
        save_data(filename, park_data)

    elif choice == "3":
        atr_name = input("Atraksion nomini kiriting: ")
        park_data["atraksions"] = [a for a in park_data["atraksions"] if a["name"] != atr_name]
        print(f"{atr_name} atraksioni o‘chirildi.")
        save_data(filename, park_data)

    elif choice == "4":
        name = input("Do‘kon nomi: ")
        info = input("Do‘kon haqida ma’lumot: ")
        shop = {"name": name, "info": info}
        park_data["shops"].append(shop)
        print(f"{name} do‘koni qo‘shildi.")
        save_data(filename, park_data)

    elif choice == "5":
        shop_name = input("Do‘kon nomini kiriting: ")
        park_data["shops"] = [s for s in park_data["shops"] if s["name"] != shop_name]
        print(f"{shop_name} do‘koni o‘chirildi.")
        save_data(filename, park_data)

    elif choice == "6":
        car_num = input("Mashina raqamini kiriting: ")
        hours = int(input("Necha soat turadi?: "))
        parking = {"car_number": car_num, "hours": hours}
        park_data["parking"].append(parking)
        print(f"{car_num} mashinasi parkingga qo‘yildi.")
        save_data(filename, park_data)

    elif choice == "7":
        car_num = input("Mashina raqamini kiriting: ")
        park_data["parking"] = [p for p in park_data["parking"] if p["car_number"] != car_num]
        print(f"{car_num} mashinasi parkingdan chiqarildi.")
        save_data(filename, park_data)

    elif choice == "8":
        visitor_id = input("Mehmon ID sini kiriting: ")
        stars = input("3, 4 yoki 5 yulduz tanlang: ")
        hotel = {"visitor_id": visitor_id, "stars": stars}
        park_data["hotel"].append(hotel)
        print(f"ID {visitor_id} mehmonxonaga joylashdi.")
        save_data(filename, park_data)

    elif choice == "9":
        visitor_id = input("Mehmon ID sini kiriting: ")
        park_data["hotel"] = [h for h in park_data["hotel"] if h["visitor_id"] != visitor_id]
        print(f"ID {visitor_id} mehmonxonadan chiqdi.")
        save_data(filename, park_data)

    elif choice == "10":
        print("Dasturdan chiqildi.")
        break

    else:
        print("Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")