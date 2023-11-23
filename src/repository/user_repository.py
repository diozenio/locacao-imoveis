import os

def ensure_data_folder_exists():
    data_folder = "./src/data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

def get_file_path():
    ensure_data_folder_exists()
    return "./src/data/users.txt"

def read_users_from_file():
    file_path = get_file_path()
    users = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                user_id, name, username, password = line.strip().split(',')
                users.append({"user_id": int(user_id), "name": name, "username": username, "password": password})
    return users

def write_users_to_file(users):
    file_path = get_file_path()
    with open(file_path, 'w') as file:
        for user in users:
            file.write(f"{user['user_id']},{user['name']},{user['username']},{user['password']}\n")

def save_user(user_id, name, username, password):
    users = read_users_from_file()
    user = {"user_id": user_id, "name": name, "username": username, "password": password}
    users.append(user)
    write_users_to_file(users)

def get_all_users():
    return read_users_from_file()

def find_user_by_id(user_id):
    users = read_users_from_file()
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None
