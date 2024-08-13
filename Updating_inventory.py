#Importing imporatant library
import json

#Loading Inventory Files(Records) from JSON as a string
fdinv = open("Records.json" , 'r')
js = fdinv.read()
fdinv.close()

#Loading String as JSON/Dictionaries
resource = json.loads(js)

#Setting password For authorized manipulation of inventory
pwd = "1234"

#Listing Current Inventory
for i in resource:
    print("Product id : " ,  i , "Product Name : " , resource[i]["Name"] , "Available Quantity : " ,resource[i]["Quantity"])

#Code for validation of product metadata and password
ch = input("Do you want to update the inventory? /n Press Y/y for Yes anyther for No:\n")
myloop = True

if(ch == 'y' or ch == 'Y'):
    pwd_i = input("Enter password to update: ")
    if(pwd_i == pwd):
                while(myloop):
                    upd_pid = str(input("Enter product id: "))
                    if upd_pid in resource:
                        upd_pqn = int(input("Enter updated product quantity: "))
                        resource[upd_pid]["Quantity"] = upd_pqn
                        print("Updated Quantity: " , resource[upd_pid]["Quantity"])
                        js_updated = json.dumps(resource)
                        fdinv = open("Records.json" , 'w')
                        fdinv.write(js_updated)
                        fdinv.close()
                        temp = input("Do you want to update any other quantity: /n Press Y/y for Yes any other for No:\n")
                        if(temp == 'y' or temp =='Y'):
                             pass
                        else:
                             myloop = False
                    else:
                        print("Enter a valid Product id")
                print("Printing The Updated Inventory")  
                for i in resource:
                    print("Product id : " ,  i , "Product Name : " , resource[i]["Name"] , "Available Quantity : " ,resource[i]["Quantity"])         
    else:
                print("Please rerun and enter a correct password")




            
