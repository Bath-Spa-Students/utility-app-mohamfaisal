# Inserting Cold drinks to our vending machine
Cold_drinks = [ 
{"product_code":"A01",
 "product_name":"Dew",
 "product_price": "4 AED" ,
 "product_stock": 4,},

{"product_code":"A02",
 "product_name":"Pepsi",
 "product_price": "3 AED" ,
 "product_stock": 3,},

{"product_code":"A03",
"product_name":"Coke",
"product_price": "5 AED",
"product_stock": 6,},

{"product_code":"A04",
 "product_name":"Fanta",
 "product_price": "6 AED" ,
 "product_stock": 2,},

{"product_code":"A05",
 "product_name":"Water",
 "product_price": "3 AED",
 "product_stock": 10,},
]

# Inserting Snacks to our vending machine 
snacks = [ 
{"product_code":"B01",
 "product_name":"Sando Wafers",
 "product_price": "2 AED" ,
 "product_stock": 4,},

{"product_code":"B02",
 "product_name":"Dairy Milk",
 "product_price": "7 AED" ,
 "product_stock": 3,},

{"product_code":"B03",
 "product_name":"Taki Chips",
 "product_price": "5 AED" ,
 "product_stock": 6,},

{"product_code":"B04",
 "product_name":"Oman chips",
 "product_price": "1 AED" ,
 "product_stock": 8,},

{"product_code":"B05",
 "product_name":"Extra Gum",
 "product_price": "4 AED" ,
 "product_stock": 9,},
]

#Inserting Hot beverages to our vending machine 
Hot_beverages = [
{"product_code":"C01",
 "product_name":"Zafran Chai",
 "product_price": "3 AED",
 "product_stock": 6,},

{"product_code":"C02",
 "product_name":"Espresso",
 "product_price":"10 AED" ,
 "product_stock": 4,},

{"product_code":"C03" ,
 "product_name":"Café au lait",
 "product_price": "15 AED",
 "product_stock": 3,},

{"product_code":"C04",
 "product_name":"Hot chocolate",
 "product_price": "5 AED" ,
 "product_stock": 5,},

{"product_code":"C05",
 "product_name":"Cappuccino",
 "product_price": "9 AED" ,
 "product_stock": 4,},
]

print("------------------------------------------------------------------------")
print("\n\t\t\t𝗩 𝗘 𝗡 𝗗 𝗜𝗡 𝗚  𝗠 𝗔 𝗖 𝗛 𝗜𝗡 𝗘\n")           # showing the desighned vending machine name to the customers 
print("------------------------------------------------------------------------")

# Introducing the cold drinks to our menu 
print("\n𝑪 𝑶 𝑳 𝑫  𝑫 𝑹 𝑰 𝑵 𝑲 𝑺\n") 

