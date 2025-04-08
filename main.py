from functions import read_json_file, create_apps_array, populate_apps_array, write_json_apps_array, create_apps, create_credential_pair, create_credentials
import sys


token = sys.argv[1]
products = sys.argv[2]
org = sys.argv[3]
developer = sys.argv[4]

def create_apps_structure():
    #Read Json file
    user_array = read_json_file("users")
    #print(user_array)
    apps_array = { "apps": {} }

    for user in user_array["users"]:
        apps_array = create_apps_array(user, apps_array)
    
    for user in user_array["users"]:
        apps_array = populate_apps_array(user, apps_array)
    
    write_json_apps_array(apps_array)
    
    #Read Json file
    business_array = read_json_file("data")
    
    for business in business_array["apps"]:
        create_apps(org, token, developer, business)
        print("Created app: " + business)
        for credential in business_array["apps"][business]:
            key, secret = create_credential_pair(credential)
            create_credentials(key, secret, org, token, developer, business, products)
            print("Created following credentials: " + key + " secret: " + secret)
    
if __name__ == "__main__":
    create_apps_structure()