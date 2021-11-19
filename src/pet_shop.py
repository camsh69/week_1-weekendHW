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
    