import requests



# user info
print("Enter your username")
user = input()

print("Enter the password")
password = input()




def main():
    url = "http://103.195.100.145:35566/online/user/login"

    while True:
        

        payload = {
            "alias": user,  
            "token": "ponkis16122",  
            "password": password
        }

        try:
            
            response = requests.post(url, json=payload)
            
            
            if response.status_code == 200:
                data = response.json()
                
                  
                
                if data.get("error_type") == "006":
                    print("User dont exist")
                    break                
                elif data.get("error_type") == "007":
                    print("Password Incorrect. But account exist!")
                    print(data)
                    break
                
                print("Account exist and the password is correct!", data)
                return

            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")

        except Exception as e:
            print(f"An error occurred: {e}")
            break


main()