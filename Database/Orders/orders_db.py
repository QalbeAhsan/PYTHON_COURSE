import order_queries as oq

 
oq.create_table('name','price','address','receiver') #We call the function to create table

oq.insert_one('car',200,'ST_24 ','harry')  #we call the function to insert order:
print("Your Order Is Added Successfully:")


addingorders=[('bus',500,'House 19 ','hamza'),
              ('watch',250,'St_05 ','joseph'),
              ('flower',900,'St_78 ','mike'),
              ('bottles',900,'St_08','jason'),
              ('chair',1500,'St_12','max') 
              ]
print("Your Orders are Added Successfully:")
oq.insert_many(addingorders)


oq.show_details()   #We call the function to retrieve our orders details