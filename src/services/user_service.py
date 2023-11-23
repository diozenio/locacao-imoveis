def login_service():
    from domain.user import login
    credentials = login()

    from repository.user_repository import get_all_users
    users = get_all_users()

    for user in users:
        if user["username"] == credentials["username"] and user["password"] == credentials["password"]:
            return user
    
    return None

def register_service():
    from domain.user import register
    user = register()

    from repository.user_repository import save_user
    save_user(user["user_id"], user["name"], user["username"], user["password"])

    return user
