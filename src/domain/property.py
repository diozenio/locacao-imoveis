from utils.divider import divider
from utils.generate_id import generate_id

def publish(owner_id):
    divider()
    name = input("Digite o nome da propriedade: ")
    description = input("Digite a descrição da propriedade: ")
    price = input("Digite o preço da propriedade: ")
    divider()
    property = {"property_id": generate_id(), "name": name, "description": description, "price": price, "owner_id": owner_id, "renter_id": "None"}
    return property