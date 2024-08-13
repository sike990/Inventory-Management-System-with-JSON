#Importing inportant libraries
import json
import datetime

#Loading file(Records) from JSON as a String
fd = open("Records.json" , 'r')
js = fd.read()
fd.close()

#Initializing variable
sale = ""

#Converting String records to JSON/Dictionaries
resource = json.loads(js)

#Displaying Menu
print("The available products are : ")
for i in resource:
    print("Product id : " ,  i , "Product Name : " , resource[i]["Name"] , "Available Quantity : " ,resource[i]["Quantity"])

#Taking user meta data and product input
u_name = str(input("Enter your name: "))
u_phone = str(input("Enter your Phone No."))
pid = str(input("Enter product id of desired product : "))
pqn = int(input("Enter desired quantity from the available quantity : "))
mrp = 0

#Function for printing Bill
def generate_bill(pid , pqn ):
    global mrp
    for i in range(3):
        print()
    if(pqn <= resource[pid]["Quantity"]):
        
        mrp = int(pqn*resource[pid]["Price"])    
        print("*" * 50)
        print("Name: " + u_name)
        print("Phone: " + u_phone)
        print("Product: " ,   resource[pid]["Name"])
        print("Quantity: " , pqn)
        print("Price: " , mrp)
        print("*" * 50)
        for i in range(3):
            print()
        if(pqn > 0):
            resource[pid]["Quantity"] -= pqn
        #To display updated quantity
        print("Updated Quantity: " , resource[pid]["Quantity"])


#Code to check validity and availiablity of the product
if pid in resource : 
    
    if(pqn <= resource[pid]["Quantity"]):
        generate_bill(pid , pqn )
    else:
        print("Available Quantity is Less.")
        print("Do you want to purchase the full quantity?")
        ch = input("Press Y/y for yes and N/n for No : \n")

        if (ch == 'Y' or ch == 'y'):
            pqn = resource[pid]["Quantity"]
            generate_bill(pid,pqn)
            
        else:
            print("Thanks")

    #Formatting a string to store as sales data
    sales = u_name+', '+u_phone+', '+"P_id: "+str(pid)+', '+resource[pid]["Name"]+", " + "Quantity: "+str(pqn) + ', ' + "Mrp: " + str(mrp) +', ' +  str(datetime.datetime.now()) + '\n'

    js_updated = json.dumps(resource)
    #print(js_updated)

    #To update the changes happened in the purchase
    fd = open("Records.json" , 'w')
    fd.write(js_updated)
    fd.close()
    # print(sales)

    #To store sales record
    fdsale = open("Sales.txt" , 'a')
    fdsale.write(sales)
    fdsale.close()
    
else:
    print("Enter a valid Product_id: ")




