import json
import time
import os
import sys
from steampy.guard import generate_one_time_code


def getcode(shared_secret):
    one_time_authentication_code = generate_one_time_code(shared_secret)
    return one_time_authentication_code


def get_login_by_id(steam_id):
    for filename in os.listdir('data/maFiles/'):
        file_path = os.path.join('data/maFiles/', filename)
        with open(file_path, encoding='utf-8') as file:
            src = file.read()
            data = json.loads(src)
            account_name = data["account_name"]
            account_id = data["Session"]["SteamID"]
            if account_id == steam_id:
                return account_name


def get_id_by_key(key):
    for filename in os.listdir('data/maFiles/'):
        file_path = os.path.join('data/maFiles/', filename)
        with open(file_path, encoding='utf-8') as file:
            src = file.read()
            data = json.loads(src)
            account_id = data["Session"]["SteamID"]
            account_name = data["account_name"]
            if account_name == key:
                return data["Session"]["SteamID"]


def get_password_by_key(key):
    with open('data/accounts.json', 'r', encoding='utf-8') as file:
        src = file.read()
        data = json.loads(src)
        account_key = data[key]
        return data[key]


def get_shared_secret_by_key(key):
    for filename in os.listdir('data/maFiles/'):
        file_path = os.path.join('data/maFiles/', filename)
        with open(file_path, encoding='utf-8') as file:
            src = file.read()
            data = json.loads(src)
            account_name = data["account_name"]
            if account_name == key:
                return data['shared_secret']