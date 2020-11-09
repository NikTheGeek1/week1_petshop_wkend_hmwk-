# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]


def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]


def add_or_remove_cash(pet_shop_dict, amount):
    pet_shop_dict["admin"]["total_cash"] = pet_shop_dict["admin"]["total_cash"] + amount


def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"]


def increase_pets_sold(pet_shop_dict, amount):
    pet_shop_dict["admin"]["pets_sold"] = pet_shop_dict["admin"]["pets_sold"] + amount


def get_stock_count(pet_shop_dict):
    return len(pet_shop_dict["pets"])

def get_pets_by_breed(pet_shop_dict, breed):
    pets = []
    for pet in pet_shop_dict["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)

    return pets

def find_pet_by_name(pet_shop_dict, name):
    for pet in pet_shop_dict["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop_dict, name):
    pet_to_delete = find_pet_by_name(pet_shop_dict, name)
    pet_shop_dict["pets"].remove(pet_to_delete)
    

def add_pet_to_stock(pet_shop_dict, pet):
    pet_shop_dict['pets'].append(pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, amount):
    customer['cash'] = customer['cash'] - amount

def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)

def customer_can_afford_pet(customer, pet):
    return get_customer_cash(customer) >= pet['price']

def sell_pet_to_customer(pet_shop_dict, pet, customer):
    # check if they can afford it 
    if pet and customer_can_afford_pet(customer, pet):
        # custumer buys pet (their money decrease and they got +1 pet)
        add_pet_to_customer(customer, pet)
        # remove custumer's cash
        pet_price = pet['price']
        remove_customer_cash(customer, pet_price)

        # the shop is by one pet light, pets_sold increases, total_cash increases
        remove_pet_by_name(pet_shop_dict, pet['name'])
        increase_pets_sold(pet_shop_dict, 1)
        add_or_remove_cash(pet_shop_dict, pet_price)