Product_details=[]
Supplier_details={}
Customer_details=[]
Gender={}
f1=open("C:\\535_tanuja\\Sales.csv","r")
while True:
  data=f1.readline()
  if not data:
   break;
  data=data.replace("\n","")
  temp=data.split(",")
  Product_details.append(temp[1])
  Customer_details.append(temp[3])
  Supplier_details.update({temp[0]:temp[2]})
  Gender.update({temp[3]:temp[4]})
f1.close()
Customer_details=tuple(Customer_details)
print(type(Customer_details))
print("Product_details",Product_details)
print("\n\nSupplier_details",Supplier_details)
print("\n\nCustomer_details",Customer_details)
print("\n\nGender",Gender)
#2 MOST POPULAR PRODUCT
frequency={}
for item in Product_details:
   if item in frequency:
    frequency[item]+=1
   else:
    frequency[item]=1
#printing the frequency
print(frequency)
marklist=sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("\nThe Most Popular Product for Sales",list(sortdict.keys()),"Sold",list(sortdict.values())[0],"Items")
#3 BEST SUPPLIER
frequency={}
for item in Supplier_details:
  if item in frequency:
    frequency[item]+=1
  else:
    frequency[item]=1
#printing the frequency
print(frequency)
marklist=sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("\nThe Most Popular Supplier for Sales",list(sortdict.keys())[0],"Sold",list(sortdict.values())[0],"Items")
#4 MOST PRODUCT BUYER CUSTOMER
frequency={}
for item in Customer_details:
  if item in frequency:
   frequency[item]+=1
  else:
   frequency[item]=1
#printing the frequency
print(frequency)
marklist=sorted(frequency.items(), key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("\nThe Most of the product buyer customer",list(sortdict.keys())[0],"Sold",list(sortdict.values())[0],"Items")
#5 FEMALE CUSTOMER
from collections import Counter
counter=dict(Counter(Gender))
names=list(counter.keys())
print(names)
male=0
female=0
for name in names:
  if Gender[name]=="Male":
   male=male+1
  if Gender[name]=="Female":
   female+=1
print("Total no of Females=",female)