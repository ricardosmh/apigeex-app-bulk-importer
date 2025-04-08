import json
import subprocess
import sys
import base64

#read user json file
def read_json_file(file_name):
    filepath = "{file}.json".format(file=file_name)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#Set apps name based on nomenclature
def set_apps_name(business_name, id_con):
    preffix="legacy"
    suffix="apps"
    return (preffix + "-" + business_name + "-" + str(id_con) + "-" + suffix)

#create json array to hold users
def create_apps_array(user, apps_array):
    apps_name = set_apps_name(user["prefijo_usuarios"], user["id_con"])
    apps_array["apps"][apps_name] = []
    return apps_array

#populate json array with user data
def populate_apps_array(user, apps_array):
    apps_name = set_apps_name(user["prefijo_usuarios"], user["id_con"])
    apps_array["apps"][apps_name].append(user)
    return apps_array

#write clean json apps array to file
def write_json_apps_array(apps_array):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(apps_array, f, ensure_ascii=False, indent=4)

def create_apps(org, token, developer, app_name):
    subprocess.run(["apigeecli", "apps", "create", "-o", org, "-t", token, "-e", developer, "-n", app_name])

def create_credential_pair(credential):
    secret = credential["clave"]
    key = credential["prefijo_usuarios"] + "." + credential["usuario"]
    
    encoded_key = key.encode('ascii')
    encoded_key = base64.b64encode(encoded_key).decode("utf-8")
    encoded_key = encoded_key.replace("=", "")

    return(str(encoded_key), secret)

def create_credentials(key, secret, org, token, developer, app_name, products):
    subprocess.run(["apigeecli", "apps","keys", "create", "-o", org, "-t", token, "-d", developer, "-n", app_name, "-p", products, "-k", key, "-c", secret])
