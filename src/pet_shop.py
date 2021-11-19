# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    new_cash = get_total_cash(pet_shop) + amount
    pet_shop["admin"]["total_cash"] = new_cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_pets_sold):
    new_num_sold = get_pets_sold(pet_shop) + num_pets_sold
    pet_shop["admin"]["pets_sold"] = new_num_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    same_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            same_breed.append(pet["breed"])

    return same_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    i = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
           pet_shop["pets"][i]["name"] = {"name": None}
        i += 1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    new_cash_amt = get_customer_cash(customer) - amount
    customer["cash"] = new_cash_amt

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)