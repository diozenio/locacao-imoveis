from domain.property import publish
from repository.property_repository import (
    save_property,
    get_properties_by_owner_id,
    get_property_by_id,
    get_properties_by_renter_id,
    rent_property,
    return_property,
    get_all_properties
)

def publish_property_service(owner_id):
    property_data = publish(owner_id)
    save_property(
        property_data["property_id"],
        property_data["name"],
        property_data["description"],
        property_data["price"],
        property_data["owner_id"]
    )
    return property_data

def get_properties_by_owner_id_service(owner_id):
    return get_properties_by_owner_id(owner_id)

def get_property_by_id_service(property_id):
    return get_property_by_id(property_id)

def get_properties_by_renter_id_service(renter_id):
    return get_properties_by_renter_id(renter_id)

def rent_property_service(property_id, renter_id):
    return rent_property(property_id, renter_id)

def return_property_service(property_id):
    return return_property(property_id)

def get_all_properties_service():
    return get_all_properties()