for i in Cold_drinks:  # To print the product name , product price , product code and product stock
    print (f"Product: {i['product_name']}\t\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("\n𝑺 𝑵 𝑨 𝑪 𝑲 𝑺\n") 

# Introducing the snacks to our menu
for i in snacks:       # To print the product name , product price , product code and product stock
    print (f"Product: {i['product_name']}\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")
print("\n𝑯 𝑶 𝑻  𝑩 𝑬 𝑽 𝑬 𝑹 𝑨 𝑮 𝑬 𝑺\n") 

# Introducing the hot beverages to our menu 
for i in Hot_beverages:   # To print the product name , product price , product code and product stock
    print(f"Product: {i['product_name']}\t Price: {i['product_price']}\t Code: {i['product_code']} \tStocks: {i['product_stock']}\n")

purchased_item = []  # Empty list of purchased item
total= []            # Empty list of total

anykey= input("\nPress Enter key to proceed...\n")  # Customers have to to press the "Enter key" for proceeding the next procedure 

def main():   # main function takes the imput from the customers
    
    
    balance = int(input("\nInsert your money (Enter Amount):\n"))      # Customers have to insert some amount of money for purchasing a product

    # section - A  Showing the stock available for each products 
    A01_stock = 4  
    A02_stock = 3  
    A03_stock = 6   
    A04_stock = 2   
    A05_stock = 10 
    # section - B  Showing the stock available for each products 
    B01_stock = 4   
    B02_stock = 3   
    B03_stock = 6   
    B04_stock = 8   
    B05_stock = 9  
    # section - C  Showing the stock available for each products 
    C01_stock = 6   
    C02_stock = 4  
    C03_stock = 3   
    C04_stock = 5  
    C05_stock = 4  

    while True: # while loop statement 
        # Customers have to type the particular product key for availing the product from the vending machine 
        buy = input("\nEnter the product code you want to purchase or press q to proceed to payment.\n")

        if buy == "q":    # "q" letter is identified as the EXIT button from the vending machine 
            print("Proceeding to payment..\n")     # When the customers EXIT the vending machine they proceed to the payment section 
            break

        elif buy == "A01":
            print("You've selected A01")
            # Your code for A1
        elif buy == "A02":
            print("You've selected A02")
        elif buy == "A03":
            print("You've selected A03")
        elif buy == "A04":
            print("You've selected A04")
        elif buy == "A05":
            print("You've selected A05")
    
        elif buy == "B01":
            print("You've selected B01")
            # Your code for B1
        elif buy == "B02":
            print("You've selected B02")
        elif buy == "B03":
            print("You've selected B03")
        elif buy == "B04":
            print("You've selected B04")
        elif buy == "B05":
            print("You've selected B05")
    
        elif buy == "C01":
            print("You've selected C01")
            # Your code for C1
        elif buy == "C02":
            print("You've selected C02")
        elif buy == "C03":
            print("You've selected C03")
        elif buy == "C04":
            print("You've selected C04")
        elif buy == "C05":
            print("You've selected C05")
    

        else:  # else statement 
            print("Code invalid, try again..\n")  # when the prduct code doesn't match the actual product code availble in the vending machine 

        # Launching Each product with thier names, sugesstions, amount and stock available for the product
        if buy == "A01":                                             # For the product code A01 
            print("\nYou added Dew in your cart\n")                  # customer has chosen this product to buy and has added it to thier cart 
            # This is the suggestion which is generally given as advertisement to the customers to purchase the other product with thier product
            suggestion=input("\nTo go with your Dew, would you like some Taki Chips with it?\n [1]Yes [2] No\n")  
            if suggestion == "1" :                                 
                print("\nEnter B03 to add Taki Chips\n")             # For adding the other product, customer needs to type the product code   
            else:                                                  
                pass                                     
            balance -= 4                                             # The product price is deducted from the total amount the customer has inserted 
            purchased_item.append("Dew--4 AED")                      # product ( dew ) has its price in vending machine for 4 AED
            total.append(4)                                          
            A01_stock -= 1                                        
            if A01_stock < 1:                                        # If the particular product's stock isn't availble then this message is displayed to the customers 
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break                                           

        elif buy == "A02":                                     
            print("\nYou added Pepsi in your cart\n")           
            suggestion=input("\nTo go with your Pepsi, would you like some Sando Wafers with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                  
                print("\nEnter B01 to add Sando Wafers\n")           
            else:                                            
                pass                                           
            balance -= 3                                        
            purchased_item.append("Pepsi--3 AED")               
            total.append(3)                                    
            A02_stock -= 1                                          
            if A02_stock < 1:                                       
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break                                         

        elif buy == "A03":                                    
            print("\nYou added Coke in your cart\n")           
            suggestion=input("\nTo go with your Coke, would you like some Oman chips with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                     
                print("\nEnter B04 to add Oman chips\n")        
            else:                                                
                pass                                            
            balance -= 5                                        
            purchased_item.append("Coke--5 AED")              
            total.append(5)                                       
            A03_stock -= 1                                   
            if A03_stock < 1:                                       
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break                                            

        elif buy == "A04":                                 
            print("\nYou added Fanta in your cart\n")          
            suggestion=input("\nTo go with your Fanta, would you like some Extra Gum with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                            
                print("\nEnter B05 to add Extra Gum\n")         
            else:                                              
                pass                                   
            balance -= 6                                        
            purchased_item.append("Fanta--6 AED")                 
            total.append(6)                                       
            A04_stock -= 1                                       
            if A04_stock < 1:                                     
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break                                            

        elif buy == "A05":                                
            print("\nYou added Water in your cart\n")  
            balance -= 3                             
            purchased_item.append("Water--3 AED")                 
            total.append(3)                                     
            A05_stock -= 1                                       
            if A05_stock < 1:                                     
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break                                           

        elif buy == "B01":                                     
            print("\nYou added Sando Wafers in your cart\n")             
            suggestion=input("\nTo go with your Sando Wafers, would you like some Espresso with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                           
                print("\nEnter C02 to add Espresso\n")          
            else:                                                  
                pass                                               
            balance -= 2                                         
            purchased_item.append("Sando Wafers--2 AED")                 
            total.append(2)                                       
            B01_stock -= 1                                     
            if B01_stock < 1:                                    
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "B02":                                    
            print("\nYou added Dairy Milk in your cart\n")            
            suggestion=input("\nTo go with your Dairy Milk, would you like some Hot chocolate with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                           
                print("\nEnter C04 to add Hot chocolate\n")           
            else:                                                 
                pass                                           
            balance -= 7                                      
            purchased_item.append("Dairy Milk--7 AED")              
            total.append(7)                              
            B02_stock -= 1                                          
            if B02_stock < 1:                                       
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "B03":                                      
            print("\nYou added Taki Chips in your cart\n")            
            suggestion=input("\nTo go with your Taki Chips, would you like some Dew with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                          
                print("\nEnter A01 to add Dew\n")           
            else:                                               
                pass                                       
            balance -= 5                             
            purchased_item.append("Taki Chips--5 AED")               
            total.append(5)                                     
            B03_stock -= 1                                       
            if B03_stock < 1:                                    
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "B04":                                     
            print("\nYou added Oman chips in your cart\n")    
            suggestion=input("\nTo go with your Oman chips, would you like some Zafran Chai with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                             
                print("\nEnter C01 to add Zafran Chai\n")         
            else:                                              
                pass                                            
            balance -= 1                                          
            purchased_item.append("Oman chips--1 AED")                
            total.append(1)                                     
            B04_stock -= 1                                       
            if B04_stock < 1:                                      
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "B05":                                  
            print("\nYou added Extra Gum in your cart\n")            
            suggestion=input("\nTo go with your Extra Gum, would you like some Water with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                            
                print("\nEnter A05 to add Water\n")        
            else:                                               
                pass                                               
            balance -= 4                                        
            purchased_item.append("Extra Gum--4 AED")              
            total.append(4)                                     
            B05_stock -= 1                                          
            if B05_stock < 1:                                      
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "C01":                                   
            print("\nYou added Zafran Chai in your cart\n")       
            suggestion=input("\nTo go with your Zafran Chai, would you like some Taki Chips with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                           
                print("\nEnter B03 to add Taki Chips\n")        
            else:                                                
                pass                                              
            balance -= 3                                           
            purchased_item.append("Zafran Chai--3 AED")             
            total.append(3)                                  
            C01_stock -= 1                                          
            if C01_stock < 1:                                      
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "C02":                                   
            print("\nYou added Espresso in your cart\n")       
            suggestion=input("\nTo go with your Espresso, would you like some Sando Wafers with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                         
                print("\nEnter A01 to add Sando Wafers\n") 
            else:                                               
                pass                                               
            balance -= 10                                         
            purchased_item.append("Espresso--10 AED")                
            total.append(10)                                      
            C02_stock -= 1                                          
            if C02_stock < 1:                                     
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "C03":                                  
            print("\nYou added Cafe au lait in your cart\n")         
            suggestion=input("\nTo go with your Cafe au lait, would you like some Taki Chips with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                          
                print("\nEnter B03 to add Taki Chips\n")           
            else:                                                 
                pass                                              
            balance -= 15                                         
            purchased_item.append("Cafe au lait--15 AED")                  
            total.append(15)                                      
            C03_stock -= 1                                         
            if C03_stock < 1:                                      
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "C04":                                   
            print("\nYou added Hot chocolate in your cart\n")           
            suggestion=input("\nTo go with your Hot chocolate, would you like some Oman chips with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                             
                print("\nEnter B04 to add Oman chips\n")           
            else:                                               
                pass                                               
            balance -= 5                                        
            purchased_item.append("Hot chocolate--5 AED")         
            total.append(5)                                      
            C04_stock -= 1                                       
            if C04_stock < 1:                                     
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "C05":                                      
            print("\nYou added Cappuccino in your cart\n")          
            suggestion=input("\nTo go with your Cappuccino, would you like some Extra Gum with it?\n [1]Yes [2] No\n")
            if suggestion == "1" :                             
                print("\nEnter B05 to add Extra Gum\n")          
            else:                                               
                pass                                               
            balance -= 9                                       
            purchased_item.append("Cappuccino--9 AED")             
            total.append(9)                                       
            C05_stock -= 1                                       
            if C05_stock < 1:                                      
                print("\nSorry, this product has been sold out or is out of stock, so we've to proceeded to the payment.\n")
                break 

        elif buy == "q":                               # After adding the product to their cart and when the customer is ready to purchase the product then,
            print("Proceeding to payment..\n")         # The customer needs to type "q" for exiting the selection process and to get in the payment process
            break
            
        else:             
            print("Code invalid, try again..\n")       # If the customer has wrongly typed the exit code then this message is shown to the customers 

    if balance < 0: 
        # If the customer hasn't inserted enough money for the purchase of the product then this messsage is displeyed to the customers     
        print ("Sorry, the amount of money you've inserted is not enough. Try again.\n") 
        main() 

    else:     # The customer recieves their change in the AED currency type 
        print("Change---", balance, "AED\n")

main() # Calling the main function.

from datetime import datetime   # To add the date and time in the product reciept for showing the customers that when they have purchased this particular product from the vending machine 

now = datetime.now()
today = now.date()
# Vending Machine receipt 
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
def receipt():
    print("\n**************** 𝑽 𝒆 𝒏 𝒅 𝒊 𝒏 𝒈  𝑴 𝒂 𝒄 𝒉 𝒊 𝒏 𝒆  𝑹 𝒆 𝒄 𝒆 𝒊 𝒑 𝒕 *****************")
    print("\nItems Purchased:")
    
    for item in purchased_item:
        print(f"- {item}")

    total_amount = sum(total)
    print(f"\nTotal Amount: {total_amount} AED")

    # Display the current date and time on the receipt
    print("\nDate and Time of Purchase:", now)

    print("********************* 𝓗 𝓪 𝓿 𝓮  𝓪  𝓖 𝓻 𝓮 𝓪 𝓽  𝓓 𝓪 𝔂 ❗ ************************")
    print("OWNED BY - MOHAMMED FAISAL")

receipt()
print("---------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------")