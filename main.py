product={
    "648659765087":{
        "title":" A 17",
        "price":"48654876",
        "year":"2025",
        "type":"Phone",
        "id":"648659765087"
    },
    "608760870679":{
        "title":" A 55",
        "price":"48657866",
        "year":"2022",
        "type":"Phone",
        "id":"608760870679"
    },
    "638329372637":{
        "title":"Asus vivobook",
        "price":"978857866",
        "year":"2024",
        "type":"Pc",
        "id":"638329372637"
    },
    "875987557888":{
        "title":"smart 43",
        "price":"7934657866",
        "year":"2025",
        "type":"Tv",
        "id":"875987557888"
    },
    "63287952995":{
        "title":"lg 32",
        "price":"89732657866",
        "year":"2025",
        "type":"Tv",
        "id":"63287952995"
    },
    "62130817434":{
        "title":"hp core i7",
        "price":"243457866",
        "year":"2025",
        "type":"Pc",
        "id":"62130817434"
    }


}
import json
def saqlash():
    with open("product.json", "w", encoding="utf-8") as f:
        json.dump(product, f, indent=4, ensure_ascii=False)


def view_type(d: dict, t: str):
    A = False
    for k, v in d.items():
        if v["type"].lower() == t.lower():
            print(f'id: {k}\n  title: {v["title"]}\n  price: {v["price"]}\n  year: {v["year"]}\n  type: {v["type"]}\n')
            A = True
    if not A:
        print(f"{t} turidagi mahsulot yo'q.\n")


def view_products(d: dict):
    while True:
        kod = input(" 1. TV\n 2. Phone\n 3. Pc\n 4. Exit\n Tanlang: ")
        if kod == "1":
            view_type(d, "Tv")
        elif kod == "2":
            view_type(d, "Phone")
        elif kod == "3":
            view_type(d, "Pc")
        elif kod == "4":
            break
        else:
            print("bunday raqamli mahsulot yoq")


def add_Tv(d: dict):
    title = input("title: ")
    price = input("price: ")
    year = input("year: ")
    type = "Tv"
    id = input("id: ")
    d[id] = {
        "title": title,
        "price": price,
        "year": year,
        "type": type,
        "id": id
    }

def add_Phone(d: dict):
    title = input("title: ")
    price = input("price: ")
    year = input("year: ")
    type = "Phone"
    id = input("id: ")
    d[id] = {
        "title": title,
        "price": price,
        "year": year,
        "type": type,
        "id": id
    }

def add_pc(d: dict):
    title = input("title: ")
    price = input("price: ")
    year = input("year: ")
    type = "Pc"
    id = input("id: ")
    d[id] = {
        "title": title,
        "price": price,
        "year": year,
        "type": type,
        "id": id
    }

def add_product(d: dict):
    while True:
        kod = input(" 1.add_Tv\n 2.add_Phone\n 3.add_pc\n 4.view_products\n 5.exit\n Tanlang: ")
        if kod == "1":
            add_Tv(d)
        elif kod == "2":
            add_Phone(d)
        elif kod == "3":
            add_pc(d)
        elif kod == "4":
            view_products(d)
        elif kod == "5":
            break
        else:
            print(" yuqoridagi raqamlardan birini tanlang ! ")

add_product(product)


