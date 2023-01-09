import json

userName = "Carlos"
userEmail = "Carlos@email.com"
userPassword = "Senha@123"
userPhone = "+5511123456789"
userAge = 25

accounts = []
doc = {"accounts": accounts}

user = {
    "name": userName,
    "email": userEmail,
    "password": userPassword,
    "phone": userPhone,
    "age": userAge,
}


accounts.append(user)

try:
    file = open("MyJson.json")
    data = json.load(file)

    with open("MyJson.json", "a") as arquivo:  
        json.dump(doc, arquivo, indent=4)

    file.close()

except:
    with open("MyJson.json", "w") as arquivo:  
        json.dump(doc, arquivo, indent=4)




    
    


    
    
    

        



