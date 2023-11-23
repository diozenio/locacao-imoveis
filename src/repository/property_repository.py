import os

def ensure_data_folder_exists():
    data_folder = "./src/data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

def get_file_path():
    ensure_data_folder_exists()
    return "./src/data/properties.txt"

def read_properties_from_file():
    file_path = get_file_path()
    properties = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                property_id, name, description, price, owner_id, renter_id = line.strip().split(',')
                properties.append({
                    "property_id": int(property_id),
                    "name": name,
                    "description": description,
                    "price": float(price),
                    "owner_id": int(owner_id),
                    "renter_id": int(renter_id) if renter_id != "None" else None
                })
    return properties

def write_properties_to_file(properties):
    file_path = get_file_path()
    with open(file_path, 'w') as file:
        for prop in properties:
            file.write(f"{prop['property_id']},{prop['name']},{prop['description']},{prop['price']},{prop['owner_id']},{prop['renter_id']}\n")

def save_property(property_id, name, description, price, owner_id):
    properties = read_properties_from_file()
    prop = {
        "property_id": property_id,
        "name": name,
        "description": description,
        "price": float(price),
        "owner_id": int(owner_id),
        "renter_id": None
    }
    properties.append(prop)
    write_properties_to_file(properties)

def get_properties_by_owner_id(owner_id):
    properties = read_properties_from_file()
    return [prop for prop in properties if prop["owner_id"] == owner_id]

def get_property_by_id(property_id):
    properties = read_properties_from_file()
    for prop in properties:
        if prop["property_id"] == property_id:
            return prop
    return None

def get_properties_by_renter_id(renter_id):
    properties = read_properties_from_file()
    return [prop for prop in properties if prop["renter_id"] == renter_id]

def rent_property(property_id, renter_id):
    properties = read_properties_from_file()
    for prop in properties:
        if prop["property_id"] == property_id and prop["renter_id"] is None:
            prop["renter_id"] = renter_id
            write_properties_to_file(properties)
            return True
    return False

def return_property(property_id):
    properties = read_properties_from_file()
    for prop in properties:
        if prop["property_id"] == property_id and prop["renter_id"] is not None:
            prop["renter_id"] = None
            write_properties_to_file(properties)
            return True
    return False

def get_all_properties():
    return read_properties_from_file()