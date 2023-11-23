from utils.menu import menu
from utils.divider import divider
from services.user_service import register_service, login_service
from services.property_service import (
    publish_property_service,
    get_properties_by_owner_id_service,
    get_property_by_id_service,
    get_properties_by_renter_id_service,
    rent_property_service,
    return_property_service,
    get_all_properties_service
)

def UnAuthApp():
    def register():
        user = register_service()
        AuthApp(user)

    def login():
        user = login_service()
        if user is not None:
            AuthApp(user)
        else:
            print("Usuário ou senha inválidos")
            UnAuthApp()

    options = [
        {"name": "Criar Conta", "function": register, "params": None},
        {"name": "Entrar", "function": login, "params": None},
    ]

    menu("Locação de Imóveis", options)

def AuthApp(user):
    def publish_property():
        property_data = publish_property_service(user["user_id"])
        print(f"Propriedade '{property_data['name']}' publicada com sucesso!")

    def view_all_properties():
        properties = get_all_properties_service()
        if len(properties) == 0:
            divider()
            print("Todas as propriedades")
            divider()
            print("Não há propriedades disponíveis no momento.")
            divider()
            return
        propertiesMenuOptions = []
        for prop in properties:
            propertiesMenuOptions.append({"name": prop["name"], "function": view_property_details, "params": prop["property_id"]})
        menu("Todas as propriedades", propertiesMenuOptions)

    def view_properties_by_owner():
        properties = get_properties_by_owner_id_service(user["user_id"])
        if len(properties) == 0:
            divider()
            print("Suas propriedades")
            divider()
            print("Você não possui nenhuma propriedade.")
            divider()
            return
        myPropertiesMenuOptions = []
        for prop in properties:
            myPropertiesMenuOptions.append({"name": prop["name"], "function": view_property_details, "params": prop["property_id"]})
        menu("Suas propriedades", myPropertiesMenuOptions)

    def view_property_details(property_id):
        property_details = get_property_by_id_service(property_id)
        if property_details:
            divider()
            print(f"Detalhes da propriedade '{property_details['name']}':")
            print(f"Descrição: {property_details['description']}")
            print(f"Preço: {property_details['price']}")
            print(f"Status: {'Alugada' if property_details['renter_id'] else 'Disponível'}")
            divider()
            choice = None
            if property_details["renter_id"] is None:
                if property_details["owner_id"] != user["user_id"]:
                    print("1. Alugar")
                    print("0. Voltar")
                    choice = input("Escolha uma opção: ")
                    if choice == "1":
                        rent_property_action(property_id)
            elif property_details["renter_id"] == user["user_id"]:
                print("1. Devolver")
                print("0. Voltar")
                choice = input("Escolha uma opção: ")
                if choice == "1":
                    return_property_action(property_id)
            print("0. Voltar")   
                    
        else:
            print("Propriedade não encontrada.")

    def rent_property_action(property_id):
        success = rent_property_service(property_id, user["user_id"])
        if success:
            print("Propriedade alugada com sucesso!")
        else:
            print("Falha ao alugar a propriedade.")

    def return_property_action(property_id):
        success = return_property_service(property_id)
        if success:
            print("Propriedade devolvida com sucesso!")
        else:
            print("Falha ao devolver a propriedade. Talvez ela não esteja alugada ou não exista.")

    def view_properties_by_renter():
        properties = get_properties_by_renter_id_service(user["user_id"])
        if len(properties) == 0:
            divider()
            print("Propriedades alugadas")
            divider()
            print("Você não possui nenhuma propriedade alugada.")
            divider()
            return
        propertiesMenuOptions = []
        for prop in properties:
            propertiesMenuOptions.append({"name": prop["name"], "function": view_property_details, "params": prop["property_id"]})
        menu("Propriedades alugadas", propertiesMenuOptions)

    options = [
        {"name": "Publicar Propriedade", "function": publish_property, "params": None},
        {"name": "Lista de Propriedades", "function": view_all_properties, "params": None},
        {"name": "Minhas Propriedades", "function": view_properties_by_owner, "params": None},
        {"name": "Ver Propriedades Alugadas", "function": view_properties_by_renter, "params": None},

    ]

    menu("Locação de Imóveis - Bem-vindo, " + user["name"], options)
